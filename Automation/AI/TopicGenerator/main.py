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

prompt = build_prompt(keyword, style)

print("Prompt长度：", len(prompt))

result = chat(prompt)

print("\n====================\n")
print(result)

filepath = save_markdown(keyword, result)

print("\n====================")
print("已保存到：")
print(filepath)