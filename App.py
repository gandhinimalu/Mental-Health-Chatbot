import streamlit as st
import openai
import time
import os

# Load API Key from Streamlit Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# App Title
st.set_page_config(page_title="MindEase AI", layout="wide")

# Sidebar Navigation
st.sidebar.title("🧠 MindEase Tools")
option = st.sidebar.radio("Select a feature:", ["Daily Affirmation", "Study Timer", "Anxiety Relief", "Study Tips", "Self-care Tips", "Chatbot"])

# ✨ Daily Affirmation
if option == "Daily Affirmation":
    st.title("🌟 Daily Affirmation")
    st.write("Keep going. Everything you need will come to you at the perfect time.")
    
# ⏳ Study Timer
elif option == "Study Timer":
    st.title("⏳ Study Timer")
    study_time = st.number_input("Set your study duration (minutes):", min_value=1, max_value=120, value=25)
    break_time = st.number_input("Break duration:", min_value=1, max_value=60, value=5)
    
    if st.button("Start Timer"):
        with st.spinner(f"Studying for {study_time} minutes..."):
            time.sleep(study_time * 60)
        st.success(f"Time for a {break_time}-minute break! 🎉")

# 😌 Anxiety Relief
elif option == "Anxiety Relief":
    st.title("😌 Anxiety Relief")
    st.write("Close your eyes and picture your happy place. Stay there for a moment.")
    st.button("Take a Deep Breath")

# 📚 Study Tips
elif option == "Study Tips":
    st.title("📚 Study Tips")
    st.write("Tip: Use the Pomodoro technique—study for 25 minutes, then take a 5-minute break.")

# 🌿 Self-care Tips
elif option == "Self-care Tips":
    st.title("🌿 Self-care Tips")
    st.write("Remember to stay hydrated and take regular breaks.")

# 🤖 AI Chatbot
elif option == "Chatbot":
    st.title("🗣️ Chat with MindEase AI")
    
    user_input = st.text_input("How are you feeling today?")
    
    if st.button("Send"):
        if user_input:
            with st.spinner("Thinking... 🤔"):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": user_input}]
                    )
                    st.success("AI Response:")
                    st.write(response["choices"][0]["message"]["content"])
                except Exception as e:
                    st.error("Error fetching response. Check API key or try again later.")

