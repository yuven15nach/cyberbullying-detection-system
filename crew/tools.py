from crewai.tools import tool
from utils.gemini_api import ask_gemini

@tool("Gemini AI Tool")
def gemini_tool(prompt: str) -> str:
    """Use Gemini AI to analyze text and generate responses"""
    return ask_gemini(prompt) 