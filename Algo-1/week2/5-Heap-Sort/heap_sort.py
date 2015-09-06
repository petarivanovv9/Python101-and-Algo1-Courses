# Heapsort is a comparison-based sorting algorithm.
# Heapsort can be thought of as an improved selection sort:
# like that algorithm, it divides its input into a sorted and an unsorted region,
# and it iteratively shrinks the unsorted region by extracting the largest element
# and moving that to the sorted region. The improvement consists of the use of
# a heap data structure rather than a linear-time search to find the maximum.

# Although somewhat slower in practice on most machines than
# a well-implemented quicksort, it has the advantage of a more
# favorable worst-case O(n log n) runtime. Heapsort is an in-place algorithm,
# but it is not a stable sort.

# Worst case: O(nlogn)


def get_left_child(i, size):
    if 2 * i + 1 >= size:
        return None
    return 2 * i + 1


def get_right_child(i, size):
    if 2 * i + 2 >= size:
        return None
    return 2 * i + 2


def get_parent(i):
    if i == 0:
        return None
    return (i - 1) // 2


def swap(sequence, i, j):
    temp = sequence[i]
    sequence[i] = sequence[j]
    sequence[j] = temp


def make_min_heap(sequence, end_index):
    index = end_index

    while index >= 0:
        heapify(sequence, index, end_index)
        index -= 1

    return sequence


def heapify(sequence, start, lenght):
    while get_left_child(start, lenght) is not None:
        left_child = get_left_child(start, lenght)
        right_child = get_right_child(start, lenght)
        min_child = None

        if right_child is None or sequence[left_child] < sequence[right_child]:
            min_child = left_child
        else:
            min_child = right_child

        if sequence[start] > sequence[min_child]:
            swap(sequence, start, min_child)

        start = min_child


# Sorts a sequence of integers.
def heap_sort(sequence):
    sequence = sequence[:]
    sorted_sequence = []

    for i in range(len(sequence)):
        make_min_heap(sequence, len(sequence) - i)
        sorted_sequence.append(sequence[0])
        swap(sequence, 0, len(sequence) - i - 1)

    return sorted_sequence


def main():

    sequence = [8, 10, 3, 7, 13, 0, -5, 2, 42, 6, 8, 92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10, 1000000]
    # sequence = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(heap_sort(sequence))


if __name__ == '__main__':
    main()
