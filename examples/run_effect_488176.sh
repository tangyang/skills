#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
python3 "$ROOT_DIR/skills/meitu-ai-effect/scripts/run_effect.py" \
  --effect-id 488176 \
  --input-json '{"image_url":"https://obs.mtlab.meitu.com/public/resources/aigensource.png","prompt":"把背景改成雪山，人物保持不变，写实风格","size":"2K","output_format":"jpeg","ratio":"auto"}'
