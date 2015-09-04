# It has O(n2) time complexity, making it inefficient on large lists,
# and generally performs worse than the similar insertion sort.

# The algorithm divides the input list into two parts: the sublist of items already sorted,
# which is built up from left to right at the front (left) of the list,
# and the sublist of items remaining to be sorted that occupy the rest of the list.
# Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
# The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element
# in the unsorted sublist, exchanging (swapping) it with the leftmost
# unsorted element (putting it in sorted order),
# and moving the sublist boundaries one element to the right.

# Selection Sort Algorithm

# Get a list of unsorted numbers
# Set a marker for the unsorted section at the front of the list
# Repeat steps 4 - 6 until one number remains in the unsorted section
#    Compare all unsorted numbers in order to select the smallest one
#    Swap this number with the first number in the unsorted section
#    Advance the marker to the right one position
# Stop


def selection_sort(sequence):

    for i in range(0, len(sequence)):
        min_element = min(sequence[i:])
        temp = sequence[i]
        min_element_indx = sequence[i:].index(min_element) + i
        sequence[i] = min_element
        sequence[min_element_indx] = temp

    return sequence


def selection_sort_2(sequence):

    for i in range(0, len(sequence)):
        min_element_indx = i

        for j in range(i, len(sequence)):
            if sequence[j] < sequence[min_element_indx]:
                min_element_indx = j

        if sequence[min_element_indx] < sequence[i]:
            temp = sequence[i]
            sequence[i] = sequence[min_element_indx]
            sequence[min_element_indx] = temp

    return sequence


def main():
    sequence = [92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10, -1]

    print(selection_sort(sequence))

    print(selection_sort_2(sequence))


if __name__ == '__main__':
    main()
