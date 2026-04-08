import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    print("Weather  :", response.text)

def world(country):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    data = response.json()[0]
    
    print("Country   :", data["name"]["common"])
    print("Population:", data["population"])
    print("Flag      :", data["flag"])
    print("languages:", list(data["languages"].values())[0])
    print("Currency  :", list(data["currencies"].keys())[0])

def joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    print("joke? :", data["setup"])
    print("Answer  :", data["punchline"])

def dog(breed):
    breed = breed.lower().strip()
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
          data = response.json()
          print("Breed :", breed)
          print("Image :", data["message"])
          print("Copy URL and paste in browser to see!")
        else:
           print("no image ")
           print("pug, labrador, husky, beagle, boxer")
    except Exception as e:
        print("Error:", e)
       

while True:
    print("\n list the option")
    print("1. Get Weather")
    print("2. Get Country Info")
    print("3. Get Dog Image")
    print("4. Get Random Joke")
    print("5. Exit")

    choice = input("enter the choice : ")

    if choice == "1":
        city = input("enter the city name :")
        get_weather(city)
    elif choice == "2":
        country = input("enter the country name :")
        world(country)
    elif choice == "3":
        breed = input("enter the breed name :")
        dog(breed)
    elif choice == "4":
        joke()
    elif choice == "5":
        print("good bye")
        break
    else:
        print("invalid")
        
