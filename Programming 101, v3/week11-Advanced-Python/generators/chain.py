def chain(iterable_one, iterable_two):

    index = 0

    while index != len(iterable_one):
        yield iterable_one[index]
        index += 1

    index = 0

    while index != len(iterable_two):
        yield iterable_two[index]
        index += 1


arr_2 = list(chain([1, 2, 3, 4], [5, 6, 7]))
print(arr_2)
