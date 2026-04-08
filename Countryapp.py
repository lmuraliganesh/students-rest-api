from flask import Flask,render_template, request
import requests

countryapp = Flask(__name__)

@countryapp.route("/")
def home():
 return render_template("home.html")

@countryapp.route("/country", methods=["POST"])
def country():
    name = request.form["country"]
    response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
    data = response.json()[0]

    country_info = {
         "name": data["name"]["common"],
        "capital": data["capital"][0],
        "population": data["population"],
        "region": data["region"],
        "flag": data["flag"],
        "currency": list(data["currencies"].keys())[0],
        "language": list(data["languages"].values())[0]
    }
    return render_template("country.html", info=country_info)
    
if __name__ == "__main__":
    countryapp.run(debug=True)
