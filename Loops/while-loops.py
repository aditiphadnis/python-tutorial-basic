#Print Hello World! 10 times
num_of_times =1

while num_of_times <= 10:
    print(f"Hello World! {num_of_times}")
    num_of_times += 1
    
# Even number list less than 10
num = 1
even_nums = []

while num <= 10:
    if num % 2 == 0:
        even_nums.append(num)
    num += 1
print("Even number list: ", even_nums)

# Infitine loop 

# i = True
# while i:
#     print("Condition satisfied")

var = 1
while var < 4:
    print("Condition satisfied: {}".format(var))
    var += 1
else:
    print("Condition not satisfied: {}".format(var))