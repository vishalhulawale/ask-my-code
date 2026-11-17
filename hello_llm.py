from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()

ANTHROPIC_API_KEY=os.environ.get("ANTHROPIC_API_KEY")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

message = client.messages.create(
    max_tokens=1024,
    system="You are an senior developer who has expertise in understanding given code and answering questions related to it accurately",
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude. My name is Vishal"
        }
    ],
    model="claude-haiku-4-5"
)

for content in message.content:
    if content.type == "text":
        print(content.text)
