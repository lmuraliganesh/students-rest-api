import random

secret = random.randint(1, 10)
attempts = 0

while True:
    try:
        guess = int(input("enter the number :"))
        attempts = attempts + 1

        if guess < secret:
          print("Too low")
        elif guess > secret:
          print("too high")
        else:
          print("🎉 Correct! You got it in", attempts, "attempts!")
          break
    except ValueError:
     print("enter the number :")
      
           

      
          
