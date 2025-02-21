# We use abstraction for hiding the internal details or implementations of 
# a function and showing its functionality only.
# This is similar to the way you drive the car without knowing its background mechanism. 

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,name):
        self.name = name

    def description(self):
        return "This is the description method of the Car class."

    @abstractmethod
    def price(self,x):
        pass

class New(Car):
    def price(self,x):
        print(f"The price of {self.name} is {x} lakhs.")

obj = New("Honda City")

obj.description()
obj.price(25)
