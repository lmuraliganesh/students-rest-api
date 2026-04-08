import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
       print(response.text)
    else:
        print("error")

city = input("enter the city: ")
get_weather(city)



    