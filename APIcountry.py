import requests 

def world(country):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    data = response.json()[0]
    print(data.keys())
    print("Country   :", data["name"]["common"])
    print("Population:", data["population"])
    print("Flag      :", data["flag"])
    print("languages:", list(data["languages"].values())[0])
    print("Currency  :", list(data["currencies"].keys())[0])
country = input("enter ther name :")
world(country)



