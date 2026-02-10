# Recipe Chatbot using Local LLM (FastAPI + Ollama)

## Overview

This project implements a local AI-powered recipe chatbot using an open-source LLM (phi3:mini) running locally via Ollama. The chatbot accepts ingredients and suggests recipes.

The system includes:

* Local LLM integration
* FastAPI backend
* CLI chatbot interface
* Fully local execution

---

## Requirements

* Python 3.8+
* Windows or Linux
* Ollama installed

---

## Step 1: Install Ollama

Download and install from:

[https://ollama.com/download](https://ollama.com/download)

Verify installation:

```
ollama --version
```

Install model:

```
ollama pull phi3:mini
```

---

## Step 2: Install Python dependencies

Navigate to project folder:

```
cd task2
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Step 3: Run FastAPI server

```
uvicorn api.server:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

API documentation available at:

```
http://127.0.0.1:8000/docs
```

---

## Step 4: Run chatbot

Open new terminal:

```
cd chatbot
python cli_chatbot.py
```

---

## Sample Input

```
eggs, onion
```

---

## Expected Output

```
Recipe Name: Simple Onion Omelette with Eggs

Ingredients:
- Eggs
- Onion

Steps:
1. Beat eggs
2. Cook onion
3. Combine and cook
```

---

## API Test Example

POST request:

```
POST http://127.0.0.1:8000/recipe
```

Body:

```
{
  "ingredients": ["egg", "onion"]
}
```

Response:

```
{
  "ingredients": ["egg", "onion"],
  "recipe": "Simple Onion Omelette Recipe..."
}
```

---

## Project Architecture

```
User → CLI Chatbot → FastAPI → Ollama Local LLM → Response
```

---

## Dependencies

```
fastapi
uvicorn
ollama
requests
pydantic
```

---

## Verification Steps

1. Install Ollama
2. Pull model phi3:mini
3. Install Python dependencies
4. Run FastAPI server
5. Run chatbot
6. Enter ingredients
7. Verify recipe output

---

## Fully Local Execution

This project runs entirely locally without any external APIs.
