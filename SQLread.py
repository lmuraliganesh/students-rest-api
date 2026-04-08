import sqlite3
read = sqlite3.connect("mydatabase.db")
pen = read.cursor()

print("=== NAME A to Z ===")
pen.execute("SELECT * FROM students ORDER BY name")
results = pen.fetchall()
print("====print all students===")
for row in results:
     print(row)

pen.execute("SELECT * FROM students ORDER BY age")
results = pen.fetchall()
print("====print all students===")
for row in results:
     print(row)


print("=== AGE HIGH TO LOW ===")
pen.execute("SELECT * FROM students ORDER BY age DESC")
results = pen.fetchall()
for row in results:
    print(row)

pen.execute("SELECT SUM(age) FROM students")
fetch = pen.fetchone()
print (round(fetch[0], 0))

pen.execute("SELECT location, COUNT(*) FROM students GROUP BY location")
results = pen.fetchall()

print("=== STUDENTS PER CITY ===")
for row in results:
    print(f"{row[0]}: {row[1]} students")


pen.execute("SELECT location, AVG(age) FROM students GROUP BY location")
results = pen.fetchall()

print("=== AVERAGE AGE PER CITY ===")
for row in results:
    print(f"{row[0]} : {round(row[1], 1)} years")

read.close