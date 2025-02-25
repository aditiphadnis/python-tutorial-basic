# Do you know List Comprehensions are 
# 35% faster than FOR loop and 45% faster than map function?

y = [x**2 for x in range(0,10)]

print(y)

z = [x for x in range(0,10) if x % 2 == 0]

print(z)

p = [x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']]
print(p)

a = [i for i in range(1,101) if int(i**0.5)==i**0.5]
print(a)

def eg2_for(sentence):
    vowels = 'aeiou'
    filtered_list = []
    for l in sentence:
        if l not in vowels:
            filtered_list.append(l)
    return ''.join(filtered_list)

for_loop = eg2_for("This is a test sentence")
print(for_loop)

def eg2_lc(sentence):
    vowels = 'aeiou'
    return ''.join([ l for l in sentence if l not in vowels])

lc_loop = eg2_lc("This is a test sentence")
print(lc_loop)

sentence = 'My name is Aarshay Jain!'
print("FOR-loop result: " + eg2_for(sentence))
print("LC result      : " + eg2_lc(sentence))

# Example 3: Dictionary Comprehension

country = ['India', 'Pakistan', 'Nepal', 'Bhutan', 'China', 'Bangladesh']
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu', 'Beijing', 'Dhaka']

def eg3_for(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    return dic

def eg3_lc(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }

print("FOR-loop result: " + str(eg3_for(country, capital)))
print("LC result      : " + str(eg3_lc(country, capital)))


def prime_num(N):
    return [x for x in range(2, N) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
print(prime_num(20)) 
