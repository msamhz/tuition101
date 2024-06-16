import gradio as gr
import requests
from urllib.parse import urlparse
import socket


def call_index():
    response = requests.get('http://app:5000/')
    if response.status_code == 200:
        return response.json()['message']
    else:
        return "Error: Unable to reach the API."
    
    
def get_greeting(name):
    """Function to call the Flask API and get a greeting."""
    url = f'http://app:5000/api/greet/{name}'
    response = requests.get(url)
    
    parsed_url = urlparse(response.request.url)
    port = parsed_url.port
    
    request_details = (
        f"Request URL: {response.request.url}\n"
        f"Request Headers: {response.request.headers}\n"
        f"Request Body: {response.request.body}\n"
        f"URLPARSED arguments: {parsed_url}\n"
        f"Request Port: {port}\n"
        f"Gradio host name: {socket.gethostname()}/n"
        f"\n"
    )
    
    if response.status_code == 200:
        response_details = (
            f"Response Headers: {response.headers}\n"
            f"Response Content: {response.json()}\n"
            f"Response Index: {call_index()}\n"
        )
        greeting = response.json()['message']
    else:
        response_details = f"Error Response: {response.text}\n"
        greeting = 'Error contacting backend'
    
    details = request_details + response_details
    return greeting, details

interface = gr.Interface(
    fn=get_greeting,
    inputs="textbox",
    outputs=["textbox", "textarea"],  # Returning two outputs: greeting and details
    title="Greeting Interface",
    description="Enter your name to receive a greeting from the backend.",
    analytics_enabled=False
)

if __name__ == "__main__":
    interface.launch(server_name="web", server_port=7860, share=False)
