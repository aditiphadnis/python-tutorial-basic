# Learning inheritance in Python
# Inheritance is a procedure in which one class inherits attributes and methods 
# from another class. 
# The class that inherits is called the subclass, and 
# the class that is inherited from is called the superclass.

#How to inherit a parent class? Use the following syntax:

class Car:
    def __init__(self, make, mileage):
        self.make = make
        self.mileage = mileage

    def description(self):
        return f"The {self.make} car gives the mileage {self.mileage} km/hour."

class BMW(Car):
    pass

class Audi(Car):
    def audi_desc(self):
        return "This is the description method of class Audi."
    

obj1 = BMW("BMW 7-series", 39.53)
print(obj1.description())
obj2 = Audi("Audi Q5", 42.34)
print(obj2.description())
print(obj2.audi_desc())
