import gradio as gr
import requests
import ollama  # For local LLaMA/Mistral models

# Choose AI Model (Ollama for local, OpenAI for cloud)
USE_OLLAMA = True  # Change to False if using OpenAI API

# OpenAI API (if not using Ollama)
OPENAI_API_KEY = "your-api-key"
OPENAI_MODEL = "gpt-3.5-turbo"

def chat_with_ai(message, history):
    """Handles chat responses using Ollama or OpenAI API."""
    if USE_OLLAMA:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": message}])
        return response["message"]["content"]
    else:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
        data = {
            "model": OPENAI_MODEL,
            "messages": [{"role": "system", "content": "You are a helpful assistant."}] + 
                       [{"role": "user", "content": message}]
        }
        response = requests.post(url, json=data, headers=headers)
        return response.json()["choices"][0]["message"]["content"]

# Gradio UI
chat_ui = gr.ChatInterface(chat_with_ai)

# Launch the UI
if __name__ == "__main__":
    chat_ui.launch()
