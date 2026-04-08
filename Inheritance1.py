class Vehicle:
     def __init__(self, brand, speed):
          self.brand = brand
          self.speed = speed

     def show_details(self):
          print("brand is", self.brand)
          print("speed is", self.speed)
    
     def move(self):
          print(self.brand, "is moving")

class Car(Vehicle):
     def __init__(self, brand, speed,doors,model):
          super().__init__(brand, speed)
          self.doors=doors
          self.model = model
    
     def show_details(self):
          super().show_details()
          print("doors", self.doors)
          print("model is", self.model)

class Bike(Vehicle):
     def __init__(self, brand, speed, type,millage):
          super().__init__(brand, speed)
          self.type = type
          self.millage = millage
           
     def show_details(self):
        super().show_details()
        print("type:",self.type)
        print("millage is ", self.millage)

car = Car("toyota", 200, 4, 2020)
bike = Bike("TVS", 120, "2stroke",50)

car.show_details()
car.move()
print("---")
bike.show_details()
bike.move()





