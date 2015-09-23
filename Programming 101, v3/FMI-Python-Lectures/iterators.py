# Iterators - iter

squares = map(lambda x: x ** 2, range(5))
for number in squares:
    print(number)
# 0 1 4 9 16

for number in squares:
    print(number)
# ....


print(40 * '-')


interjections = [
    'Ring-ding-ding-ding-dingeringeding!',
    'Wa-pa-pa-pa-pa-pa-pow!',
    'Hatee-hatee-hatee-ho!',
    'Joff-tchoff-tchoffo-tchoffo-tchoff!'
]

# iterator = iter(interjections)
# while True:
#     interjection = next(iterator)
#     print(interjection)

iterable = iter([1, 2, 3])
print(iter(iterable) is iterable)  # True


print(40 * '-')


class IterableThingie:
    def __getitem__(self, index):
        if index < 10:
            return index * 2
        else:
            raise StopIteration()

it = IterableThingie()
for i in it:
    print(i)
# 0, 2, 4, …, 18


class IterableThingie:
    def __getitem__(self, index):
        if index < 10:
            return index * 2
        else:
            raise StopIteration()

    def __iter__(self):
        return iter('ⰰⰱⰲⰳⰴⰵⰶⰷⰸⰹⰺⰻ')

it = IterableThingie()
for i in it:
    print(i)
# ⰰ, ⰱ, ⰲ, ⰳ, ⰴ, ⰵ, ⰶ, ⰷ, ⰸ, ⰹ, ⰺ, ⰻ


print(40 * '-')


# Стражари и апаши

counter = 0


def clbl():
    # WRITING CODE LIKE THIS WILL LIKELY RESULT
    # IN THE AGONIZING UNTIMELY DEATHS OF MANY
    # CUTE FURRY ANIMALS

    global counter
    counter += 1

    return counter

iterable = iter(clbl, 23)
# [1, 2, 3, …, 22]
for i in iterable:
    print(i)


print(40 * '-')

odd = filter(lambda num: num % 2, range(10))
print(iter(odd) is odd)  # True


print(40 * '-')


loud_names = ['JEFF', 'STONE', 'MIKE', 'EDDIE', 'MATT']
quiet_names = map(lambda name: name.lower(), loud_names)
loud_names[3] = 'VEDDER'

print(list(quiet_names))
# ['jeff', 'stone', 'mike', 'vedder', 'matt']


print(40 * '-')

numbers = [12, 15, 14, 10, 5, 7, 6]
print(numbers.sort())  # None
print(numbers)  # [5, 6, 7, 10, 12, 14, 15]


print(40 * '-')


numbers = [12, 15, 14, 10, 5, 7, 6]
print(sorted(numbers))  # [5, 6, 7, 10, 12, 14, 15]
print(numbers)  # [12, 15, 14, 10, 5, 7, 6]

points = [(10, 3), (4, 8), (5, 9), (2, 3), (12, 6), (7, 4)]
print(sorted(points))
# [(2, 3), (4, 8), (5, 9), (7, 4), (10, 3), (12, 6)]
print(sorted(points, key=lambda point: point[1]))
# [(10, 3), (2, 3), (7, 4), (12, 6), (4, 8), (5, 9)]


print(40 * '-')


numbers = [12, 15, 14, 10, 5, 7, 6]
print(reversed(numbers))
# <list_reverseiterator object at 0x7f14ff534490>
print(numbers.reverse())  # None
