from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================
# 项目目录
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

TOPIC_GENERATOR_DIR = Path(__file__).parent

OUTPUT_DIR = PROJECT_ROOT / "Output"

PROMPTS_DIR = TOPIC_GENERATOR_DIR / "Prompts"

STYLE_FILE = TOPIC_GENERATOR_DIR / "styles.json"

PLATFORM_FILE = TOPIC_GENERATOR_DIR / "platforms.json"

DEFAULT_PROMPT = PROMPTS_DIR / "default.txt"

# ==========================
# 加载 .env
# ==========================

env_path = PROJECT_ROOT / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL = os.getenv("LLM_MODEL", "gpt-5.5")

# ==========================
# 调试
# ==========================

DEBUG = True

if DEBUG:
    print("API_KEY 是否读取成功：", API_KEY is not None)
    print("BASE_URL：", BASE_URL)
    print("MODEL：", MODEL)