class MinMaxHeap:

    # Checks if a binary tree is a min/max heap.

    @staticmethod
    def is_valid(values, index, level, min_value, max_value):
        if index >= len(values):
            return True

        if (values[index] > min_value and values[index] < max_value) == False:
            return False

        if level % 2 != 0:  # odd
            min_value = values[index]
        else:  # even
            max_value = values[index]

        return (MinMaxHeap.is_valid(values, index * 2 + 1, level + 1, min_value, max_value)
                and MinMaxHeap.is_valid(values, index * 2 + 2, level + 1, min_value, max_value))


def main():

    # "8 71 41 31 10 11 16 46 51 31 21 13" - YES

    # "8 71 41 31 25 11 16 46 51 31 21 13" - NO

    N = int(input("N: "))
    line = input()
    l = line.split()
    values = []

    for number in l:
        values.append(int(number))

    result = MinMaxHeap.is_valid(values, 0, 1, 0, 1e10)

    if result:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
