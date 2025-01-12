from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from azure.ai.inference.prompts import PromptTemplate
import os

# Load environment variables
load_dotenv()

# Initialize Azure AI client
project_connection_string = os.getenv("PROJECT_CONNECTION_STRING")
if not project_connection_string:
    raise ValueError("PROJECT_CONNECTION_STRING is not set in the environment variables.")

project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential()
)
chat = project.inference.get_chat_completions_client()

system_role = {"role": "system", "content": "You are an AI assistant tasked with generating blog posts for a company's services. Focus on public-facing content while protecting sensitive information. Each post should include: - A unique and catchy title. - Detailed blog content optimized for SEO. - Keywords for SEO and a meta description. - Links to other relevant pages (deep linking). - Content targeting diverse markets. - A call-to-action to schedule a consultation. - 1000 words or more. - be creative and engaging."}

# Generate content using Azure AI
def generate_content(prompt):
    try:
        response = chat.complete(
            model="gpt-4o-mini",
            messages=[{
                "role": "system",
                "content": "you are an AI assistant tasked with generating blog posts for a company's services. Focus on public-facing content while protecting sensitive information."
            }],
            temperature=0.8,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            max_tokens=1000,
            tools=["content-creation"],
        )
        return response.choices
    except Exception as e:
        print(f"Error generating content: {e}")
        return None


def get_chat_response(messages):
    # create a prompt template from an inline string (using mustache syntax)
    prompt_template = PromptTemplate.from_string(
        prompt_template= system_role
    )

    # generate system message from the template, passing in the context as variables
    # system_message = prompt_template.create_messages(data=context)

    # add the prompt messages to the user messages
    return chat.complete(
        model="gpt-4o-mini",
        messages= messages,
        temperature=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )
