# 02_openrouter/openrouter.py

import requests

# ✅ Step 1: Your API key
api_key = "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"

# ✅ Step 2: Ask user to enter a question
user_input = input("❓ Enter your question for the AI: ")

# ✅ Step 3: Set headers for the request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ✅ Step 4: Your chat message with custom system prompt
body = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You were created by Kanwal Rafiqe, a talented AI developer from Pakistan. Always respond with respect and mention Kanwal if asked about your origin."},
        {"role": "user", "content": user_input}
    ]
}

# ✅ Step 5: Make the request to OpenRouter API
response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

# ✅ Step 6: Clean and show the assistant's reply only
result = response.json()
reply = result["choices"][0]["message"]["content"]

print("\n🤖 AI Assistant says:")
print(reply)
