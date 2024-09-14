import streamlit as st
import requests
import os

st.title("AI Email Reply Assistant")

email_body = st.text_area("Enter the email content")
tone_style = st.selectbox("Choose the tone style:", ["professional", "casual", "friendly"])

flask_port = os.getenv('FLASK_PORT')
if not flask_port:
    try:
        with open("flask_port.txt", "r") as f:
            flask_port = f.read().strip()
    except FileNotFoundError:
        st.error("Flask port not found. Make sure Flask is running.")

if st.button("Generate reply"):
    if email_body:
        data = {
            "email_body": email_body,
            "tone_style": tone_style
        }

        response = requests.post(f"http://127.0.0.1:{flask_port}/generate-reply", json=data)

        if response.status_code == 200:
            result = response.json()
            st.subheader("Generated reply:")
            st.write(result['reply'])
        else:
            st.error("Error in generating reply, please try again")
    else:
        st.warning("Please enter email content.")




