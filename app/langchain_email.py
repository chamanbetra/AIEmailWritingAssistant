from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
# from langchain.chains import SimpleChain
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=openai_key, model="gpt-4")

def analyze_email(email_body):
    prompt = f"Analyze this email and summarize its key points: {email_body}"
    response = llm([HumanMessage(content=prompt)])
    return response.content

def detect_tone(email_body):
    prompt = f"Detect the tone of this email: {email_body}"
    response = llm([HumanMessage(content=prompt)])
    return response.content

def generate_reply(summary, tone, style="professional"):
    prompt = f"Write a {style} reply based on the following summary: {summary}.\nTone: {tone}."
    response = llm([HumanMessage(content=prompt)])
    return response.content
