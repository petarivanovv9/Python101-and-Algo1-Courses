# YIELD


def actors_generator():
    yield 'Graham Chapman'
    yield 'John Cleese'
    yield 'Terry Gilliam'
    yield 'Eric Idle'
    yield 'Terry Jones'
    yield 'Michael Palin'

actors = actors_generator()
for actor in actors:
    print(actor + ' as seen on British TV')


print(40 * '-')


# Iterator pattern

class SquaresUpTo:

    def __init__(self, up_to):
        self.up_to = up_to
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.up_to:
            raise StopIteration

        square = self.num ** 2
        self.num += 1

        return square

squares = SquaresUpTo(100)

# for square in squares:
#     print(square)


# with generator


def squares_up_to(number):
    value = 0
    while value <= number:
        yield value ** 2
        value += 1
    raise StopIteration


# Generator expression

squares_up_to_ten = (number ** 2 for number in range(10))


print(40 * '-')


print(all([True, True]))  # True
print(all([True, False]))  # False
print(any([True, False]))  # True


print(40 * '-')

# map and filter


def numbers():
    num = 0
    while True:
        yield num
        num += 1

doulbes = map(lambda num: num * 2, numbers())


print(40 * '-')

# enumerate

exclamations = ['koli', 'besi', 'sechi']
for index, exclamation in enumerate(exclamations):
    print('{0}. {1}!'.format(index, exclamation))


# zip

titles = ['anima', 'Lateralus', '10,000 Days']
positions_US = [2, 1, 1]
positions_UK = [108, 16, 4]
template = 'Tool\'s {0} was at {1} in the US and at {2} in the UK'

for title, us_pos, uk_pos in zip(titles, positions_US, positions_UK):
    print(template.format(title, us_pos, uk_pos))


print(40 * '-')


# itertools.accumulate

from itertools import accumulate

sums = accumulate(range(1, 101), lambda a, b: a + b)
print(sums)
# <itertools.accumulate object at 0x7ff61d24b518>
print(next(sums))  # 1
print(next(sums))  # 3
print(next(sums))  # 6
print(list(sums)[-1])  # 5050


print(40 * '-')


# itertools.chain

from itertools import chain

all_to_15 = chain(range(10), range(11, 15))
print(list(all_to_15))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]


print(40 * '-')


# itertools.compress

from itertools import compress

print(list(compress(range(10), [True, False] * 5)))
# [0, 2, 4, 6, 8]


print(40 * '-')

# itertools.groupby

from itertools import groupby
from collections import defaultdict

data = [('John', 'Tilsit'), ('Eric', 'Cheshire'), ('Michael', 'Camembert'),
        ('Terry', 'Gouda'), ('Terry', 'Port Salut'), ('Michael', 'Edam'),
        ('Eric', 'Ilchester'), ('John', 'Fynbo')]
data = sorted(data, key=lambda record: record[0])
by_owner = defaultdict(list)

for key, group in groupby(data, lambda record: record[0]):
    for record in group:
        by_owner[key].append(record[1])
by_owner['Terry']  # ['Gouda', 'Port Salut']
