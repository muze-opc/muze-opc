from platforms import choose_platforms
from styles import choose_style
from generator import generate_content

from logger import success, info
from utils import divider

# 输入关键词
keyword = input("请输入今天的视频关键词：").strip()

# 选择风格
style = choose_style()

# 选择平台
platforms = choose_platforms()

saved_files = []

# 批量生成
for platform in platforms:

    filepath = generate_content(
        keyword,
        style,
        platform
    )

    saved_files.append(filepath)

divider()

success("全部平台生成完成")

for path in saved_files:
    info(path)

divider()