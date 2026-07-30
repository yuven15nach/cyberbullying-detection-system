# utils/gemini_api.py
import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-3.1-flash-lite")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text 
