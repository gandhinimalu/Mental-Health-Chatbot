import streamlit as st  
import time  
import openai  
import streamlit.components.v1 as components  

# Set page config
st.set_page_config(page_title="MindEase", page_icon="🌿", layout="wide")

# Custom background styling
st.markdown("""
    <style>
        body {
            background-image: url('https://source.unsplash.com/1600x900/?nature,mindfulness');
            background-size: cover;
        }
        .big-font {
            font-size:18px !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("🧠 MindEase Tools")  
menu = st.sidebar.radio("Select a feature:", ["Daily Affirmation", "Study Timer", "Anxiety Relief", "Study Tips", "Self-care Tips", "Chatbot"])

# ------------------- Daily Affirmation -------------------
if menu == "Daily Affirmation":
    st.title("✨ Daily Affirmation")  
    st.write("Keep going. Everything you need will come to you at the perfect time.")
    if st.button("💡 Inspire Me!"):
        st.success("You are stronger than you think. Believe in yourself!")

# ------------------- Study Timer -------------------
elif menu == "Study Timer":
    st.title("⏳ Study Timer")  
    study_time = st.slider("Set study duration (minutes):", 5, 180, 25)  
    break_time = st.slider("Break duration (minutes):", 1, 60, 5)  
    if st.button("Start Timer"):  
        my_bar = st.progress(0)
        for i in range(100):
            time.sleep(study_time / 100)
            my_bar.progress(i + 1)
        st.success("Time’s up! Take a break 🎉")

# ------------------- Anxiety Relief -------------------
elif menu == "Anxiety Relief":
    st.title("😌 Anxiety Relief")
    st.write("Close your eyes and focus on your breath. Here's a guided meditation:")
    st.video("https://www.youtube.com/watch?v=inpok4MKVLM")  # Meditation video

# ------------------- Study Tips -------------------
elif menu == "Study Tips":
    st.title("📚 Study Tips")
    tips = [
        "1️⃣ Use the Pomodoro technique ⏳",
        "2️⃣ Take handwritten notes ✍️",
        "3️⃣ Test yourself regularly ✅",
        "4️⃣ Stay organized with a planner 📅",
        "5️⃣ Avoid multitasking ❌"
    ]
    for tip in tips:
        st.write(tip)

# ------------------- Self-care Tips -------------------
elif menu == "Self-care Tips":
    st.title("🌿 Self-care Tips")
    tips = [
        "💧 Stay hydrated",
        "😴 Get enough sleep",
        "🧘 Take deep breaths",
        "📵 Limit screen time",
        "🍎 Eat healthy meals"
    ]
    for tip in tips:
        st.write(tip)

# ------------------- Chatbot -------------------
elif menu == "Chatbot":
    st.title("🗣️ Chat with MindEase AI")  
    user_input = st.text_input("How are you feeling today?")  
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("🤖", response["choices"][0]["message"]["content"])

# ------------------- Breathing Exercise Animation -------------------
st.markdown("### 🧘 Guided Breathing Exercise")  
st.markdown("Inhale for 4 seconds, hold for 4, exhale for 4. Repeat.")  
components.html("""
    <style>
        @keyframes breathe {
            0% { transform: scale(1); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }
        .circle {
            width: 100px;
            height: 100px;
            background-color: #4CAF50;
            border-radius: 50%;
            animation: breathe 4s infinite;
        }
    </style>
    <div class="circle"></div>
""")
