import random
import streamlit as st

# Streamlit UI Styling
st.set_page_config(page_title="Rock Paper Scissor", page_icon="🎮", layout="centered")

# Custom CSS for background
background_css = """
<style>
   .stApp {
        background-color: #ffe29c;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)


# Custom CSS for Stylish UI
st.markdown("""
    <style>
        .stButton>button {
            font-size: 18px !important;
            padding: 12px !important;
            border-radius: 10px !important;
            font-weight: bold !important;
            width: 100% !important;
            background-color: #4CAF50 !important;
            color: white !important;
        }
        .stButton>button:hover {
            background-color: #ff5733 !important;
        }
        .title {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #ff5733;
        }
        .result-box {
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 🎮 Game Title
st.markdown("<h1 class='title'>🪨 Rock - 📄 Paper - ✂️ Scissors</h1>", unsafe_allow_html=True)
st.markdown("### Play against the computer and test your luck! 💡")

# 🎯 Initialize Score
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

# 🏆 Scoreboard
st.markdown(f"""
    <div style="text-align: center; font-size: 20px; font-weight: bold;">
        👤 You: {st.session_state.user_score}  |  💻 Computer: {st.session_state.computer_score}
    </div>
""", unsafe_allow_html=True)

# Choices
choices = ["Rock", "Paper", "Scissors"]
icons = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# 🎮 User Input (Buttons)
st.markdown("### Choose Your Move:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Rock"):
        user_choice = "Rock"
with col2:
    if st.button("📄 Paper"):
        user_choice = "Paper"
with col3:
    if st.button("✂️ Scissors"):
        user_choice = "Scissors"

# 🚀 Game Logic
if "user_choice" in locals():
    computer_choice = random.choice(choices)

    # 🆚 Show Choices
    st.subheader("📢 Results")
    st.markdown(f"**👤 You choose:** {icons[user_choice]} {user_choice}")
    st.markdown(f"**💻 Computer choose:** {icons[computer_choice]} {computer_choice}")

    # 🏆 Determine Winner
    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        color = "#3498db"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You Win!"
        color = "#2ecc71"
        st.session_state.user_score += 1  # Increase user score
    else:
        result = "💻 Computer Wins!"
        color = "#e74c3c"
        st.session_state.computer_score += 1  # Increase AI score

    # 🎉 Display Result
    st.markdown(f"<div class='result-box' style='background-color: {color}; color: white;'>{result}</div>", unsafe_allow_html=True)

    # 🔄 Play Again Button
    if st.button("🔄 Play Again"):
        st.experimental_rerun()