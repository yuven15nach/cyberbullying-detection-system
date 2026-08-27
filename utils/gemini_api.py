import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.1-flash-lite")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text