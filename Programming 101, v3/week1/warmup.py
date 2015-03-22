def factorial(n):
    if n == 0 or n == 1:
        return 1

    counter = 1
    result = 1

    while counter <= n:
        result *= counter
        counter += 1

    return result

print (factorial(0))
print (factorial(1))
print (factorial(5))

print (10 * '-')


def fibonacci(n):

    if n == 1:
        return [1]

    result = [1, 1]

    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])

    return result


print (fibonacci(1))
print (fibonacci(2))
print (fibonacci(3))
print (fibonacci(10))

print (10 * '-')


def sum_of_digits(n):
    n = abs(n)

    result = 0

    while n != 0:
        result += n % 10
        n = n // 10

    return result

print (sum_of_digits(1325132435356))
print (sum_of_digits(123))
print (sum_of_digits(6))
print (sum_of_digits(-10))

print (10 * '-')


def fact_digits(n):
    result = 0

    while n != 0:
        result += factorial(n % 10)
        n = n // 10

    return result

print (fact_digits(111))
print (fact_digits(145))
print (fact_digits(999))

print (10 * '-')


def palindrome(obj):

    is_palindrome = True
    obj = str(obj)

    obj_list = list(obj)

    obj_list_reverse = obj_list[::-1]

    return obj_list == obj_list_reverse

print (palindrome(121))
print (palindrome("kapak"))
print (palindrome("baba"))

print (10 * '-')


def to_digits(n):
    result = []

    while n != 0:
        result += [n % 10]
        n = n // 10

    result = result[::-1]
    return result

print (to_digits(123))
print (to_digits(99999))
print (to_digits(123023))

print (10 * '-')


def to_number(digits):
    number = 0

    for digit in digits:
        number = number * 10 + digit

    return number

print (to_number([1, 2, 3]))
print (to_number([9, 9, 9, 9, 9]))
print (to_number([1, 2, 3, 0, 2, 3]))

print (10 * '-')


def fib_number(n):

    result_str = ""
    result = fibonacci(n)

    for item in result:
        result_str += str(item)

    return result_str

print (fib_number(3))
print (fib_number(10))

print (10 * '-')


def count_vowels(text):
    counter = 0
    vowels = "aeiouyAEIOUY"

    for c in text:
        if c in vowels:
            counter += 1

    return counter

print (count_vowels("Python"))
print (count_vowels("Theistareykjarbunga"))
print (count_vowels("grrrrgh!"))
print (count_vowels(
    "Github is the second best thing that happend to programmers, after the keyboard!"))
print (count_vowels("A nice day to code!"))
print (count_vowels("aei    dsa!!1!ouy"))

print (10 * '-')


def count_consonants(text):
    counter = 0
    consonants = "bcdfghjklmnpqrstvwxz"

    for i in range(0, len(text)):
        if text[i].lower() in consonants:
            counter += 1

    return counter

print (count_consonants("Python"))
print (count_consonants("Theistareykjarbunga"))
print (count_consonants("grrrrgh!"))
print (count_consonants(
    "Github is the second best thing that happend to programmers, after the keyboard!"))
print (count_consonants("A nice day to code!"))

print (10 * '-')


def char_histogram(string):
    histogram = {}

    string_list = list(string)

    for item in string_list:
        if item in histogram:
            histogram[item] += 1
        else:
            histogram[item] = 1

    return histogram

print (char_histogram("Python!"))
print (char_histogram("AAAAaaa!!!"))

print (10 * '-')


def p_score(n):

    if palindrome(n):
        return 1

    n_reversed = str(n)
    n_reversed = n_reversed[::-1]

    result = n + int(n_reversed)

    return 1 + p_score(result)

print (p_score(121))
print (p_score(48))
print (p_score(198))

print (10 * '-')


def is_increasing(seq):

    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            return False

    return True

print (is_increasing([1, 2, 3, 4, 5]))
print (is_increasing([1]))
print (is_increasing([5, 6, -10]))
print (is_increasing([1, 1, 1, 1]))

print (10 * '-')


def is_decreasing(seq):

    for i in range(1, len(seq)):
        if seq[i] >= seq[i - 1]:
            return False

    return True

print (is_decreasing([5, 4, 3, 2, 1]))
print (is_decreasing([1, 2, 3]))
print (is_decreasing([100, 50, 20]))
print (is_decreasing([1, 1, 1, 1]))

print (10 * '-')


def is_hack_number(n):
    n_bin = bin(n)
    n_bin_list = list(n_bin)
    n_bin_list = n_bin_list[2:]
    n_bin_list_reversed = n_bin_list[::-1]

    is_palindrome = False

    if n_bin_list == n_bin_list_reversed:
        is_palindrome = True

    is_hack_num = False
    sum_of_one_n = 0

    for i in range(0, len(n_bin_list)):
        if n_bin_list[i] == '1':
            sum_of_one_n += 1

    if sum_of_one_n % 2 != 0 and is_palindrome == True:
        is_hack_num = True

    return is_hack_num


def next_hack(n):
    n += 1

    next_hack = False
    result = 0

    while next_hack != True:
        if is_hack_number(n) == True:
            result = n
            next_hack = True
        else:
            n += 1

    return result

print (next_hack(0))
print (next_hack(7))
print (next_hack(10))
print (next_hack(8031))
