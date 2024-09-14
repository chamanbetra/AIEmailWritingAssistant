from langchain_community.llms import OpenAI
# from langchain.chains import SimpleChain
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_key)

def analyze_email(email_body):
    prompt = f"Analyze this email and summarize its key points: {email_body}"
    return llm(prompt)

def detect_tone(email_body):
    prompt = f"Detect the tone of this email: {email_body}"
    return llm(prompt)

def generate_reply(summary, tone, style="professional"):
    prompt = f"Write a {style} reply based on the following summary: {summary}.\nTone: {tone}."
    return llm(prompt)
