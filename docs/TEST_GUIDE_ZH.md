# 龙虾测试说明（给测试同学）

本文档用于让测试同学快速验证 `meitu-ai-skillpack` 在龙虾（OpenClaw）中的可用性。

## 1. 拉取 GitHub 项目

```bash
# HTTPS
git clone https://github.com/tangyang/skills.git

# 或 SSH
git clone git@github.com:tangyang/skills.git

cd skills
git pull
```

## 2. 安装 CLI（meitu-ai）

```bash
# 首次安装
pipx install --force meitu-ai

# 如果已安装，建议升级到最新
pipx upgrade meitu-ai
```

检查命令是否可用：

```bash
meitu --help
```

## 3. 配置凭证

二选一即可。

方式 A：环境变量（推荐）

```bash
export OPENAPI_ACCESS_KEY="你的AK"
export OPENAPI_SECRET_KEY="你的SK"
```

方式 B：文件

创建 `~/.openapi/credentials.json`：

```json
{
  "accessKey": "你的AK",
  "secretKey": "你的SK"
}
```

## 4. 先做 CLI 冒烟验证（不经过龙虾）

```bash
cd /path/to/skills
python3 skills/meitu-ai/scripts/run_command.py \
  --command image-upscale \
  --input-json '{"image":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}'
```

通过标准：
- 返回 JSON 中包含 `ok: true`
- 包含 `task_id`
- `media_urls` 中有可访问的结果链接

## 5. 把 Skill 放到龙虾工作区

```bash
mkdir -p ~/.openclaw/workspace/skills
rsync -a /path/to/skills/skills/ ~/.openclaw/workspace/skills/
```

说明：
- 这里同步的是本项目里的 `skills/` 子目录（含 `meitu-ai` 基础 skill 和各场景目录）。
- 如果龙虾已经在运行，建议重开一个新会话再测。

## 6. 在龙虾里测试（腾讯文档粘贴友好）

以下是可直接复制的内容。建议整行复制到龙虾输入框。

1. 图片超清
/skill meitu-image-upscale input={"image":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}

2. 图片编辑
/skill meitu-image-edit input={"image":["https://obs.mtlab.meitu.com/public/resources/aigensource.png"],"prompt":"把背景改成雪山，人物保持不变，写实风格","size":"2K","output_format":"jpeg","ratio":"auto"}

3. 图片生成
/skill meitu-image-generate input={"prompt":"一位站在雪山前的亚洲女性，写实摄影风格，电影级光影，细节清晰","size":"2K"}

4. 抠图
/skill meitu-image-cutout input={"image":"https://obs.mtlab.meitu.com/public/resources/aigensource.png"}

5. 换头像
/skill meitu-image-face-swap input={"head_image_url":"https://obs.mtlab.meitu.com/public/resources/aigensource.png","sence_image_url":"https://meitu-commons-test.obs.cn-north-4.myhuaweicloud.com/autotest/aipaintingtext1.jpg","prompt":"自然融合，保持肤色一致，写实风格"}

6. 试衣（请准备两张可访问图片）
/skill meitu-image-virtual-tryon input={"clothes_image_url":"<衣服图片URL>","person_image_url":"<人物图片URL>"}

7. 文章转海报（同事提供的最终 skill）
/skill article-to-cover
请把下面这段内容做成一张中文海报封面，风格偏科技感，主标题醒目，适合公众号头图：
“AI 图像能力平台上线，支持图片编辑、超清、换头像、试衣、图生视频等功能，面向开发者开放测试。”

## 7. 验收标准

每条测试建议记录：
- 触发时间
- 使用的 skill 名称
- 输入参数（或 prompt）
- 返回的 `task_id`
- 最终结果 URL
- 是否成功（成功/失败）

建议最少通过：
- `meitu-image-upscale`
- `meitu-image-edit`
- `meitu-image-generate`
- `article-to-cover`

## 8. 常见问题

1. `meitu: command not found`
- 执行 `pipx ensurepath` 后重新打开终端。

2. 凭证错误/鉴权失败
- 检查 AK/SK 是否生效，或 `~/.openapi/credentials.json` 字段名是否为 `accessKey`、`secretKey`。

3. 返回无结果 URL
- 先确认输入图片 URL 可公网访问，再重试。

4. 龙虾未触发到指定 skill
- 优先使用 `/skill <skill-name> input=...` 强触发格式。
