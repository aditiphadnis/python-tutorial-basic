# Encapsulation is to ensure security. 
# If you declare a variable using single '_', it is a convention that 
# it is a private variable and should be used only within the class.
# Example _self.name or def _method().

# class Car:
#     def __init__(self, name, mileage):
#         self._name = name #protected variable
#         self.mileage = mileage

#     def description(self):
#         return f"The {self._name} car gives the mileage {self.mileage} km/hour." #protected variable

# obj = Car("BMW 7-series",39.53)

# #accessing protected variable via class method 
# print(obj.description())

# #accessing protected variable directly from outside
# print(obj._name)
# print(obj.mileage)

# class Car:
#     def __init__(self, name, mileage):
#         self.__name = name #protected variable
#         self.mileage = mileage

#     def description(self):
#         return f"The {self.__name} car gives the mileage {self.mileage} km/hour." #protected variable

# obj = Car("BMW 7-series",39.53)

# #accessing protected variable via class method 
# print(obj.description())

# #accessing protected variable directly from outside
# print(obj.__name)
# print(obj.mileage)

#Mangling 
class Car:
    def __init__(self, name, mileage):
        self.__name = name #protected variable
        self.mileage = mileage

    def description(self):
        return f"The {self.__name} car gives the mileage {self.mileage} km/hour." #protected variable

obj = Car("BMW 7-series",39.53)

#accessing protected variable via class method 
print(obj.description())

#accessing protected variable directly from outside
print(obj._Car__name)
print(obj.mileage)

