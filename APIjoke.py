import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()

print("Full data:", data)
print("----------")

print("keys:", data.keys())
print("-----------")

print("joke? :", data["setup"])
print("Answer  :", data["punchline"])
