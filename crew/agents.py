from crewai import Agent
from crew.tools import gemini_tool

bullying_classifier = Agent(
    role="Cyberbullying Detection Expert",
    goal="Detect cyberbullying",
    backstory="Expert in harmful language detection",
    tools=[gemini_tool],
    verbose=True,
    
)

risk_agent = Agent(
    role="Risk Detection Specialist",
    goal="Detect risk level",
    backstory="Expert in identifying threats",
    tools=[gemini_tool],
    verbose=True,
    
)

safety_coach = Agent(
    role="Emotional Support Assistant",
    goal="Provide emotional support",
    backstory="Expert in mental well-being",
    tools=[gemini_tool],
    verbose=True,
    
)