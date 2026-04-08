age = int(input("enter the age:"))
citizen =input("are you citizen? (yes/no):")
if age >=18 :
    if citizen == "yes":
        print("you can vote")
    else :
        print("you must be citizen to vote")
else:
    print("you must be 18 and above to vote")