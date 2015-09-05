# Returns the number of quadruplets that sum to zero.
# a - [int]
# b - [int]
# d - [int]
# c - [int]


# a + b == -(c + d)
# sort
# binary search


def zero_quadruplets_count(a, b, c, d):
    left_sums = []
    right_sums = []
    result = 0

    for i in a:
        for j in b:
            left_sums.append(i + j)

    for i in c:
        for j in d:
            right_sums.append(i + j)

    for i in left_sums:
        for j in right_sums:
            if i + j == 0:
                result += 1

    return result


def main():

    a = [5, 3, 4]
    b = [-2, -1, 6]
    c = [-1, -2, 4]
    d = [-1, -2, 7]

    print(zero_quadruplets_count(a, b, c, d))


if __name__ == '__main__':
    main()
