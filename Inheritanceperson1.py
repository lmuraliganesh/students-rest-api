class Person: 
     def __init__(self, name, age):
          self.name = name
          self.age = age

     def introduce(self):
          print("Hi i am :", self.name)

class Student(Person):
     def __init__(self, name, age, grade):
          super().__init__(name, age)  
          self.grade = grade
    
     def introduce(self):
          super().introduce()
          print("i am studying grade :", self.grade)

class Teacher(Person):
     def __init__(self, name, age, teach):
          super().__init__(name, age) 
          self.teach = teach

     def introduce(self):
         super().introduce()
         print("i teach :", self.teach)

student1 = Student("Ganesh", 7, "A")
teacher1 = Teacher("lakshmi", 30, "Python")

student1.introduce()
print("-----------------")
teacher1.introduce()


