import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except:
        return []
    
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
        
def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    city = input("Enter city: ")
    contact = {
        "name": name,
        "phone": phone,
        "city": city
    }
    contacts.append(contact)
    save_contacts()         # ✅ save after adding!
    print(name, "added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found!")
    else:
        for contact in contacts:
            for key, value in contact.items():
                print(key, ":", value)

def delete_contacts():
    search = input("enter the name : ")
    for contact in contacts:
             if contact["name"].lower() == search.lower():            
              contacts.remove(contact)
              print("contact deleted")

def search_contacts():
    search = input("enter the name : ")
    for contact in contacts:
             for key, value in contact.items():
               if contact['name'].lower() == search.lower():
                print(key, ":", value)
            

def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

contacts = load_contacts()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        delete_contacts()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")