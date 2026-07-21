import json
from pathlib import Path

STYLE_FILE = Path(__file__).parent / "styles.json"

with open(STYLE_FILE, "r", encoding="utf-8") as f:
    STYLES = json.load(f)


def choose_style():
    """
    选择创作风格
    """

    print("\n请选择创作风格：\n")

    keys = list(STYLES.keys())

    for i, key in enumerate(keys, start=1):
        print(f"{i}. {STYLES[key]['name']}")

    while True:

        choice = input("请输入编号：").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(keys):
                return keys[choice - 1]

        print("输入无效，请重新输入。")