import time
import streamlit as st

# Set page config for better UI
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-font { font-size: 32px; font-weight: bold; text-align: center; color: #FF4500; }
        .timer-text { font-size: 24px; font-weight: bold; text-align: center; color: #008000; }
        .stButton>button { background-color: skyblue; color: white; font-size: 20px; border-radius: 15px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# App title and header
st.title("⏰ Stylish Countdown Timer")
st.header("⏳ Stay Tuned for the Countdown!")

# Get user input
seconds = int(st.number_input("🔢 Enter the countdown time (in seconds):", min_value=1, step=1))

# Start button
if st.button("🚀 Start Countdown"):
    countdown_placeholder = st.empty()  # Placeholder for countdown display
    progress_bar = st.progress(0)  # progressbar initialization

    for countdown in range(seconds, 0, -1):
        countdown_placeholder.markdown(f'<p class="timer-text">⏳ {countdown} seconds remaining</p>',
                                       unsafe_allow_html=True)
        progress_bar.progress((seconds - countdown) / seconds)  # Update progress bar
        time.sleep(1)

    progress_bar.progress(1.0)  # Ensure that progress  bar is completely full at the end

    # Display "Time's Up" message
    countdown_placeholder.markdown('<p class="big-font">🎉 Time’s Up! 🎊</p>', unsafe_allow_html=True)

    # 🎈 Balloons effect
    st.balloons()