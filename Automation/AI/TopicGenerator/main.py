from platforms import choose_platform, get_platform_prompt
from prompts import build_prompt
from llm import chat
from save import save_markdown

import json
from pathlib import Path

STYLE_FILE = Path(__file__).parent / "styles.json"

with open(STYLE_FILE, "r", encoding="utf-8") as f:
    styles = json.load(f)

keyword = input("请输入今天的视频关键词：")

print("\n请选择创作风格：\n")

for key, value in styles.items():
    print(f"{key}. {value['name']}")

style = input("请输入编号：")

platform = choose_platform()
platform_prompt = get_platform_prompt(platform)

print("\n平台要求：")
print(platform_prompt)

print(f"\n当前平台：{platform}")

prompt = build_prompt(
    keyword,
    style,
    platform_prompt
)

print("Prompt长度：", len(prompt))

result = chat(prompt)

print("\n====================\n")
print(result)

filepath = save_markdown(
    keyword,
    result,
    platform
)

print("\n====================")
print("已保存到：")
print(filepath)