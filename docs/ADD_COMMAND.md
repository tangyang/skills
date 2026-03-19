# ADD_COMMAND

Add a new built-in command and capability skill.

## Steps

1. Edit `skills/_shared/run_command.py`.
2. Add or update one command entry in `COMMAND_SPECS`.
3. Define only user input keys:
- `required_keys`
- `optional_keys`
- `array_keys`
4. Create one new skill folder under `skills/` (for example `skills/meitu-xxx/SKILL.md`) and bind it to the new command.
5. Validate with a minimal run:

```bash
python3 skills/_shared/run_command.py \
  --command <command_name> \
  --input-json '{...}'
```

## Input principle

- Only expose keys users actually need to fill.
- Do not expose internal routing details in documents.
