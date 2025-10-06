import streamlit as st
import pyperclip

text_to_copy = """dc23aa0f2333267cda6be7965f67814c 

or just copy the key by copying and pasting normally as we do The button has some issues. :)"""

st.text_area("Text to Copy", value=text_to_copy, height=150)

if st.button("Copy Text"):
    pyperclip.copy(text_to_copy)
    st.success("Text copied to clipboard!")
