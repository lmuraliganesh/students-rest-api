from flask import Flask, render_template
updateapp = Flask(__name__)

@updateapp.route("/")
def home():
    fruits = ["Apple", "Banana", "Mango", "Orange"]
    return render_template("home.html", fruits=fruits)

@updateapp.route("/about")
def about():
    return render_template("about.html")

@updateapp.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    updateapp.run(debug=True)