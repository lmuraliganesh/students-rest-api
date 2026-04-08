with open("test.txt", "w") as page :
    page.write("name : ganesh\n")
    page.write("city : chennai\n")

with open("test.txt","r") as page :
    content = page.read()
    print(content)