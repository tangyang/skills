# OPENCLAW_SETUP

## Recommended skill enable order

1. `skills/meitu-ai-effect/SKILL.md`

## Trigger pattern

- Use the same skill for routing and execution.
- Provide `effect_id` and JSON input directly.

Example prompt:

```text
Use meitu-ai-effect.
Run effect_id=488176 with:
{"image_url":"https://obs.mtlab.meitu.com/public/resources/aigensource.png","prompt":"把背景改成雪山，人物保持不变，写实风格","size":"2K","output_format":"jpeg","ratio":"auto"}
```
