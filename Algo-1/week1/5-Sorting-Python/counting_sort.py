# counting sort is an algorithm for sorting a collection of objects according to keys
# that are small integers; that is, it is an integer sorting algorithm.
# It operates by counting the number of objects that have each distinct key value,
# and using arithmetic on those counts to determine the positions of each key value
# in the output sequence. Its running time is linear in the number of items and
# the difference between the maximum and minimum key values, so it is only suitable
# for direct use in situations where the variation in keys is not significantly greater
# than the number of items. However, it is often used as a subroutine in another sorting algorithm,
# radix sort, that can handle larger keys more efficiently


def counting_sort(sequence):
    max_number = max(sequence)

    sorted_array = []
    possible_values_count = max_number + 1
    values_counter = [0] * possible_values_count

    # Making keys
    # Counting the frequency of occurrence of the elements
    for num in sequence:
        values_counter[num] += 1

    # Making the new sorted array
    for i in range(possible_values_count):
        for j in range(values_counter[i]):
            sorted_array += [i]

    return sorted_array


def main():

    sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 500, 500, 500, 321, 21, 11, 1001, 42000, 1000000]

    print(counting_sort(sequence))


if __name__ == '__main__':
    main()
