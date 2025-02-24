num = 1
odd_nums = []
while num:
    if num % 2 != 0:
        odd_nums.append(num)
    if num >= 20:
        break
    num += 1

print("Odd number list: ", odd_nums)

a = [i for i in range(1,101) if int(i**0.5)==i**0.5]
    