import requests
def dog(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    data = response.json()

    if data["status"] == "success":
        print("Breed :", breed)
        print("Image :", data["message"])
        print("Copy URL and paste in browser to see!")
    else:
        print("Breed not found! Try another breed!")

breed= input("enter the bread name : ")
dog(breed)