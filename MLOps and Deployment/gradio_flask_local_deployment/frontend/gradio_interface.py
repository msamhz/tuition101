import gradio as gr
import requests

def get_greeting(name):
    """Function to call the Flask API and get a greeting."""
    url = f'http://app:5000/api/greet/{name}'
    response = requests.get(url)
    
    request_details = (
        f"Request URL: {response.request.url}\n"
        f"Request Headers: {response.request.headers}\n"
        f"Request Body: {response.request.body}\n"
    )
    
    if response.status_code == 200:
        response_details = (
            f"Response Headers: {response.headers}\n"
            f"Response Content: {response.json()}\n"
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
