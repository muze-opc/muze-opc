import requests
from config import API_KEY, BASE_URL, MODEL


def chat(prompt: str):
    print("API_KEY:", API_KEY[:10] + "..." if API_KEY else None)
    print("BASE_URL:", repr(BASE_URL))
    print("MODEL:", repr(MODEL))

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    print("Request JSON:", data)

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=data,
        timeout=60,
    )

    print("Status:", response.status_code)
    print("Body:", response.text)

    if response.status_code != 200:
        print("========== 返回内容 ==========")
        print(response.text)
        return None

    return response.json()["choices"][0]["message"]["content"]