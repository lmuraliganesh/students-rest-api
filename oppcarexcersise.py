class car:
    def __init__(self, brand, colour, speed, model):
        self.brand = brand
        self.colour = colour
        self.speed = speed
        self.model = model
    def show_brand(self):
        print("brand is", self.brand)
    def show_colour(self):
        print("colour is", self.colour)
    def show_accelerate(self):
        self.speed = self.speed + 10 
        print("speed is :", self.speed)
    def show_model(self):
        print("model is", self.model)
p1 = car("volvo", "white", 100, "2000")
p2 = car("benz", "black", 120, "2020")
p3 = car("maruti", "black", 80, "2010")

p2.show_brand()
p2.show_accelerate()
p2.show_model()