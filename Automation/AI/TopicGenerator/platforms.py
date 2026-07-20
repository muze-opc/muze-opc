import json
from pathlib import Path


root = Path(__file__).resolve().parents[3]

platform_file = (
    root
    / "Automation"
    / "AI"
    / "TopicGenerator"
    / "platforms.json"
)


with open(platform_file, "r", encoding="utf-8") as f:
    PLATFORMS = json.load(f)


def choose_platform():
    print("\n请选择发布平台：\n")

    keys = list(PLATFORMS.keys())

    for i, key in enumerate(keys, start=1):
        print(f"{i}. {PLATFORMS[key]['name']}")

    while True:
        choice = input("请输入编号：").strip()

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(keys):
                return keys[choice - 1]

        print("输入无效，请重新输入。")

    return keys[choice - 1]

def get_platform_prompt(platform):
    return PLATFORMS[platform]["prompt"]