---
name: meitu-ai
description: Unified Meitu AI effect skill. Use this skill to choose effect_id, validate required inputs, and execute effect calls through a config-driven Python runner. Return result id and final media URL.
---

Use this single skill for both routing and execution.

Prerequisites:
- Configure credentials (one of the following):
  - Environment variables: `OPENAPI_ACCESS_KEY` and `OPENAPI_SECRET_KEY`
  - Local file: `~/.openapi/credentials.json` with keys `accessKey` and `secretKey`

Workflow:
1. **Ensure Python 3.9+ is installed**:
   - Run: `python3 --version` to check if installed
   - If not found or version < 3.9:
     - macOS: `brew install python@3.11` (or latest stable)
     - Linux (Debian/Ubuntu): `sudo apt-get update && sudo apt-get install -y python3.11` (or latest stable)
     - Linux (RHEL/CentOS): `sudo yum install -y python3.11` (or latest stable)
   - Verify python3 version is 3.9 or higher before proceeding
2. **Ensure pipx is installed**:
   - Run: `pipx --version` to check if installed
   - If not found:
     - macOS: `brew install pipx && pipx ensurepath`
     - Linux: `python3 -m pip install --user pipx && pipx ensurepath`
   - Verify pipx is available before proceeding
3. **Check and update/install meitu-ai CLI**:
   - Run: `meitu --version` to check if installed
   - If installed: update to latest via `pipx upgrade meitu-ai`
   - If not found: auto-install via `pipx install meitu-ai`
   - Verify installation/update succeeded before proceeding
4. Decide `effect_id` from user intent.
5. Validate required keys for that effect.
6. Execute runner command.
7. Return `result_id` and final `media_urls`.

Run:

```bash
python3 scripts/run_effect.py --effect-id "<effect_id>" --input-json '<json object>'
```

Input contract:
- `effect_id`: required
- `input-json`: required object

Validated effects:
- `488178`
  - required: `image_url`
- `488176`
  - required: `image_url`, `prompt`
  - optional: `size` (default `2K`), `output_format` (default `jpeg`), `ratio` (default `auto`)

Output fields:
- `ok`
- `effect_id`
- `result_id`
- `media_urls`
- `result`
