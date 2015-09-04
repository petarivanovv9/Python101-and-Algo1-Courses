# An O(n log n) comparison-based sorting algorithm.
# Most implementations produce a stable sort, which means that the
# implementation preserves the input order of equal elements
# in the sorted output.
# Mergesort is a divide and conquer algorithm

# Conceptually, a merge sort works as follows:
# 1) Divide the unsorted list into n sublists,
# each containing 1 element (a list of 1 element is considered sorted).
# 2) Repeatedly merge sublists to produce new sorted sublists until
# there is only 1 sublist remaining. This will be the sorted list.


# one of mergesort’s most attractive properties is
# that it guarantees to sort any array of N items in
# time proportional to N log N. Its prime
# disadvantage is that it uses extra space proportional to N.


def merge_sort(sequence):

    if len(sequence) > 1:
        sorted_sequence = []

        # print("cak")
        left_half = merge_sort(sequence[:len(sequence) // 2])
        print("hop")
        right_half = merge_sort(sequence[len(sequence) // 2:])
        # print("bam")

        left_index = 0
        right_index = 0

        while len(sequence) != len(sorted_sequence):

            if len(left_half) > left_index and len(right_half) > right_index:

                if left_half[left_index] <= right_half[right_index]:
                    sorted_sequence.append(left_half[left_index])
                    left_index += 1

                elif left_half[left_index] > right_half[right_index]:
                    sorted_sequence.append(right_half[right_index])
                    right_index += 1

            elif len(left_half) == left_index:
                sorted_sequence.append(right_half[right_index])
                right_index += 1

            elif len(right_half) == right_index:
                sorted_sequence.append(left_half[left_index])
                left_index += 1

        return sorted_sequence

    else:
        # print("tuka sum")
        return sequence


def main():

    # sequence = [8, 10, 3, 7, 13, 0, -5, 2, 42, 6, 8, 92, 34, 67, 43, 78, 65, 43, 3, 23, 98, 10, 1000000]
    sequence = [7, 2, 11, 15, 3, 0, 2]

    print(merge_sort(sequence))


if __name__ == '__main__':
    main()
