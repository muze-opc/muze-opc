from prompts import build_prompt
from platforms import get_platform_prompt
from llm import chat
from save import save_markdown

from logger import info, success
from utils import divider


def generate_content(keyword, style, platform):
    """
    生成一个平台内容并保存 Markdown
    """

    divider()

    info(f"开始生成平台：{platform}")

    # 获取平台 Prompt
    platform_prompt = get_platform_prompt(platform)

    # 构建 Prompt
    prompt = build_prompt(
        keyword,
        style,
        platform_prompt
    )

    info(f"Prompt长度：{len(prompt)}")

    divider()

    # 调用 GPT
    result = chat(prompt)

    success("GPT 内容生成完成")

    # 保存 Markdown
    filepath = save_markdown(
        keyword,
        result,
        platform
    )

    success(f"已保存：{filepath}")

    divider()

    return filepath