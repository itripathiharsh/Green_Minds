# import requests

# # 🔑 Paste your key here
# # GEMINI_API_KEY = "AIzaSyCA-gS0PxpuHp-bz-RHpO8CCB_SphU72MQ"

# import google.generativeai as genai

# genai.configure(api_key="AIzaSyCA-gS0PxpuHp-bz-RHpO8CCB_SphU72MQ")

# model = gemini-2.5-flash

# test_gemini.py
import requests

# 🔑 Replace with your actual API key
GEMINI_API_KEY =  "AIzaSyCA-gS0PxpuHp-bz-RHpO8CCB_SphU72MQ"

# ✅ Correct model name for v1beta
MODEL_NAME = "models/gemini-2.5-flash"

# ✅ Correct endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_NAME}:generateContent?key={GEMINI_API_KEY}"

# 📦 Payload
payload = {
    "contents": [
        {
            "parts": [
                {"text": "Say 'Hello from Green Minds!' in one sentence."}
            ]
        }
    ]
}

print("📡 Sending request to Gemini API...")
try:
    response = requests.post(url, json=payload, timeout=20)
    print(f"✅ Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        print(f"💬 Response: {text.strip()}")
        print("\n🎉 SUCCESS! Your API key works.")
    else:
        print(f"❌ Error: {response.json()}")

except Exception as e:
    print(f"💥 Exception: {e}")
