def compress(iterable, mask):

    index = 0

    while index != len(iterable):
        if mask[index] is True:
            yield iterable[index]
        index += 1


arr_2 = list(compress(["Ivo", "Rado", "Panda"], [True, False, True]))
print(arr_2)
