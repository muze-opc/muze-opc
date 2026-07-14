from pathlib import Path
from dotenv import load_dotenv
import os

# 加载项目根目录 .env
env_path = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL = os.getenv("LLM_MODEL")

print("API_KEY 是否读取成功：", API_KEY is not None)
print("BASE_URL：", BASE_URL)
print("MODEL：", MODEL)