from flask import Flask, jsonify, request
import sqlite3


app =Flask(__name__)
DATABASE = "students_api.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute(""" CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 age INT NOT NULL,
                 city TEXT NOT NULL)""")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return jsonify({
        "message"  : "Students REST API with SQL!",
        "endpoints": {
            "GET"   : "/api/students",
            "GET"   : "/api/students/<id>",
            "POST"  : "/api/students",
            "PUT"   : "/api/students/<id>",
            "DELETE": "/api/students/<id>"
        }
    })
@app.route("/api/students", methods = ["GET"])
def get_students():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return jsonify({
        "status" : "success",
        "count" : len(students),
        "students" : [dict(s) for s in students]
    }), 200

@app.route("/api/students/<int:id>", methods = ["GET"])
def get_student(id):
    conn = get_db()
    student = conn.execute("SELECT * FROM students WHERE id = ?", (id,)).fetchone()
    conn.close()

    if student:
        return jsonify ({
            "status" : "sucsess",
            "student" :  dict(student)

        }), 200
    return jsonify({
        ""
    })

@app.route("/api/students", methods = ["POST"])
def add_students():
    data = request.get_json()

    if not data:
        return jsonify({
            "status" : "error",
            "message" : "no data received"
        }), 400
    if "name" not in data or "age" not in data or "city" not in data:
        return jsonify({
            "status" : "error",
            "message" : "name, age, city required"

        }),400
    
    conn = get_db()
    cursor = conn.execute("INSERT INTO students(name, age, city) VALUES (?,?,?)", (data ["name"], data["age"], data["city"]))
    conn.commit()

    new_id = cursor.lastrowid
    new_student = conn.execute("SELECT * FROM students WHERE id = ?", (new_id,)).fetchone()
    conn.close()

    return jsonify({
        "status" : "success",
        "message" : " Student added !",
        "student" : dict(new_student)
    }), 201

@app.route("/api/students/<int:id>", methods = ["PUT"])
def update_student(id):
    data = request.get_json()
    conn = get_db()
    student = conn.execute("SELECT * FROM students WHERE id = ?",(id,)).fetchone()

    if not student :
        conn.close()
        return jsonify({
            "status" : "error",
            "message" : f"Student {id} not found!"
        }), 404
    
    name = data.get("name", student["name"])
    age = data.get("age", student["age"])
    city = data.get("city", student["city"])

    conn.execute("""UPDATE students
                 SET name = ?,
                 age = ?,
                 city = ?
                 WHERE id = ?""", (name,age,city, id)
                 )
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": f"Student {id} updated successfully!"}), 200

@app.route("/api/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db()
    student = conn.execute("SELECT * FROM students WHERE id = ?", (id,)).fetchone()

    if not student :
        conn.close()
        return jsonify({
            "status" : "error",
            "message" : f"Student {id} not found!"
        }), 404
    
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)








    



