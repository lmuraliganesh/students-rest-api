from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("students.db") # create data base
    conn.row_factory = sqlite3.Row # access columns by name!
    return conn

def init_db():
    conn = get_db()
    conn.execute(""" 
            CREATE TABLE IF NOT EXISTS students(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 age INTEGER,
                 city TEXT
            )
        """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

#add student details

@app.route("/add", methods = ["GET" ,"POST"])
def add():
    if request.method == "POST":
      name  = request.form["name"]
      age = request.form["age"]
      city = request.form["city"]
      conn= get_db()
      conn.execute("""INSERT INTO students(name, age, city)
                   VALUES(?,?,?)""" , (name, age, city))
      conn.commit()
      conn.close()
      return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__" :
    init_db()
    app.run(debug=True)

