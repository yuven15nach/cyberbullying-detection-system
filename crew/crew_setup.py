from utils.gemini_api import ask_gemini

def run_crew(text):

    # Agent 1: Classification Agent 
    classification = ask_gemini(f"""
    Analyze this message:
    "{text}"

    Return:
    Bullying: Yes/No
    Type: (not_cyberbullying, gender, religion, age, ethnicity, or other_cyberbullying)
    Severity: (Low, Medium, High)
    """)

    # Agent 2: Risk agent 
    risk = ask_gemini(f"""
    Analyze risk level for:
    "{text}"

    Return: Low / Medium / High
    """)

    # Agent 3: Safety_coach Support Agent
    support = ask_gemini(f"""
    Provide a supportive response for:
    "{text}"
    """)

    # Combine results 
    final_output = f"""
    🔍 Classification:
    {classification}

    ⚠️ Risk Level:
    {risk}

    💬 Support Response:
    {support}
    """

    return final_output




