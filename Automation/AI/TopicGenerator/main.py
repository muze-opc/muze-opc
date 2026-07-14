from llm import chat
from prompts import build_prompt

keyword = input("请输入今天的视频关键词：")

result = chat(build_prompt(keyword))

print("\n====================\n")
print(result)