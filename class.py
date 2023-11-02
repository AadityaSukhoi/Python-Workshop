#Classes in Python are like blueprints for creating objects to encapsulate both data and behavior.

#Creating a Class
class Car:
    def __init__(self, make, model):
        self.make= make
        self.model= model

#Creating objects from the classes
car1=Car("Nissan" , "GTR")
car2=Car("BMW","M5 Competition")

print(car1.make , car1.model)
print(car2.make , car2.model)