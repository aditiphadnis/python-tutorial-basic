# Dynamic bindiong or late binding means deciding 
# which method to call when the program runs. 
#This make your code more flexible because exact method to run, is chosen
# at run time based on the object type. 

class Car:
    def start_engine(self):

        raise NotImplementedError("Subclass must implement abstract method")
    
class Honda(Car):
    def start_engine(self):
        return "Honda car engine started."
    
class Audi(Car):
    def start_engine(self):
        return "Audi car engine started."
    
def start_car_engine(car):
    print(car.start_engine())

honda = Honda()
audi = Audi()

start_car_engine(honda)
start_car_engine(audi)


