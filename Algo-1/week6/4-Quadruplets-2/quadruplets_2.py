class Quadruplets_2:

    # Returns the number of quadruplets that sum to zero.
    # a - [int]
    # b - [int]
    # c - [int]
    # d - [int]

    @staticmethod
    def zero_quadruplets_count(a, b, c, d):
        left_sums = {}
        right_sums = {}
        counter = 0

        for elem1 in a:
            for elem2 in b:
                if elem1 + elem2 not in left_sums:
                    left_sums[elem1 + elem2] = 1
                else:
                    left_sums[elem1 + elem2] += 1

        for elem1 in c:
            for elem2 in d:
                if elem1 + elem2 not in right_sums:
                    right_sums[elem1 + elem2] = 1
                else:
                    right_sums[elem1 + elem2] += 1

        for key in left_sums:
            if -key in right_sums:
                counter = counter + (left_sums[key] * right_sums[-key])

        return counter


def main():

    a = [5, 3, 4]
    b = [-2, -1, 6]
    c = [-1, -2, 4]
    d = [-1, -2, 7]

    print(Quadruplets_2.zero_quadruplets_count(a, b, c, d))


if __name__ == '__main__':
    main()
