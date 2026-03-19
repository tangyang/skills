---
name: meitu-ai
description: Unified Meitu AI effect skill. Use this skill to choose effect_id, validate required inputs, and execute effect calls through a config-driven Python runner. Return result id and final media URL.
---

Use this single skill for both routing and execution.

Prerequisites:
- Install runtime CLI:
  - `pipx install meitu-ai`
- Configure credentials (one of the following):
  - Environment variables: `OPENAPI_ACCESS_KEY` and `OPENAPI_SECRET_KEY`
  - Local file: `~/.openapi/credentials.json` with keys `accessKey` and `secretKey`

Workflow:
1. Decide `effect_id` from user intent.
2. Validate required keys for that effect.
3. Execute runner command.
4. Return `result_id` and final `media_urls`.

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
