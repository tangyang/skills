# VERSIONING

## Pack versioning

Use SemVer for this repository:
- MAJOR: incompatible config/schema changes
- MINOR: new effects, backward-compatible behavior
- PATCH: bugfixes and docs updates

## Runtime compatibility

Target runtime:
- `meitu-ai` command interface with `generate` subcommand

Runner command resolution order:
1. `MEITU_AI_CMD` env override
2. `meitu-ai`
