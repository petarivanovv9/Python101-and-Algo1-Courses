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

iterator = iter(interjections)
while True:
    interjection = next(iterator)
    print(interjection)

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
