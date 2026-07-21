import re
from datetime import datetime


def safe_filename(text: str) -> str:
    """
    将字符串转换为安全文件名
    """
    text = text.strip()
    text = text.replace(" ", "-")
    text = re.sub(r'[\\/:*?"<>|]', "-", text)
    return text


def current_time():
    """
    返回当前时间
    格式：2026-07-22_10-30-15
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def current_date():
    """
    返回当前日期
    格式：2026-07-22
    """
    return datetime.now().strftime("%Y-%m-%d")


def divider(length=60):
    """
    打印分隔线
    """
    print("=" * length)


def blank():
    """
    打印空行
    """
    print()


def title(text):
    """
    打印标题
    """
    divider()
    print(text)
    divider()