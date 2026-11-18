from dotenv import load_dotenv
import os
from anthropic import AnthropicFoundry

load_dotenv()


client = AnthropicFoundry(
    base_url=os.environ.get("AZURE_FOUNDRY_BASE_URL"),
    api_key=os.environ.get("AZURE_FOUNDRY_API_KEY")
)

message = client.messages.create(
    max_tokens=1024,
    system="You are an senior developer who has expertise in understanding given code and answering questions related to it accurately",
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude. My name is Vishal"
        }
    ],
    model=os.environ.get("AZURE_FOUNDRY_DEPLOYMENT")
)

for content in message.content:
    if content.type == "text":
        print(content.text)
