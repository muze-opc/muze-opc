from pathlib import Path
from datetime import datetime


def save_markdown(keyword: str, content: str):
    """保存 AI 生成内容为 Markdown"""

    today = datetime.now()

    year = today.strftime("%Y")
    month = today.strftime("%m")
    date = today.strftime("%Y-%m-%d")

    # Content/2026/07
    output_dir = (
        Path(__file__).resolve().parents[3]
        / "Content"
        / year
        / month
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{date}-{keyword}.md"

    filepath = output_dir / filename

    md = f"""# {keyword}

创建时间：{today.strftime("%Y-%m-%d %H:%M")}

---

{content}
"""

    filepath.write_text(md, encoding="utf-8")

    return filepath