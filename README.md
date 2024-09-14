# AI-Powered Email Writing Assistant

## Overview
This project is an AI-powered email writing assistant designed to help generate contextually appropriate replies to emails. The assistant leverages LangChain, OpenAI's GPT, and Python to analyze incoming emails, detect tone and key points, and generate professional, casual, or custom-styled responses. The application is fully containerized using Docker, allowing for easy deployment across different environments.

## Features
- **Email Analysis**: Analyzes incoming emails to extract key points and summarize the content.
- **Tone Detection**: Detects the tone of the received email (e.g., casual, formal) to craft an appropriate reply.
- **Customizable Reply Style**: Allows users to specify the tone of the reply, such as casual, formal, or professional.
- **Context-Aware Responses**: Generates coherent and contextually accurate replies based on the email’s content and tone.
- **Dockerized Application**: Easily deployable as a containerized application with Docker, making it platform-agnostic.
- **API-First Approach**: Exposes the application through a REST API for easy integration with any front-end or email platform.

## Tech Stack
- **LangChain**: Builds a multi-step processing pipeline to handle email understanding, tone detection, and reply generation.
- **OpenAI API**: Powers the natural language processing and reply generation using state-of-the-art GPT models.
- **Flask**: A lightweight Python framework to build the backend REST API for handling email input and response generation.
- **Streamlit**: A powerful, fast, and easy-to-use frontend framework for creating interactive web applications to display the assistant’s email reply features in a user-friendly interface.
- **Docker**: Containerizes the entire application to ensure consistent behavior across different deployment environments.

## How It Works
1. **Input Email**: Users send an incoming email body via the API or through the Streamlit-based frontend.
2. **Key Points Extraction**: The assistant uses LangChain and GPT to summarize the key points from the email.
3. **Tone Detection**: Detects the tone of the email (e.g., casual, formal, etc.).
4. **Reply Generation**: Based on the summary and detected tone, the assistant generates a contextually relevant reply.
5. **Reply Customization**: Users can specify the desired reply tone (e.g., formal, professional, casual).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chamanbetra/AIEmailWritingAssistant.git
    cd AIEmailWritingAssistant/app
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your OpenAI API key:
    ```bash
    OPENAI_API_KEY=your-openai-api-key
    ```

4. Run the app (there is a script to run both frontend and backend at once):
    ```bash
    python run_app.py
    ```

### (Optional) Docker Setup:

1. Build the Docker image:
    ```bash
    docker build -t ai-email-reply-assistant .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 5000:5000 --env-file .env ai-email-reply-assistant
    ```

## API Endpoints

### POST `/generate-reply`
Accepts the body of an email and generates a context-aware reply.

**Request Body**:
```json
{
  "email_body": "Your email content here",
  "tone_style": "professional"
}

**Response**:
```json
{
  "summary": "Summary of the email",
  "tone": "Detected tone",
  "reply": "Generated reply based on the content"
}

## Future Enhancements

- **Multi-language Support**: Add support for generating replies in multiple languages to accommodate a broader range of users.
- **Integration with Email Clients**: Seamless integration with popular email platforms like Gmail and Outlook to enable automatic reply generation directly within these clients.
- **Smart Follow-ups**: Include suggestions for follow-up actions, such as scheduling meetings or setting reminders, based on the content of the incoming email.
- **Email Thread Handling**: Improve the ability to understand and respond to longer email threads with multiple participants, ensuring contextually relevant responses for all.
- **Personalization**: Allow users to save and personalize common response templates and signatures for faster email handling.
