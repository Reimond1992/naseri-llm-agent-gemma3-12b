import httpx
import uuid
import time
from core.config import settings

def generate_ids(user_id=None, session_id=None):
    return (
        user_id or f"user_{uuid.uuid4().hex[:6]}",
        session_id or f"session_{uuid.uuid4().hex[:6]}"
    )

class OllamaAgent:
    async def analyze(self, message: str) -> str:
        return f"سؤال کاربر را تحلیل کن و پاسخ مناسب بده:\n{message}"

    async def generate(self, analysis: str) -> str:
        url = settings.LLM_URL
        payload = {
            "model": "gemma3:12b",
            "prompt": f"""
تو یک دستیار هوش مصنوعی هستی.

قوانین:
- فقط به زبان فارسی پاسخ بده
- از کلمات انگلیسی استفاده نکن
- توضیح مراحل فکری یا تحلیل را ننویس
- فقط پاسخ نهایی را برگردان
سؤال:
{analysis}
""",
            "stream": False
        }
        try:
            async with httpx.AsyncClient(timeout=settings.TIMEOUT) as client:
                res = await client.post(url, json=payload)
                res.raise_for_status()
                data = res.json()
                return data.get("response", "پاسخی دریافت نشد")
        except Exception as e:
            return f"خطا در اتصال به LLM: {str(e)}"

    async def tone_tool(self, text: str, tone: str = "friendly") -> str:
        if tone == "friendly":
            return f"😊 {text}"
        return text

    async def run(self, message: str) -> str:
        analysis = await self.analyze(message)
        response = await self.generate(analysis)
        response = await self.tone_tool(response, tone="friendly")
        return response
