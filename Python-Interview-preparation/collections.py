foods = ['spam', 'eggs', 'ham']
things = foods
things[1] = 'chips'
print(foods[1])  # 'chips'
print(foods)  # ['spam', 'chips', 'ham']
print(things)  # ['spam', 'chips', 'ham']

print(40 * '-')

a = ['spam', 'eggs', 'ham']
b = a
c = a[:]
print(a is b, a is c)  # (True, False)
print(a == b, a == c)  # (True, True)
b[1] = 'milk'
print(a is b, a is c)  # (True, False)
print(a == b, a == c)  # (True, False)

print(40 * '-')

my_string = '1234567890'
print(my_string[9])

print(40 * '-')

my_data = set(range(15))
print(my_data)

for x in my_data:
    print(x)
    break

print(40 * '-')


