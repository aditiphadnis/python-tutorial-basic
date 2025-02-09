class Kettle():

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

print("*" * 80)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make)
print(hamilton.price)

print("*" * 80)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.power = 1.5

print("*" * 80)

print(hamilton.on)

Kettle.switch_on(hamilton)
print(hamilton.on)

print("*" * 80)
print(Kettle.power_source) 
print(kenwood.power_source)
print(hamilton.power_source)
print("*" * 80)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)