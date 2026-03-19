---
name: meitu-ai
description: Top-level entry skill for Meitu image tasks such as 抠图, 人像抠图, 去背景, 去除背景, 背景去除, background removal, remove background, and other Meitu image editing requests. Use this skill first when multiple Meitu skills are available. It decides which underlying Meitu skill should run and then delegates execution.
---

Use this skill as the top-level router when the user describes an image-editing scenario and the system needs to choose the correct underlying Meitu skill.

Prerequisites:
- The `meitu` CLI must already be installed and available on `PATH`.
- Recommended install for external CLI usage: `pipx install meitu-cli`
- Local repository install: `pipx install /path/to/openapi-cli/cli`
- Alternative install: `pip install /path/to/openapi-cli/cli`

Inputs:
- request: required freeform user request or operation description
- image_path: required local image file path
- route: optional explicit route override, for example `intelligent_cutout`

Execution:
Run:
python3 scripts/dispatch.py \
  --request "<request>" \
  --image-path "<image_path>" \
  --route "<route>"

Behavior:
- Prefer explicit `route` when provided.
- Otherwise, evaluate the route table. Each route can define direct phrase matches plus grouped match rules for more natural language coverage.
- Route table:
  - cutout, background removal, remove background, transparent background, `抠图`, `去背景`, or `去除背景` -> `Intelligent Cutout Executor`
- Do not reimplement Meitu API logic in the router. The router should call the selected skill script and return its result.
- Do not expose downstream algorithm-specific parameters as part of the router's public contract. Those belong to the selected leaf skill.
- If no route matches, return a clear unsupported response and list the currently available routes.

Return:
- ok
- selected_skill
- selected_route
- matched_terms
- request
- image_path
- result

Notes:
- Credentials should come from the meitu local config or environment.
- Do not print access key or secret key.
- Keep the router lightweight. Add new skills by extending the route table rather than duplicating business logic here.
