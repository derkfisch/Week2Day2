# Question 1

l_1 = [1,11,14,5,8,9]

numbers_less_than_ten = []

for l in l_1:
    if l < 10:
        numbers_less_than_ten.append(l)

print(numbers_less_than_ten)

ten_numbers = [l for l in l_1 if l < 10]
print(ten_numbers)

#Question 2

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

names1_comps = [name.upper() if len(name) > 4 else name.remove() for name in names1]
print(names1_comps)
# ???