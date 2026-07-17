from prompts import build_prompt
from llm import chat

keyword = input("请输入今天的视频关键词：")

prompt = build_prompt(keyword)

print("Prompt长度：", len(prompt))

result = chat(prompt)

print("\n====================\n")
print(result)