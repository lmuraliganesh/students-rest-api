def find_largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b 
    else:
     return c
     
while True:
     a = int(input("enter the first number :"))
     b = int(input("enter the second number :"))
     c = int(input("enter the third number :"))
     print(find_largest(a,b,c))
     break
