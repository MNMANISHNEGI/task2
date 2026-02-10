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
**Recipe Name: Simple Onion Omelette**


**Ingredients:** (Note that eggs and onions are the only required items)

- 2 large eggs

- Salt, to taste

- Black pepper, freshly ground, to taste

- Butter or cooking spray for greasing pan

- 1 small finely chopped onion (adjust quantity as needed based on desired amount of incorporation)


**Steps:**

1. In a mixing bowl, beat the eggs with salt and pepper until well combined. Set aside.

2. Heat butter or cooking spray in a non-stick frying pan over medium heat. Add the chopped onion and sauté for about 3 minutes until they become translucent. Be sure to stir occasionally so that it doesn't burn.

3. Pour the eggs into one half of the skillet, letting them sit undisturbed as they begin to set at the edges. Using a spatula gently push the egg from the set edge toward the center allowing uncooked liquid to flow underneath towards the pan’s side not in contact with the onions (folding technique). Continue until no runny eggs remain, for about 2-3 minutes depending on how many servings you are making.

4. Carefully slide your omelette onto a plate and serve immediately while hot. Enjoy this simple yet delicious Onion Omelette!
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
