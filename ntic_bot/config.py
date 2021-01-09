import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
env_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(env_file):
    load_dotenv(env_file)

bot_token = os.getenv('TOKEN')
announcement_channel = "announcement📢"
