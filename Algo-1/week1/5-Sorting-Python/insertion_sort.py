# nsertion sort is a simple sorting algorithm that builds the
# final sorted array (or list) one item at a time.
# It is much less efficient on large lists than more advanced algorithms
# such as quicksort, heapsort, or merge sort.
# However, insertion sort provides several advantages:
# - Simple implementation:
# - Efficient for (quite) small data sets
# - More efficient in practice than most other simple quadratic algorithms
# - Adaptive, i.e., efficient for data sets that are already substantially sorted:
# the time complexity is O(nk) when each element
# in the input is no more than k places away from its sorted position
# - Stable; i.e., does not change the relative order of elements with equal keys
# - In-place; i.e., only requires a constant amount O(1) of additional memory space
# - Online; i.e., can sort a list as it receives it

# When people manually sort cards in a bridge hand, most use a method that is similar to insertion sort.

# Worst case: O(n2) comparisons

# Insertion Sort Algorithm

# Get a list of unsorted numbers
# Set a marker for the sorted section after the first number in the list
# Repeat steps 4 through 6 until the unsorted section is empty
#    Select the first unsorted number
#    Swap this number to the left until it arrives at the correct sorted position
#    Advance the marker to the right one position
# Stop


def insertion_sort(sequence):

    for i in range(1, len(sequence)):
        index = i

        while index > 0 and sequence[index] < sequence[index - 1]:
            sequence[index - 1], sequence[index] = sequence[index], sequence[index - 1]
            index -= 1

    return sequence


def main():

    sequence = [8, 10, 3, 7, 13, 0, -5, 2, 42, 6, 8, 92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10]

    print(insertion_sort(sequence))


if __name__ == '__main__':
    main()
