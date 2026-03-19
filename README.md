# meitu-ai-skillpack

Command-based skill pack for OpenClaw, powered by `meitu-ai`.

This pack provides:
- one skill per capability (9 skills)
- a shared runner script: `skills/_shared/run_command.py`

Capabilities:
- `meitu-video-motion-transfer` -> `video-motion-transfer` (动作迁移)
- `meitu-image-edit` -> `image-edit` (图片编辑)
- `meitu-image-generate` -> `image-generate` (图片生成)
- `meitu-image-upscale` -> `image-upscale` (图片超清)
- `meitu-image-virtual-tryon` -> `image-virtual-tryon` (试衣)
- `meitu-image-to-video` -> `image-to-video` (图生视频)
- `meitu-image-face-swap` -> `image-face-swap` (换头像)
- `meitu-image-cutout` -> `image-cutout` (抠图)
- `article-to-cover` -> `image-generate` (文章转海报/封面设计)

## Quick Start

1. Install runtime CLI

```bash
pipx install --force meitu-ai
```

Runtime requirement:
- `meitu-ai >= 0.1.2` (must include built-in commands like `image-edit`, `image-upscale`)

2. Configure credentials

Set either:
- `OPENAPI_ACCESS_KEY` and `OPENAPI_SECRET_KEY`

or place credentials in:
- `~/.openapi/credentials.json`

3. Run a built-in command

```bash
python3 skills/_shared/run_command.py \
  --command image-upscale \
  --input-json '{"image":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}'
```

## Recommended GitHub structure

```text
meitu-ai-skillpack/
  README.md
  docs/
  examples/
  skills/
    _shared/
      run_command.py
    meitu-video-motion-transfer/
      SKILL.md
    meitu-image-edit/
      SKILL.md
    meitu-image-generate/
      SKILL.md
    meitu-image-upscale/
      SKILL.md
    meitu-image-virtual-tryon/
      SKILL.md
    meitu-image-to-video/
      SKILL.md
    meitu-image-face-swap/
      SKILL.md
    meitu-image-cutout/
      SKILL.md
    article-to-cover/
      SKILL.md
      references/
```

See `docs/` for OpenClaw setup, extension strategy, and maintenance rules.

## Image command examples

See `examples/README.md` for ready-to-run image command scripts.
