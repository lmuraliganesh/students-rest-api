while True:       
    try:
          a = int(input("enter the number : "))
          b = int(input("enter the number : "))
          print("result :", a/b)
    
    except ValueError:
     print("this is not the number ")
      
    except ZeroDivisionError:
     print("cannot divided zero")

    finally:
     print("thanks for using this program")

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() == "no":
     print("Goodbye!")
     break
         