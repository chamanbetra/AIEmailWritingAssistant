import streamlit as st
import requests
from get_flask_port import get_flask_port

st.title("AI Email Reply Assistant")

email_body = st.text_area("Enter the email content", height=300)
tone_style = st.selectbox("Choose the tone style:", ["professional", "casual", "friendly"])
flask_port = get_flask_port()

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




