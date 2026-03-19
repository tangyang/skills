# meitu-ai-skillpack

Effect-ID based skill pack for OpenClaw, powered by `meitu-ai`.

This pack provides:
- `meitu-ai-effect`: unified strategy + execution skill
- a reusable runner script driven by `effects/*.json`

## Quick Start

1. Install runtime CLI

```bash
pipx install meitu-ai
```

2. Configure credentials

Set either:
- `OPENAPI_ACCESS_KEY` and `OPENAPI_SECRET_KEY`

or place credentials in:
- `~/.openapi/credentials.json`

3. Run an effect

```bash
python3 skills/meitu-ai-effect/scripts/run_effect.py \
  --effect-id 488178 \
  --input-json '{"image_url":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}'
```

See `docs/` for OpenClaw setup, effect expansion, and versioning strategy.
