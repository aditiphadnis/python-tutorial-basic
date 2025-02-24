# Do you know List Comprehensions are 
# 35% faster than FOR loop and 45% faster than map function?

y = [x**2 for x in range(0,10)]

print(y)

z = [x for x in range(0,10) if x % 2 == 0]

print(z)

p = [x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']]
print(p)


