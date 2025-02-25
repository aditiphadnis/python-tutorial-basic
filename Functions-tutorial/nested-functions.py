

def outer_func(who):
    def inner_func():
        print(f"Hello, {who}")
    inner_func()

print("-------")
outer_func("World!")

outer_func("Python!")
print("-------")

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("The number must be whole.")
    if number < 0:
        raise ValueError("The number must be non-negative.")
    #Factorial calculation
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)
 
print(factorial(4))
print(factorial(10))
