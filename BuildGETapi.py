from flask import Flask, jsonify, request

app = Flask(__name__)


students = [{"id" : 1, "name" : "Ganesh", "city" : "Chennai", "age" : 39},
            {"id" : 2, "name" : "murali", "city" : "madurai", "age" : 50},
            {"id" : 4, "name" : "jithesh", "city" : "Chennai", "age" : 88},
            {"id" : 3, "name" : "suresh", "city" : "coimbatore", "age" : 76}
        ]
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Students API!",
        "endpoints": [
            "/api/students",
            "/api/students/<id>",
            "/api/students/city/<city>"
        ]
    })
# PUT — update student
@app.route("/api/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    if not data:
        return jsonify({
            "status" : "error",
            "message": "No data provided!"
        }), 400

    for student in students:
        if student["id"] == id:
            # update only fields that are provided!
            student["name"] = data.get("name", student["name"])
            student["age"]  = data.get("age",  student["age"])
            student["city"] = data.get("city", student["city"])

            return jsonify({
                "status" : "success",
                "message": "Student updated!",
                "student": student
            }), 200

    return jsonify({
        "status" : "error",
        "message": "Student not found!"
    }), 404


# DELETE — remove student
@app.route("/api/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({
                "status" : "success",
                "message": f"Student {id} deleted!"
            }), 200

    return jsonify({
        "status" : "error",
        "message": "Student not found!"
    }), 404

@app.route("/api/students", methods =["POST"])
def add_students():
    data = request.get_json()

    if not data :
        return jsonify({
             "status" : "error",
            "message": "No data provided!"
        }), 400
    
    if "name" not in data or "age" not in data or "city" not in data:
        return jsonify({
            "status" : "error",
            "message" : "name, age and city are required!"
        }), 400
    
    new_student = {
        "id"  : len(students) + 1,
        "name": data["name"],
        "age" : data["age"],
        "city": data["city"]
    }

    students.append(new_student)

    return jsonify({
        "status" : "success",
        "message": "Student added!",
        "student": new_student
    }), 201

@app.route("/api/students", methods = ["GET"])
def get_students():
    return jsonify({
        "status" : "success",
        "count"  : len(students),
        "students": students
    }), 200

@app.route("/api/students/age/<int:age>", methods=["GET"])
def get_age_students(age):
 result = [s for s in students if s["age"] == age]
 if result:
        return jsonify({
            "status"  : "success",
            "age"    : age,
            "count"   : len(result),
            "students": result
        }), 200
 return jsonify({
        "status" : "error",
        "message": f"No students found in {age}"
 }), 400

@app.route("/api/students/<int:id>", methods = ["GET"])
def get_student(id):
    
    for student in students:
        if student["id"] == id:
            return jsonify({
                "status" : "success",
                "student": student
            }), 200
        
    return jsonify({
     "status" : "error",
     "message": "Student not found!"
     }), 400

@app.route("/api/students/city/<string:city>", methods = ["GET"])
def get_City_students(city):
 result = []
 for s in students:
    if s["city"].lower() == city.lower():
       result.append(s)
 if result:
        return jsonify({
            "status"  : "success",
            "city"    : city,
            "count"   : len(result),
            "students": result
        }), 200
 return jsonify({
        "status" : "error",
        "message": f"No students found in {city}"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)

