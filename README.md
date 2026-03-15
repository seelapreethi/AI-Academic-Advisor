# AI Academic Advisor with MCP Memory

## Project Overview

This project implements an **AI Academic Advisor Agent** that uses a **Memory, Control, and Process (MCP) architecture** to maintain long-term context beyond the LLM’s context window.

The system stores structured conversation history in **SQLite** and semantic memory in **ChromaDB**, enabling the agent to recall past conversations and provide personalized academic guidance.

The agent communicates with a memory backend (MCP server) through exposed memory tools and uses a local LLM via **Ollama** for generating responses.


# Architecture

The system follows the **MCP (Memory–Control–Process) pattern**.

**Memory**

* SQLite (structured memory)
* ChromaDB (vector similarity memory)

**Control**

* MCP Server built using FastAPI
* Exposes memory tools for the agent

**Process**

* LLM Agent running locally using Ollama

### Data Flow

User → Agent → MCP Server → Databases
Agent retrieves relevant memory → Generates response using LLM → Stores conversation back to memory


# System Architecture Diagram

See: `docs/memory_architecture.png`

User
 │
 ▼
LLM Agent
 │
 ▼
MCP Server (FastAPI)
 │
 ├── memory_write
 ├── memory_read
 └── memory_retrieve_by_context
 │
 ├── SQLite (structured memory)
 └── ChromaDB (vector memory)


# Memory Components

## Structured Memory (SQLite)

Stores:

* Conversation history
* User preferences
* Academic milestones

Implemented using:

* SQLAlchemy ORM
* Pydantic validation

Tables include:

* conversations
* preferences
* milestones


## Semantic Memory (Vector Store)

ChromaDB stores vector embeddings of conversation text.

Embeddings generated using:

* sentence-transformers model
* `all-MiniLM-L6-v2`

This allows the system to retrieve context using **semantic similarity rather than keywords**.


# Memory Tools (MCP API)

The MCP server exposes the following tools.

### memory_write

Stores conversation turns and indexes embeddings.

POST `/memory/write`

Example request:


{
 "user_id": "student1",
 "turn_id": 1,
 "role": "user",
 "content": "I want to learn AI"
}



### memory_read

Retrieves recent conversations for a user.

GET `/memory/read?user_id=student1`



### memory_retrieve_by_context

Performs semantic similarity search using vector embeddings.

GET `/memory/context_search?query=AI`



# LLM Agent

The agent uses **Ollama** to run a local LLM such as:

* llama3
* mistral

Agent workflow:

1. User asks a question
2. Agent retrieves relevant memories
3. Agent sends prompt + memory to LLM
4. LLM generates response
5. Conversation stored in long-term memory



# Project Structure


ai-academic-advisor-mcp
│
├── docker-compose.yml
├── README.md
├── submission.json
├── .env.example
│
├── data
│
├── docs
│   └── memory_architecture.png
│
├── mcp_server
│   ├── Dockerfile
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── vector_store.py
│   ├── memory_schemas.py
│   └── memory_tools.py
│
└── agent
    └── advisor_agent.py


# Setup Instructions

## 1 Install Docker

Install Docker and Docker Compose.



## 2 Clone Repository

git clone <repository-url>
cd ai-academic-advisor-mcp




## 3 Create Environment File

Copy the example file.


cp .env.example .env


## 4 Start MCP Server


docker-compose up --build


Server runs at:


http://localhost:8000


API documentation:


http://localhost:8000/docs


## 5 Install and Run Ollama

Install Ollama locally.

Pull a model:


ollama pull llama3


Run the model:


ollama run llama3


## 6 Start the Agent

Open another terminal:


cd agent
python advisor_agent.py


# Example Interaction


You: I want to learn AI

Advisor:
To start learning AI, begin with Python programming,
linear algebra, probability, and machine learning fundamentals.


The conversation is stored in long-term memory and can be retrieved later.



# Key Features

* Long-term conversational memory
* Hybrid memory architecture
* Semantic search using embeddings
* Local LLM inference using Ollama
* Containerized deployment with Docker
* Modular MCP server architecture



# Future Improvements

* Add user profile personalization
* Improve milestone tracking
* Add academic course recommendation engine
* Implement automatic memory summarization
* Add LangChain or autonomous agent planning



# Author

AI Academic Advisor MCP Project
