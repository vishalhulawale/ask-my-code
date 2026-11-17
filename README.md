Phase 0 — Python + first LLM call (3–5 days)

Goal: Get comfortable with Python and call an LLM from code.

    1. Set up Python 3.12, VS Code and a virtual environment with uv.
    2. Learn the Python you’ll actually use: functions, lists/dicts, classes, f-strings, reading files, pathlib, requests, type hints.
    3. Get an API key (Anthropic or OpenAI) and store it in a .env file using python-dotenv.
    4. Write hello_llm.py, which sends a question and prints the answer.
    5. Learn: prompts, system message vs user message, tokens, temperature.
    6. Done when: You can ask the LLM a question from your terminal.

Commands:
    python -m ensurepip --upgrade
    pip install uv
    uv venv venv
    source ./venv/Scripts/activate

    pip3 install python-dotenv
    pip3 install anthropic
    
