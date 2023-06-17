from dotenv import load_dotenv
import requests
import os

load_dotenv()


class Telegram:
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")
        self.admin_tg_user_id = os.getenv("ADMIN_USER_ID")

    def send_tg_message(self, text: str):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": "213337828",
            "text": text
        }

        return requests.post(url=url, data=data).status_code
