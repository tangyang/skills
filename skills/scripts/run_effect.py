import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


PROFILE = {
    "media_profiles": {"media_data_type": "url"},
    "version": "v1",
}


def _load_openapi_credentials_from_file() -> dict:
    cred_path = Path.home() / ".openapi" / "credentials.json"
    if not cred_path.is_file():
        return {}
    try:
        payload = json.loads(cred_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    ak = str(payload.get("accessKey") or "").strip()
    sk = str(payload.get("secretKey") or "").strip()
    if not ak or not sk:
        return {}
    return {
        "OPENAPI_ACCESS_KEY": ak,
        "OPENAPI_SECRET_KEY": sk,
    }


def resolve_cli_command() -> str:
    override = str(os.getenv("MEITU_AI_CMD") or "").strip()
    if override:
        return override

    for name in ("meitu-ai", "meitu"):
        found = shutil.which(name)
        if found:
            return found

    fallback = Path.home() / "Library" / "Python" / "3.11" / "bin" / "meitu"
    if fallback.is_file():
        return str(fallback)

    raise RuntimeError("meitu-ai/meitu command not found; install runtime first")


def build_env() -> dict:
    env = dict(os.environ)
    has_ak = str(env.get("OPENAPI_ACCESS_KEY") or "").strip()
    has_sk = str(env.get("OPENAPI_SECRET_KEY") or "").strip()
    if has_ak and has_sk:
        return env

    bridged = _load_openapi_credentials_from_file()
    if bridged:
        env.update(bridged)
    return env


def run_generate(
    cli_cmd: str,
    task: str,
    task_type: str,
    init_images_json: str,
    params_json: str,
    rsp_media_type: str,
) -> subprocess.CompletedProcess:
    cmd = [
        cli_cmd,
        "generate",
        "--task",
        task,
        "--task-type",
        task_type,
        "--init-images-json",
        init_images_json,
        "--params-json",
        params_json,
        "--rsp-media-type",
        rsp_media_type,
        "--json",
    ]
    return subprocess.run(cmd, capture_output=True, text=True, env=build_env())


def effects_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "effects"


def load_effect_config(effect_id: str) -> dict:
    path = effects_dir() / f"{effect_id}.json"
    if not path.is_file():
        raise RuntimeError(f"effect config not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"invalid effect config json: {path}") from exc


def require_non_empty_string(value, field_name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise RuntimeError(f"{field_name} is required")
    return text


def validate_allowed_keys(input_payload: dict, allowed_keys: list[str]) -> None:
    if not allowed_keys:
        return
    unknown = [key for key in input_payload.keys() if key not in allowed_keys and key != "image_url"]
    if unknown:
        raise RuntimeError(f"unsupported input keys: {unknown}")


def build_init_images_json(effect_cfg: dict, user_input: dict) -> str:
    media_cfg = effect_cfg.get("media_input") or {}
    input_key = str(media_cfg.get("input_key") or "image_url")
    media_type = str(media_cfg.get("type") or "single_url")

    if media_type == "single_url":
        image_url = require_non_empty_string(user_input.get(input_key), input_key)
        payload = [{"url": image_url, "profile": PROFILE}]
        return json.dumps(payload, ensure_ascii=False)

    if media_type == "url_array":
        raw_list = user_input.get(input_key)
        if not isinstance(raw_list, list) or not raw_list:
            raise RuntimeError(f"{input_key} must be a non-empty array")
        payload = [{"url": require_non_empty_string(item, input_key), "profile": PROFILE} for item in raw_list]
        return json.dumps(payload, ensure_ascii=False)

    raise RuntimeError(f"unsupported media_input.type: {media_type}")


def build_params_json(effect_cfg: dict, user_input: dict) -> str:
    parameter_cfg = effect_cfg.get("parameter") or {}
    allowed_keys = list(parameter_cfg.get("allowed_keys") or [])
    required_keys = list(parameter_cfg.get("required_keys") or [])
    defaults = dict(parameter_cfg.get("defaults") or {})
    wrap_mode = str(parameter_cfg.get("wrap_mode") or "none")

    merged = dict(defaults)
    for key in allowed_keys:
        if key in user_input and user_input.get(key) is not None:
            merged[key] = user_input.get(key)

    for key in required_keys:
        if str(merged.get(key) or "").strip() == "":
            raise RuntimeError(f"{key} is required for effect {effect_cfg.get('effect_id')}")

    if wrap_mode == "parameter":
        return json.dumps({"parameter": merged}, ensure_ascii=False)

    if wrap_mode == "none":
        return json.dumps(merged, ensure_ascii=False)

    raise RuntimeError(f"unsupported parameter.wrap_mode: {wrap_mode}")


def extract_media_urls(result: dict) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()

    def add(value) -> None:
        text = str(value or "").strip()
        if not text or text in seen:
            return
        seen.add(text)
        urls.append(text)

    data = result.get("data") or {}
    output = data.get("result") or {}

    for item in output.get("media_info_list", []):
        if isinstance(item, dict):
            add(item.get("media_data"))

    for item in output.get("urls", []):
        add(item)

    add(output.get("url"))
    return urls


def extract_result_id(result: dict) -> str:
    data = result.get("data") or {}
    output = data.get("result") or {}
    return str(output.get("id") or data.get("task_id") or "").strip()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Meitu AI effect by effect_id.")
    parser.add_argument("--effect-id", required=True, help="effect id, for example 488178")
    parser.add_argument("--input-json", required=True, help="input object json")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    effect_id = str(args.effect_id).strip()
    if not effect_id:
        print(json.dumps({"ok": False, "error": "effect_id is required"}, ensure_ascii=False))
        return 2

    try:
        user_input = json.loads(args.input_json)
    except Exception:
        print(json.dumps({"ok": False, "error": "input-json must be valid json object"}, ensure_ascii=False))
        return 2

    if not isinstance(user_input, dict):
        print(json.dumps({"ok": False, "error": "input-json must be json object"}, ensure_ascii=False))
        return 2

    try:
        effect_cfg = load_effect_config(effect_id)
        allowed_keys = list((effect_cfg.get("parameter") or {}).get("allowed_keys") or [])
        validate_allowed_keys(user_input, allowed_keys)

        init_images_json = build_init_images_json(effect_cfg, user_input)
        params_json = build_params_json(effect_cfg, user_input)

        cli_cmd = resolve_cli_command()
        task_type = str(effect_cfg.get("task_type") or "formula")
        rsp_media_type = str(effect_cfg.get("rsp_media_type") or "url")

        res = run_generate(
            cli_cmd=cli_cmd,
            task=effect_id,
            task_type=task_type,
            init_images_json=init_images_json,
            params_json=params_json,
            rsp_media_type=rsp_media_type,
        )

        stdout = (res.stdout or "").strip()
        stderr = (res.stderr or "").strip()
        if not stdout:
            print(
                json.dumps(
                    {
                        "ok": False,
                        "effect_id": effect_id,
                        "error": stderr or "empty cli output",
                        "exit_code": res.returncode,
                    },
                    ensure_ascii=False,
                )
            )
            return 1

        try:
            payload = json.loads(stdout)
        except Exception:
            print(
                json.dumps(
                    {
                        "ok": False,
                        "effect_id": effect_id,
                        "error": "invalid cli json output",
                        "exit_code": res.returncode,
                        "stdout": stdout,
                        "stderr": stderr,
                    },
                    ensure_ascii=False,
                )
            )
            return 1

        ok = res.returncode == 0 and payload.get("code") == 0
        output = {
            "ok": ok,
            "effect_id": effect_id,
            "task_type": task_type,
            "result_id": extract_result_id(payload),
            "media_urls": extract_media_urls(payload),
            "result": payload,
        }
        if not ok:
            output["exit_code"] = res.returncode
            if stderr:
                output["stderr"] = stderr

        print(json.dumps(output, ensure_ascii=False))
        return 0 if ok else 1

    except Exception as exc:
        print(json.dumps({"ok": False, "effect_id": effect_id, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
