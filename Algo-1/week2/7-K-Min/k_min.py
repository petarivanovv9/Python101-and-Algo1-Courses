class KMin:

    # Quick sort

    @staticmethod
    def swap(numbers, i, j):
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp

    # The last element is a pivot, all smaller elements are to left of it
    # and greater elements to right
    @staticmethod
    def partition(numbers, l, r):
        x = numbers[r]
        i = l

        for j in range(l, r):
            if numbers[j] <= x:
                KMin.swap(numbers, i, j)
                i += 1

        KMin.swap(numbers, i, r)

        return i

    @staticmethod
    def kthSmallest(numbers, l, r, k):
        if k > 0 and k <= r - l + 1:
            pos = KMin.partition(numbers, l, r)

            if pos - l == k - 1:
                return numbers[pos]

            if pos - l > k - 1:
                return KMin.kthSmallest(numbers, l, pos - 1, k)

            return KMin.kthSmallest(numbers, pos + 1, r, k - pos + l - 1)

    # Finds the k-th minimum element in an unsorted collection.
    # numbers - [int]
    # k - int
    @staticmethod
    def kthMinimum(numbers, k):
        return KMin.kthSmallest(numbers, 0, len(numbers) - 1, k)


def main():

    numbers = [33, 8, 5, 2, 3, 6, 1, 4, 9, 99]

    for i in range(1, len(numbers) + 1):
        print(KMin.kthMinimum(numbers, i))

if __name__ == '__main__':
    main()
