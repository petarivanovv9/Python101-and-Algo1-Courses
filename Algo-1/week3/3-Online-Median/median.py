# This module provides an implementation of the heap queue algorithm,
# also known as the priority queue algorithm.
# heap[0] is the smallest item,
import heapq


# For <, __lt__ is used. For >, __gt__.
# For <= and >=, __le__ and __ge__ respectively.

# a wrapper class that takes a comparable type and reverses the < comparison
class ReverseLess:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

# A median of the collection is the element
# which stays on position ceiling((Length-1)/2)
# in the zero-based sorted list of the items.


class Median:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def add_to_left_heap(self, value):
        heapq.heappush(self.left_heap, ReverseLess(value))

    def remove_from_left_heap(self):
        return heapq.heappop(self.left_heap).value

    def median(self):
        return self.left_heap[0].value

    # inserts the number and returns the median
    def insert(self, number):

        if len(self.left_heap) == 0:
            self.add_to_left_heap(number)
        else:
            if self.median() >= number:
                self.add_to_left_heap(number)
                if len(self.left_heap) == len(self.right_heap) + 3:
                    a = self.remove_from_left_heap()
                    heapq.heappush(self.right_heap, a)
            else:
                heapq.heappush(self.right_heap, number)
                if len(self.left_heap) == len(self.right_heap):
                    a = heapq.heappop(self.right_heap)
                    self.add_to_left_heap(a)

        return self.median()


def main():

    # N = int(input())
    numbers = [int(item) for item in input().split()]

    # numbers = [5, 3, 4]

    result = Median()
    print(numbers)

    for number in numbers:
        print(result.insert(number))


if __name__ == '__main__':
    main()
