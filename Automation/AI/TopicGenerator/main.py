from save import save_markdown
from prompts import build_prompt
from llm import chat

keyword = input("请输入今天的视频关键词：")

prompt = build_prompt(keyword)

print("Prompt长度：", len(prompt))

result = chat(prompt)

print("\n====================\n")
print(result)

filepath = save_markdown(keyword, result)

print("\n====================")
print("已保存到：")
print(filepath)