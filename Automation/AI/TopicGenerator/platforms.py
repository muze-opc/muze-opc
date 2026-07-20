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


def choose_platforms():
    print("\n请选择发布平台（可多选）：\n")

    keys = list(PLATFORMS.keys())

    for i, key in enumerate(keys, start=1):
        print(f"{i}. {PLATFORMS[key]['name']}")

    while True:
        choices = input("请输入编号（例如：1 2 3）：").split()

        result = []
        valid = True

        for choice in choices:

            if not choice.isdigit():
                valid = False
                break

            choice = int(choice)

            if 1 <= choice <= len(keys):
                result.append(keys[choice - 1])
            else:
                valid = False
                break

        if valid and result:
            return result

        print("输入无效，请重新输入。")


def get_platform_prompt(platform):
    return PLATFORMS[platform]["prompt"]