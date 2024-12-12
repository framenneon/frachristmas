import streamlit as st
from datetime import datetime
from gtts import gTTS
import os
import time

# Set the title of the app
st.title("🎅 Santa Claus Christmas Countdown 🎄")

# Display a festive greeting
st.header("Welcome to the Christmas Wonderland with Santa Claus!")

# Display a picture of Santa Claus
st.image("https://play-lh.googleusercontent.com/U6hu7q67BaibfGfG2WtJxr0e8WC-xMBqbH_FTJpOR-sSaGGQiEVuKxvvRslmn9uozSU", width=400)

# Language selection (English or Italian)
language = st.selectbox("Choose your language", ["English", "Italian"])

# Countdown messages for English and Italian
if language == "English":
    countdown_message = "🎅 Only {} days, {} hours, {} minutes, and {} seconds left until Christmas!".format(
        "{days_remaining}", "{hours_remaining}", "{minutes_remaining}", "{seconds_remaining}")
elif language == "Italian":
    countdown_message = "🎅 Manca solo {} giorni, {} ore, {} minuti e {} secondi a Natale!".format(
        "{days_remaining}", "{hours_remaining}", "{minutes_remaining}", "{seconds_remaining}")

# Countdown to Christmas (December 25th)
today = datetime.today()
christmas = datetime(today.year, 12, 25)

# If Christmas has already passed this year, set the countdown for next year
if today > christmas:
    christmas = datetime(today.year + 1, 12, 25)

# Calculate time remaining until Christmas
time_remaining = christmas - today
days_remaining = time_remaining.days
hours_remaining = time_remaining.seconds // 3600
minutes_remaining = (time_remaining.seconds // 60) % 60
seconds_remaining = time_remaining.seconds % 60

# Format the countdown message
countdown_message = countdown_message.format(
    days_remaining=days_remaining,
    hours_remaining=hours_remaining,
    minutes_remaining=minutes_remaining,
    seconds_remaining=seconds_remaining
)

# Display the countdown message
st.subheader(countdown_message)

# Generate audio of the countdown message using Google Text-to-Speech (gTTS)
if language == "English":
    tts = gTTS(countdown_message, lang='en')
elif language == "Italian":
    tts = gTTS(countdown_message, lang='it')

# Save the audio to a file
audio_file_path = "countdown.mp3"
tts.save(audio_file_path)

# Play the generated audio using Streamlit's audio player
st.audio(audio_file_path)

# Show a fun fact about Santa Claus in the selected language
if language == "English":
    st.markdown("""
    ### 🎁 Fun Fact about Santa Claus:
    Did you know that Santa Claus' red suit was popularized by Coca-Cola in the 1930s? Before that, Santa's outfit was depicted in a variety of colors!
    """)
elif language == "Italian":
    st.markdown("""
    ### 🎁 Curiosità su Babbo Natale:
    Sapevi che il vestito rosso di Babbo Natale è stato reso popolare dalla Coca-Cola negli anni '30? Prima di allora, l'outfit di Babbo Natale era raffigurato in vari colori!
    """)

# Give an option for users to send a Christmas wish to Santa
user_message = st.text_input("🎄 Write your Christmas wish to Santa:")

if user_message:
    if language == "English":
        st.write(f"🎅 Santa says: '{user_message}' has been added to the nice list!")
    elif language == "Italian":
        st.write(f"🎅 Babbo Natale dice: '{user_message}' è stato aggiunto alla lista dei buoni!")

# Button to show a Christmas greeting
if st.button("Get Christmas Cheer 🎅"):
    st.balloons()  # Display virtual balloons for some extra festive fun
    if language == "English":
        st.success("🎄 Merry Christmas! 🎅 Wishing you all the joy and warmth this holiday season! 🎁")
    elif language == "Italian":
        st.success("🎄 Buon Natale! 🎅 Ti auguro tutta la gioia e il calore di questa stagione natalizia! 🎁")
    time.sleep(1)  # Adding a brief delay for the effect

# Display a footer message in the selected language
st.markdown("---")
if language == "English":
    st.markdown("Created with ❤️ for the holiday season by Francesco")
elif language == "Italian":
    st.markdown("Creato con ❤️ per la stagione delle festività da Francesco")

# Clean up the generated audio file after it's used
os.remove(audio_file_path)
