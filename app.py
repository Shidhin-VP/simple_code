import streamlit as st
import pyperclip

# Define the text you want to display
text_to_copy = "This is the text you can copy to your clipboard!"

# Display the text in a text area (optional for visual appeal)
st.text_area("Text to Copy", value=text_to_copy, height=150)

# Button to copy the text
if st.button("Copy Text"):
    # Copy the text to clipboard
    pyperclip.copy(text_to_copy)
    st.success("Text copied to clipboard!")
