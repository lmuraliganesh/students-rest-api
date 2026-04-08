def calculator(a, b, operator):
    if operator == "+":
     return a + b
    elif operator == "-":
     return a - b
    elif operator == "*":
     return a * b
    elif operator == "/":
              if b == 0:
               return "cant be divided by zero"
    else :
     return "invalid"

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    output =calculator(a,b,operator)
    print(output)
    break