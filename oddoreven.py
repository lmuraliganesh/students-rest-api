def odd_or_even(n):
    if n % 2 != 0:
        return "odd"
    else:
        return "even"
    
while True:
    n = int(input("enter the number :"))
    if n == 0:
        print("bye")
        break
    print(odd_or_even(n))
