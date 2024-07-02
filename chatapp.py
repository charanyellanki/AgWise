import streamlit as st

prompt = st.chat_input("Ask something")

if prompt:
    st.write(f"User asked the following: {prompt}")

    