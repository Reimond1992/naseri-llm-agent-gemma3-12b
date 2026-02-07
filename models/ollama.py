import uuid
import time
from datetime import datetime
import httpx
from core.config import settings
from core.logger import logger

class OllamaAgent:
    def __init__(self):
        self.url = settings.LLM_URL
        self.timeout = settings.TIMEOUT

    async def analyze(self, message: str) -> str:
        return f"سؤال کاربر را تحلیل کن و پاسخ مناسب بده:\n{message}"

    async def generate(self, analysis: str) -> str:
        payload = {
            "model": "gemma3:12b",
            "prompt": f"""
تو یک دستیار هوش مصنوعی هستی.

قوانین:
- فقط به زبان فارسی پاسخ بده
- از کلمات انگلیسی استفاده نکن
- فقط پاسخ نهایی را برگردان
سؤال:
{analysis}
""",
            "stream": False
        }
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                res = await client.post(self.url, json=payload)
                res.raise_for_status()
                data = res.json()
                return data.get("response", "پاسخی دریافت نشد")
        except Exception as e:
            logger.error(f"خطا در LLM: {e}")
            return f"خطا در LLM: {str(e)}"

    async def run(self, message: str) -> str:
        analysis = await self.analyze(message)
        return await self.generate(analysis)

def generate_ids(user_id=None, session_id=None):
    return (
        user_id or f"user_{uuid.uuid4().hex[:6]}",
        session_id or f"session_{uuid.uuid4().hex[:6]}"
    )
