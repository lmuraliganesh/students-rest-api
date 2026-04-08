with open("info.txt", "a") as file:
    for i in range(1,4):
        line = input("enter the line:")
        file.write(line + "\n")

with open("info.txt", "r") as file:
    for line in file:
        print(line)     