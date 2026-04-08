contacts = []
def add_contact():
    name = input("enter the name :")
    mobile = int(input("enter the mobile number :"))
    city = input("enter the city : ")
    contact ={
        "Name" : name,
        "Mobile" : mobile,
        "City" : city
    } 
    contacts.append(contact)
    print("contacts added ")
   

def view_contacts():
    if len(contacts) == 0:
         print("no contacts")
    else:
        for i in contacts:
            for key, value in i.items():
                print(key, ":", value)
                

def search_contacts():
    search = input("enter the name :")
    for x in contacts: 
     for key, value in x.items():
      if x['Name'].lower() == search.lower():
          print(key, ":", value)
        
    else:
        print("no contacts")

def delete_contacts():
         search = input("enter the name :")
         for contact in contacts:
             if contact["Name"].lower() == search.lower():            
              contacts.remove(contact)
              print("contact deleted")

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. delete contact")

    choice = input("enter your choice")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
         delete_contacts()
    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
     print("break")
     break
    
       