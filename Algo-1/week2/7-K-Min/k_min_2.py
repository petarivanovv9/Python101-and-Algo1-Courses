import random
import time

# Algorithm :
# QuickSelect:
# Given array A of size n and integer k ≤ n,
# 1. Pick a pivot element p at random from A.
# 2. Split A into subarrays LESS and GREATER by comparing
# each element to p as in Quicksort.
# While we are at it, count the number L of elements going in to LESS.
# 3. (a) If L = k − 1, then output p.
# (b) If L > k − 1, output QuickSelect(LESS, k).
# (c) If L < k − 1, output QuickSelect(GREATER, k − L − 1)


def RandSelect(A, k, length):
    # let r be chosen uniformly at random in the range 1 to length(A)
    n = length - 1
    r = random.randint(0, length - 1)
    A1 = []
    A2 = []
    pivot = A[r]
    # lesser and bigger array
    for i in range(0, n + 1):
        if A[i] < pivot:
            A1.append(A[i])
        if A[i] > pivot:
            A2.append(A[i])
    if k <= len(A1):
        # search in list of small elements
        return RandSelect(A1, k, len(A1))
    if k > len(A) - len(A2):
        # search in the pile of big elements
        return RandSelect(A2, k - (len(A) - len(A2)), len(A2))
    else:
        return pivot

# A = range(1, 1000001)
A = [33, 8, 5, 2, 3, 6, 1, 4, 9, 99]
random.shuffle(A)
length = len(A)
start = time.strftime('%s')
value = RandSelect(A, 9, length)
print value
end = time.strftime('%s')
time = int(end) - int(start)
