class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def greet(self):
        print("Hello", self.name)
    def show_age(self):
        print("my age is", self.age)
    def cities(self):
        print("i am from :",self.city)

p1 = Person("Ganesh",33,"chennia")
p2 = Person("Lakshmi", 23, "stockholm")
p3 = Person("vijaylakshmi", 53, "stockholm")

p1.greet()
p1.show_age()
p1.cities()





