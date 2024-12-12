import streamlit as st
from datetime import datetime
import time

# Set the title of the app
st.title("🎅 Santa Claus Christmas Countdown 🎄")

# Display a festive greeting
st.header("Welcome to the Christmas Wonderland with Santa Claus!")

# Display a picture of Santa Claus
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fsanta-claus&psig=AOvVaw36HqBXvxOsy4Jsrnw5p7K2&ust=1734080990647000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCIDW5Z7xoYoDFQAAAAAdAAAAABAE", width=400)

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

# Display the countdown
st.subheader(f"🎅 Only {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes, and {seconds_remaining} seconds left until Christmas!")

# Show a fun fact about Santa Claus
st.markdown("""
### 🎁 Fun Fact about Santa Claus:
Did you know that Santa Claus' red suit was popularized by Coca-Cola in the 1930s? Before that, Santa's outfit was depicted in a variety of colors!
""")

# Give an option for users to send a Christmas wish to Santa
user_message = st.text_input("🎄 Write your Christmas wish to Santa:")

if user_message:
    st.write(f"🎅 Santa says: '{user_message}' has been added to the nice list!")

# Button to show a Christmas greeting
if st.button("Get Christmas Cheer 🎅"):
    st.balloons()  # Display virtual balloons for some extra festive fun
    st.success("🎄 Merry Christmas! 🎅 Wishing you all the joy and warmth this holiday season! 🎁")
    time.sleep(1)  # Adding a brief delay for the effect

# Display a footer message
st.markdown("---")
st.markdown("Created with ❤️ for the holiday season by [Your Name]")

