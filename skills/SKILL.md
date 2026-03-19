---
name: meitu-ai
description: Unified Meitu AI command skill. Use this skill to choose built-in command, validate user inputs, and execute through the Python runner. Return task id and final media URL.
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
4. Decide `command` from user intent.
5. Validate required input keys for that command.
6. Execute runner command.
7. Return `task_id` and final `media_urls`.

Run:

```bash
python3 scripts/run_command.py --command "<command>" --input-json '<json object>'
```

Supported commands and input keys:
- `video-motion-transfer`
  - required: `image_url`, `video_url`, `prompt`
- `image-edit`
  - required: `image`, `prompt`
  - optional: `size`, `output_format`, `ratio`
- `image-generate`
  - required: `prompt`
  - optional: `image`, `size`
- `image-upscale`
  - required: `image`
  - optional: `model_type`
- `image-virtual-tryon`
  - required: `clothes_image_url`, `person_image_url`
  - optional: `replace`, `need_sd`
- `image-to-video`
  - required: `image`, `prompt`
  - optional: `video_duration`, `ratio`
- `image-face-swap`
  - required: `head_image_url`, `sence_image_url`, `prompt`
- `image-cutout`
  - required: `image`
  - optional: `model_type`

Output fields:
- `ok`
- `command`
- `task_id`
- `media_urls`
- `result`
