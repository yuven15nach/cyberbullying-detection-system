# utils/gemini_api.py

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env when running locally
load_dotenv()

# Try local .env first
api_key = os.getenv("GEMINI_API_KEY")

# If not found, use Streamlit Cloud Secrets
if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.1-flash-lite")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text