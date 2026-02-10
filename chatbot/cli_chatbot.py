import requests

API_URL = "http://127.0.0.1:8000/recipe"

print("Recipe Chatbot")
print("Enter ingredients separated by comma")

while True:

    user_input = input("\nYou: ")

    ingredients = [x.strip() for x in user_input.split(",")]

    response = requests.post(
        API_URL,
        json={"ingredients": ingredients}
    )

    result = response.json()

    print("\nBot:")
    print(result["recipe"])
    