import requests

MCP_URL = "http://localhost:8000"
OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3"

user_id = "student1"
turn_id = 1


def retrieve_context(query):

    r = requests.get(
        f"{MCP_URL}/memory/context_search",
        params={"query": query}
    )

    return r.json()


def store_memory(role, content):

    global turn_id

    payload = {
        "user_id": user_id,
        "turn_id": turn_id,
        "role": role,
        "content": content
    }

    requests.post(
        f"{MCP_URL}/memory/write",
        json=payload
    )

    turn_id += 1


def generate_response(user_input, context):

    prompt = f"""
You are an AI Academic Advisor.

Relevant past memories:
{context}

Student question:
{user_input}

Give helpful academic advice.
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]


print("\nAI Academic Advisor Started\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # retrieve memory
    context = retrieve_context(user_input)

    print("\nSearching memory...")

    # generate LLM response
    response = generate_response(user_input, context)

    print("\nAdvisor:", response)

    # store conversation
    store_memory("user", user_input)
    store_memory("assistant", response)

    print()