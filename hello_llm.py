from dotenv import load_dotenv
import os
from anthropic import AnthropicBedrock

load_dotenv()

ANTHROPIC_API_KEY=os.environ.get("ANTHROPIC_API_KEY")

client = AnthropicBedrock(api_key=ANTHROPIC_API_KEY, aws_region="ap-south-1")

message = client.messages.create(
    max_tokens=1024,
    system="You are an senior developer who has expertise in understanding given code and answering questions related to it accurately",
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude. My name is Vishal"
        }
    ],
    model="in.anthropic.claude-haiku-4-5-20251001-v1:0"
)

print(message.to_json())

for content in message.content:
    if content.type == "text":
        print(content.text)
