import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT,
        mobile INTEGER,
        country TEXT      
               
    )
""")

students = [
    (451,"Ganesh", 39, "Chennai", 98888833344, "Sweden"),
    (230,"Lakshmi", 30, "Chennai",98888833344, "Sweden"),
    (901,"Ravi", 25, "Mumbai", 98888833344, "Sweden"),
    (122,"Priya", 28, "Delhi", 98888833344, "Sweden"),
    (333,"Kumar", 32, "Bangalore", 98888833344, "Sweden"),
    (123,"Revethi", 77, "Navi Mumbai", 98888833344, "Sweden"),
    (113,"Noortha", 68, "NewDelhi",98888833344, "Sweden"),
    (222,"AshokKumar", 22, "Chennai",98888833344, "Sweden")
]

cursor.executemany("""
    INSERT INTO students (id, name, age, city,mobile,country)
    VALUES (?, ?, ?, ?, ?, ?)
""", students)

conn.commit()


print("=== ALL STUDENTS ===")
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
for row in results:
    print(row)


print("---")

print("=== NAMES ONLY ===")
cursor.execute("SELECT name, city FROM students")
results = cursor.fetchall()

for row in results:
    print(row)

print("---")

print("===CITY ONLY===")
print("___________")

cursor.execute("SELECT * FROM students WHERE city = 'Chennai' ")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()

print("Data inserted successfully!")

