from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import subprocess
import json
import ollama

app = FastAPI()

MODEL = "phi3:mini"

class Query(BaseModel):
    ingredients: List[str]





def query_ollama(prompt):

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']



def build_prompt(ingredients):

    ingredients_str = ", ".join(ingredients)

    prompt = f"""
You are a recipe assistant.

User ingredients: {ingredients_str}

Suggest a recipe using ONLY these ingredients.
Include:
- recipe name
- steps
- cooking time
"""

    return prompt


@app.post("/recipe")
def get_recipe(query: Query):

    prompt = build_prompt(query.ingredients)

    response = query_ollama(prompt)

    return {
        "ingredients": query.ingredients,
        "recipe": response
    }
