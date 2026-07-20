import json
from pathlib import Path

# 当前目录
BASE_DIR = Path(__file__).parent

# Prompt 模板
PROMPT_FILE = BASE_DIR / "Prompts" / "default.txt"

# 风格配置
STYLE_FILE = BASE_DIR / "styles.json"


def build_prompt(keyword, style, platform_prompt):
    # 读取 Prompt 模板
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    # 读取风格配置
    with open(STYLE_FILE, "r", encoding="utf-8") as f:
        styles = json.load(f)

    # 如果用户输入不存在，就默认使用 5（木泽OPC风格）
    style_info = styles.get(style, styles["5"])

    # 替换模板中的占位符
    prompt = template.format(
    keyword=keyword,
    style_prompt=style_info["prompt"],
    platform_prompt=platform_prompt
)

    return prompt