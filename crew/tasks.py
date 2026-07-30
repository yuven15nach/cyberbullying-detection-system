from crewai import Task

def classification_task(text, agent):
    return Task(
        description=f"""
        Use Gemini tool to analyze:
        "{text}"

        You MUST use the tool.

        Return:
        - Bullying: Yes/No
        - Type
        - Severity
        """,
        agent=agent,
        expected_output="Bullying classification with type and severity"
    )

def risk_task(text, agent):
    return Task(
        description=f"""
        Use Gemini tool to analyze risk level:
        "{text}"

        You MUST use the tool.

        Return: Low / Medium / High
        """,
        agent=agent,
        expected_output="Risk level (Low/Medium/High)"
    )

def support_task(text, agent):
    return Task(
        description=f"""
        Provide a supportive response for:
        "{text}"

        You MUST use the tool.
        """,
        agent=agent,
        expected_output="Empathetic support message"
    )