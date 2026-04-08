def calc(a,b,operator):
    try:
         if operator == "+":
          return a + b
         elif operator == "-":
          return a - b
         elif operator == "*":
          return a * b
         elif operator == "/":
           if b == 0:
            return "cant be divided by zero"
           return a / b
         else:
          return "invalid "
    
    except:
      return "something wrong"

while True:
          try:
             a = int(input("enter the number :"))
             b = int(input("enter the number :"))
             operator = input(" enter the operator :+ * - / ")
             print (calc(a,b,operator))
             break
          except ValueError:
            print("enter the number only")