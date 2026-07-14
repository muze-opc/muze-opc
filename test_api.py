import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('LLM_API_KEY')}",
    "Content-Type": "application/json",
}

data = {
    "model": os.getenv("LLM_MODEL"),
    "messages": [
        {
            "role": "user",
            "content": "你好"
        }
    ]
}

r = requests.post(
    f"{os.getenv('LLM_BASE_URL')}/chat/completions",
    headers=headers,
    json=data,
)

print("状态码：", r.status_code)
print("响应：")
print(r.text)