import streamlit as st
from crew.crew_setup import run_crew

st.set_page_config(
    page_title="AI Cyberbullying Detection Self-Help Tool",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI Cyberbullying Detection & Support Tool")

st.caption(
    "A  multi-stage LLM Crew-AI inspired system for cyberbullying analysis"
)

st.info(
    "This system analyzes text for possible cyberbullying indicators, severity, risk level, "
    "and provides supportive guidance. It is intended as a self-help tool for the users not a replacement "
    "for professional counselling or emergency support."
)

with st.sidebar:
    st.header("System Overview")

    st.markdown(
        """
        **Architecture**
        1. User enters a text message  
        2. Classification module detects bullying type  
        3. Risk module assesses risk level  
        4. Support module generates guidance  

        **Model**
        - Gemini-based LLM
        - CrewAI-inspired modular pipeline
        """
    )

    st.divider()

    if st.button("Clear Analysis History"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("Message Analysis")

st.markdown(
    """
    Enter a message below to analyze whether it may contain cyberbullying content.
    """
)

prompt = st.chat_input("Enter a message to analyze...")

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing message using Gemini model..."):
            response = run_crew(prompt)

        st.success("Analysis completed")
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

if st.session_state.messages:
    with st.expander("View Previous Analyses"):
        for message in st.session_state.messages:
            role = "User Input" if message["role"] == "user" else "System Analysis"
            st.markdown(f"**{role}:**")
            st.markdown(message["content"])
            st.divider()