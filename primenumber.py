def prime_number(n):
    if n < 2:
        return False
    i = 2
    while i < n:
     if n % i == 0:
       return False
    i = i + 1
    return True

n = int(input("enter the number :"))

if prime_number(n):
    print(n, "is prime")
else:
    print(n, "is not prime")