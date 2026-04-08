import pandas as pd 

data = {
    "Name" : ["Ganesh", "Lakshmi", "Kabilan", "Tamizh"],
    "Age" : [39, 30, 4, 3],
    "City" : ["Chennai", "madhavaram", "Velachery", "Adayar"],
    "Salary" : [500000, 300000, 20000, 19000]
}

df = pd.DataFrame(data)

print(df)

print("========")
print("Shape:", df.shape)
print("Total rows:", len(df))
print("Columns:", df.columns.tolist())

print("=== CHENNAI ONLY ===")
chennai = df[df["City"] == "Chennai"]
print(chennai)

print("\n=== AGE > 30 ===")
older = df[df["Age"] > 30]
print(older)

print("\n=== AGE < 30 ===")
older = df[df["Age" ] <= 30]
print(older)

print("\n=== HIGH SALARY ===")
rich = df[df["Salary"] > 40000]
print(rich)

print("=== STATISTICS ===")
print("Average age :", df["Age"].mean())
print("Max salary:", df["Salary"].max())
print("Min salary:", df["Salary"].min())
print("Average salary:", df["Salary"].mean())
print("Sum of salary :", df["Salary"].sum())
print(df.describe())
