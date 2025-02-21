# Polymorphism is the ability to take different forms
# Poly means many and morph means forms
# Polymorphism refers to functions having same names but different functionalities. 

class Audi:
  def description(self):
    print("This the description function of class AUDI.")

class BMW:
  def description(self):
    print("This the description function of class BMW.")

audi = Audi()
bmw = BMW()
for car in (audi,bmw):
 car.description()
