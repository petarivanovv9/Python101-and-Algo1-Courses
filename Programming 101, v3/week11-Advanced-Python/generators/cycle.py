def cycle(iterable):

    index = 0
    while True:
        yield iterable[index]
        index += 1
        if index == len(iterable):
            index = 0


endless = cycle([1, 2, 3])
for item in endless:
    print(item)
