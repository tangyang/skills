#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
python3 "$ROOT_DIR/skills/meitu-ai-effect/scripts/run_effect.py" \
  --effect-id 488178 \
  --input-json '{"image_url":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}'
