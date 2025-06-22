from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
from openai import AsyncOpenAI

# === CONFIGURATION ===
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSy..."  # replace with your actual Gemini API key
MODEL_NAME = "gemini-2.0-flash"

# Validate key
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set!")

# Initialize OpenAI-compatible Gemini client
client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)

# === ASYNC FUNCTION ===
async def main():
    response = await client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": "What is LiteLLM?"}
        ]
    )

    print("\n🧠 Gemini Response:\n")
    print(response.choices[0].message.content)

# === ENTRY POINT ===
if __name__ == "__main__":
    asyncio.run(main())
