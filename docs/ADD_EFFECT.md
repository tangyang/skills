# ADD_EFFECT

Add a new effect by configuration only (no new script by default).

## Steps

1. Copy template:

```bash
cp skills/meitu-ai-effect/effects/_template.json \
   skills/meitu-ai-effect/effects/<effect_id>.json
```

2. Fill fields:
- `effect_id`
- `task_type` (usually `formula`)
- `media_input`
- `parameter` block

3. Register in `effects/index.json`.

4. Validate with a minimal run:

```bash
python3 skills/meitu-ai-effect/scripts/run_effect.py \
  --effect-id <effect_id> \
  --input-json '{...}'
```

## Parameter principle

- Only pass dynamic keys declared by that effect config.
- Keep static parameters out of runtime request payload when they are already fixed by effect id.
