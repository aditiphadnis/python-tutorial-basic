#A python for loop control statement is used to iterate over data structures 
# like python lists, arrays, dictionaries, sets, tuples or even strings.

list = [1, 2, 3, 4, 5]

for num in list:
    print("Hello World!: ", num)

even_nums = []

for i in range(1, 11):
    if i % 2 == 0:
        even_nums.append(i)
print("Even number list: ", even_nums)

iterator = (1, 2, 3, 4, 5)
for i in iterator:
    print("Hello World!: ", i)
else:
    print("Loop completed successfully. No more elements to iterate.")

example = {"name": "John", 
           "age": 30, 
           "city": "New York"}

for i in example:
    print(i, example[i])
for key in example:    
    print(f"{key}: {example[key]}")

for key, value in example.items():  
    print(f"{key}: {value}")