from pathlib import Path

from config import OUTPUT_DIR
from utils import safe_filename, current_time


def save_markdown(keyword, content, platform):
    """
    保存 Markdown 文件
    """

    # 日期（只保留年月日，用于发布包目录）
    from utils import safe_filename, current_date

today = current_date()

    # 安全关键词
    safe_keyword = safe_filename(keyword)

    # 发布包目录
    package_dir = OUTPUT_DIR / f"{today}-{safe_keyword}"
    package_dir.mkdir(parents=True, exist_ok=True)

    # 文件名
    filepath = package_dir / f"{platform}.md"

    # 写入 Markdown
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {keyword}\n\n")
        f.write(content)

    return filepath