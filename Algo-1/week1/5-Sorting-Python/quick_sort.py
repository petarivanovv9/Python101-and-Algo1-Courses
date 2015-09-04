# Quicksort (sometimes called partition-exchange sort)
# is an efficient sorting algorithm

# When implemented well, it can be about two or three times faster
# than its main competitors, merge sort and heapsort.

# Quicksort is a comparison sort, meaning that it can sort items of any type
# for which a "less-than" relation (formally, a total order) is defined.
# In efficient implementations it is not a stable sort,
# meaning that the relative order of equal sort items is not preserved.
# Quicksort can operate in-place on an array, requiring small additional
# amounts of memory to perform the sorting.
# Mathematical analysis of quicksort shows that, on average, the algorithm
# takes O(n log n) comparisons to sort n items. In the worst case, it makes O(n2) comparisons,
# though this behavior is rare.

# The steps are:
# 1) Pick an element, called a pivot, from the array.
# 2) Reorder the array so that all elements with values less than the pivot
# come before the pivot, while all elements with values greater than
# the pivot come after it (equal values can go either way).
# After this partitioning, the pivot is in its final position.
# This is called the partition operation.
# 3) Recursively apply the above steps to the sub-array of elements
# with smaller values and separately to the sub-array of elements with greater values.


def quick_sort(sequence):
    sorted_sequence = []

    if len(sequence) < 2:
        return sequence

    sequence_len = len(sequence)
    pivot = sequence.pop(sequence_len // 2)
    sequence.insert(sequence_len, pivot)
    i = 0

    for elem in sequence:
        if sequence[i] > pivot:
            sequence.insert(sequence_len, sequence[i])
            del sequence[i]
        else:
            i += 1

    first_seq = quick_sort(sequence[:sequence.index(pivot)])
    second_seq = quick_sort(sequence[sequence.index(pivot) + 1:])

    for i in first_seq:
        sorted_sequence.append(i)

    sorted_sequence.append(pivot)

    for i in second_seq:
        sorted_sequence.append(i)

    return sorted_sequence


def main():

    sequence = [8, 10, 3, 7, 13, 0, -5, 2, 42, 6, 8, 92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10, 1000000]

    print(quick_sort(sequence))


if __name__ == '__main__':
    main()
