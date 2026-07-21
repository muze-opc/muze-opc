from pathlib import Path

from utils import safe_filename, current_date


def save_markdown(keyword, content, platform):
    """
    保存 Markdown 文件
    """

    # 项目根目录
    root = Path(__file__).resolve().parents[3]

    # 日期
    today = current_date()

    # 安全文件名
    safe_keyword = safe_filename(keyword)

    # 输出目录
    package_dir = root / "Output" / f"{today}-{safe_keyword}"
    package_dir.mkdir(parents=True, exist_ok=True)

    # 文件路径
    filepath = package_dir / f"{platform}.md"

    # 写入 Markdown
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {keyword}\n\n")
        f.write(content)

    return filepath