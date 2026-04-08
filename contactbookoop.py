class Contact:
    def __init__(self, name, mobile, city):
        self.name = name
        self.mobile = mobile
        self.city = city

    def show(self):
        print("Name :", self.name)
        print("Mobile :", self.mobile)
        print("City:", self.city)
        print("--------------")

class Contactbook:
    def __init__(self):
        self.contacts =[]
    
    def Add_contact(self, name, mobile, city):
        contact = Contact(name, mobile, city)
        self.contacts.append(contact)
        print("contact added")
    
    def View_contacts(self):
        if len(self.contacts) == 0:
            print("no contacts")
        else:
            for contact in self.contacts:
                contact.show()
    
    def Search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.show()
                return
            print("contant not found")

    def Delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
               self.contacts.remove(contact)
               print(name,"contact removed")
               return
            print("contact not found")

book = Contactbook()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("enter the choice : ")

    if choice == "1":
        name = input("entet the name").capitalize()
        mobile = int(input("enter the mobile number :"))
        city = input("enter the city name :")
        book.Add_contact(name, mobile, city)
    
    elif choice == "2":
        book.View_contacts()

    elif choice == "3":
        name = input("enter the name :").capitalize()
        book.Search_contact(name)
    
    elif choice == "4":
        name = input("enter the name :").capitalize()
        book.Delete_contact(name)
    
    elif choice == "5":
        print("good bye")
        break
    else:
     print("invalid")
    