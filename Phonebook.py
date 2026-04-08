phonebook ={
    "Ravi" : 95661100176,
    "Lakshmi" : 9899909322,
    "Harsih" : 800044086

}
search = input("search for the friend:")
if search in phonebook:
         
      print(search,":", phonebook[search])
      
    
else:
    print("not in the storage")
   
