def sum_of_divisors(n):
    sum_divisors = sum([x for x in range(1, n + 1) if n % x == 0])

    return sum_divisors


def count_of_divisors(n):
    counter_divisors = sum([1 for x in range(1, n + 1) if n % x == 0])

    return counter_divisors


def is_prime(n):

    return n + 1 == sum_of_divisors(n)


def prime_number_of_divisors(n):
    is_prime(count_of_divisors(n))


def to_digits(n):
    digits = [int(x) for x in str(n)]

    return digits


def contains_digit(number, digit):

    return digit in to_digits(number)


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
    return True


def count_digits(n):
    counter_digits = sum([1 for x in to_digits(n)])

    return counter_digits


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def is_number_balanced(n):
    numbs = to_digits(n)

    half = len(numbs) // 2

    left_numbs = numbs[0:half]

    if len(numbs) % 2 == 0:
        right_numbs = numbs[half:]
    else:
        right_numbs = numbs[half + 1:]

    return sum(left_numbs) == sum(right_numbs)


def sum_matrix(matr):
    result = 0

    for row in matr:
        result += sum(row)

    return result


def sum_matrix2(matr):
    # Using list comprehensions
    result = sum([sum(row) for row in matr])

    return result
