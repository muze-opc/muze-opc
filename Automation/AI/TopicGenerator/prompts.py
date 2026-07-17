import json
from pathlib import Path


# styles.json 文件路径
STYLE_FILE = Path(__file__).parent / "styles.json"


def build_prompt(keyword, style):
    # 读取 JSON
    with open(STYLE_FILE, "r", encoding="utf-8") as f:
        styles = json.load(f)

    # 获取对应风格
    style_info = styles.get(style, styles["5"])

    return f"""
你是一名专业的AI自媒体策划。

请围绕「{keyword}」生成：

1. 三个视频标题
2. 一个3秒Hook
3. 一个60秒视频脚本
4. 三个适合的话题标签

创作风格：

{style_info["prompt"]}

要求：

- 中文输出
- 适合抖音、视频号
- 内容真实
- 有故事感
"""