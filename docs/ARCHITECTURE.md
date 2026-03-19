# ARCHITECTURE

## Goal

Use a scalable skill-pack layout for GitHub publishing and OpenClaw consumption:
- one capability = one skill
- one shared runner for all capabilities

## Why this structure

1. Clear invocation boundary
- Users can select a capability skill directly without routing ambiguity.

2. Easier extension
- Add a new capability by adding one new skill folder and one command spec entry.

3. Stable maintenance
- Shared runner keeps validation and response format consistent.

## Current pattern

- Capability skills live under `skills/meitu-*`.
- Shared execution logic lives in `skills/_shared/run_command.py`.
- Every capability skill calls the shared runner with a fixed built-in command.

## Add a new capability

1. Update `skills/_shared/run_command.py`:
- add command spec
- add optional Chinese command alias
- add input key aliases if needed

2. Add a new capability skill folder:
- `skills/meitu-<new-capability>/SKILL.md`

3. Add example and docs:
- update `examples/`
- update `README.md`
