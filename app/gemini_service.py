from google import genai
from app.config import GEMINI_API_KEY
import time

client = genai.Client(api_key=GEMINI_API_KEY)


async def generate_reply(conversation_context: str) -> str:
    prompt = f"""
You are a helpful WhatsApp business assistant.
Do not imply real-time system access.
Avoid saying "checking availability" or "one moment".

Continue the conversation naturally.

Conversation:
{conversation_context}

Assistant:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text.strip()

    except Exception as e:
        print("Gemini error:", e)

        # fallback response
        return "Thanks for your message! We will get back to you shortly."
