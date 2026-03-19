# INSTALL

## Runtime

Recommended:

```bash
pipx install meitu-ai
```

## Credentials

Preferred:

```bash
export OPENAPI_ACCESS_KEY="..."
export OPENAPI_SECRET_KEY="..."
```

Fallback:
- `~/.openapi/credentials.json` with keys `accessKey` and `secretKey`.

## Verification

```bash
python3 skills/meitu-ai-effect/scripts/run_effect.py \
  --effect-id 488178 \
  --input-json '{"image_url":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}'
```
