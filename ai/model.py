from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.inference.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


project_connection_string = os.getenv("PROJECT_CONNECTION_STRING")
if not project_connection_string:
    raise ValueError("PROJECT_CONNECTION_STRING is not set in the environment variables.")

# Initialize Azure AI client
project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential()
)
chat = project.inference.get_chat_completions_client()

# Generate content using Azure AI
def generate_content(prompt):
    try:
        response = chat.complete(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.8,
            frequency_penalty=0.5,
            presence_penalty=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content: {e}")
        return None
