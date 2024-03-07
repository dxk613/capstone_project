import pickle
import streamlit as st

st.title("Is this young person likely to face homelessness more than 1 year?")

your_text = st.text_input("Please enter some text: ", max_chars = 500)

st.write(your_text)