import streamlit as st
import pyperclip

# Define the text you want to display
text_to_copy = """dc23aa0f2333267cda6be7965f67814c 

or can just copy the key by copying and pasting normally as we do"""

# Display the text in a text area (optional for visual appeal)
st.text_area("Text to Copy", value=text_to_copy, height=150)

# Button to copy the text
if st.button("Copy Text"):
    # Copy the text to clipboard
    pyperclip.copy(text_to_copy)
    st.success("Text copied to clipboard!")
