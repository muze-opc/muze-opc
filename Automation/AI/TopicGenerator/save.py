from pathlib import Path
from datetime import datetime


def save_markdown(keyword, content, platform):
    # 项目根目录
    root = Path(__file__).resolve().parents[3]

    # Output 文件夹
    output_dir = root / "Output" / platform
    output_dir.mkdir(parents=True, exist_ok=True)

    # 文件名
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_keyword = keyword.replace(" ", "-").replace("/", "-")
    filename = f"{today}-{safe_keyword}.md"

    filepath = output_dir / filename

    # 写入 Markdown
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {keyword}\n\n")
        f.write(content)

    return filepath