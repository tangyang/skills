# OPENCLAW_SETUP

## Recommended skills

- `skills/meitu-video-motion-transfer/SKILL.md`
- `skills/meitu-image-edit/SKILL.md`
- `skills/meitu-image-generate/SKILL.md`
- `skills/meitu-image-upscale/SKILL.md`
- `skills/meitu-image-virtual-tryon/SKILL.md`
- `skills/meitu-image-to-video/SKILL.md`
- `skills/meitu-image-face-swap/SKILL.md`
- `skills/meitu-image-cutout/SKILL.md`

## Trigger pattern

Recommended: invoke the capability skill directly.

Example prompts:

```text
Use meitu-image-edit.
Input:
{"image":["https://obs.mtlab.meitu.com/public/resources/aigensource.png"],"prompt":"把背景改成雪山，人物保持不变，写实风格","size":"2K","output_format":"jpeg","ratio":"auto"}
```

```text
Use meitu-image-upscale.
Input:
{"image":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}
```
