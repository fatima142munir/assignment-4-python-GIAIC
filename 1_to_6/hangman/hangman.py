import random
import string
import streamlit as st
from words import words

# get a valid word from the words.py file
def get_valid_word(words):
    word = random.choice(words)
    print(word)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

# Hangman stages (visuals)
hangman_stages = [
    "😵💀",  # Game over
    "😰 O\n  /|\\\n  / \\",
    "😨 O\n  /|\\\n  /",
    "😧 O\n  /|\\",
    "😕 O\n  /|",
    "😐 O\n  /",
    "🙂 O",
]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = get_valid_word(words)
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.alphabet = set(string.ascii_uppercase)
    st.session_state.used_letters = set()
    st.session_state.lives = 6

# Title & Styling
st.markdown("<h1 style='text-align: center; color: #ff5733;'>🔥 Hangman Game 🎮</h1>", unsafe_allow_html=True)
st.write("🎯 Guess the word one letter at a time!")

# Show Hangman stage
st.subheader("Your Hangman:")
st.write(f"```\n{hangman_stages[st.session_state.lives]}\n```")

# Display used letters and lives
col1, col2 = st.columns(2)
with col1:
    st.write(f"💡 **Used Letters:** {' '.join(st.session_state.used_letters) if st.session_state.used_letters else 'None'}")
with col2:
    st.write(f"❤️ **Lives Left:** {st.session_state.lives}")

# Show current word progress
word_display = [letter if letter in st.session_state.used_letters else "_" for letter in st.session_state.word]
st.subheader("🔤 Word Progress:")
st.markdown(f"<h2>{' '.join(word_display)}</h2>", unsafe_allow_html=True)

# User input
user_input = st.text_input("🎯 Guess a letter:", max_chars=1).upper()

if st.button("✅ Submit Guess") and user_input:
    if user_input in st.session_state.alphabet - st.session_state.used_letters:
        st.session_state.used_letters.add(user_input)
        if user_input in st.session_state.word_letters:
            st.session_state.word_letters.remove(user_input)
            st.success(f"🎉 Correct! {user_input} is in the word!")
        else:
            st.session_state.lives -= 1
            st.warning(f"❌ Wrong guess! {user_input} is not in the word.")
    elif user_input in st.session_state.used_letters:
        st.warning("⚠️ You already guessed that letter!")
    else:
        st.error("🚫 Invalid input! Please enter a single letter.")

# Game result
if st.session_state.lives == 0:
    st.error(f"💀 Game Over! The word was **{st.session_state.word}**")
    if st.button("🔄 Play Again"):
        st.session_state.clear()
        st.experimental_rerun()
elif len(st.session_state.word_letters) == 0:
    st.success(f"🏆 Congratulations! You guessed the word **{st.session_state.word}** 🎉")
    if st.button("🔄 Play Again"):
        st.session_state.clear()
        st.experimental_rerun()