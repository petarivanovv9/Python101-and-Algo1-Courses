def count_words(words):
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))

print (10 * '-')


def unique_words_count(arr):
    words = []

    for word in arr:
        if word not in words:
            words += [word]

    # unique_words = set(arr)

    return len(words)

print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
print (unique_words_count(["HELLO!"] * 10))

print (10 * '-')


def magic_square(square):

    size_square = len(square)
    is_magic = True

    wanted_sum = 0

    for index in range(0, size_square):
        wanted_sum += square[0][index]

    for row in range(0, size_square):
        current_sum = 0
        for col in range(0, size_square):
            current_sum += square[row][col]
        if current_sum != wanted_sum:
            is_magic = False
            break

    for col in range(0, size_square):
        current_sum = 0
        for row in range(0, size_square):
            current_sum += square[row][col]
        if current_sum != wanted_sum:
            is_magic = False
            break

    current_sum = 0
    row = 0
    col = 0

    while row < size_square and col < size_square:
        current_sum += square[row][col]
        row += 1
        col += 1

    if current_sum != wanted_sum:
        is_magic = False

    current_sum = 0
    row = 0
    col = size_square - 1

    while row < size_square and col >= 0:
        current_sum += square[row][col]
        row += 1
        col -= 1

    if current_sum != wanted_sum:
        is_magic = False

    return is_magic

print (magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print (magic_square([[7, 12, 1, 14],
                     [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

print (10 * '-')


def nan_expand(times):
    result = ""

    while times > 0:
        result += "Not a "
        if times == 1:
            result += "NaN"

        times -= 1

    return result

print (nan_expand(0))
print (nan_expand(1))
print (nan_expand(2))
print (nan_expand(3))

print (10 * '-')


def iterations_of_nan_expand(expanded):
    nan_str = "Not a "

    counter = expanded.count(nan_str, 0, len(expanded))

    if counter == 0 and expanded != "":
        return False

    return counter

print (iterations_of_nan_expand(""))
print (iterations_of_nan_expand("Not a NaN"))
print (iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print (iterations_of_nan_expand("Show these people!"))
print ("Not a NaN        ".strip(''))
print (iterations_of_nan_expand(("Not a NaN        ").strip('')))
print (iterations_of_nan_expand("Not a NaN        "))


print (10 * '-')


def max_consecutive(items):
    counter = 1
    best_counter = 1

    for i in range(0, len(items) - 1):
        if items[i] == items[i + 1]:
            counter += 1
        else:
            if best_counter < counter:
                best_counter = counter
                counter = 1

    return best_counter

print (max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print (max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))

print (10 * '-')


def sum_of_divisors(n):
    sum_divisors = sum([x for x in range(1, n + 1) if n % x == 0])

    return sum_divisors


def is_prime(n):
    if n == 1:
        return False

    return n + 1 == sum_of_divisors(n)


def prime_factorization(n):
    divisors = [x for x in range(1, n + 1) if n %
                x == 0 and is_prime(x) == True]
    result = []

    for divisor in divisors:
        counter = 0
        temp = n
        while temp != 0:
            if temp % divisor == 0:
                counter += 1
            temp = temp / 10

        result += [(divisor, counter)]

    return result

print (prime_factorization(10))
print (prime_factorization(14))
print (prime_factorization(356))
print (prime_factorization(89))
print (prime_factorization(1000))

print (10 * '-')


def prepare_meal(number):
    result = ""
    counter_spam = 0
    temp = number
    while temp != 0:
        if temp % 3 == 0:
            counter_spam += 1
        temp /= 3

    temp_counter_spam = counter_spam

    while counter_spam > 0:
        result += "spam "
        counter_spam -= 1

    if number % 5 == 0 and temp_counter_spam != 0:
        result += "and eggs"
    elif number % 5 == 0:
        result += "eggs"
    else:
        result += ""

    return (result)

print (prepare_meal(5))
print (prepare_meal(3))
print (prepare_meal(27))
print (prepare_meal(15))
print (prepare_meal(45))
print (prepare_meal(7))

print (10 * '-')


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def to_digits(n):

    return [int(x) for x in str(n)]


def is_credit_card_valid(number):
    digits = to_digits(number)

    if odd(len(digits)) == False:
        return False

    transformed_number_list = []

    for i in range(0, len(digits)):
        if even(i):
            transformed_number_list.append(digits[i])
        if odd(i):
            transformed_number_list.append(digits[i] + digits[i])

    if sum(transformed_number_list) % 10 == 0:
        return False
    else:
        return True

print (is_credit_card_valid(79927398713))
print (is_credit_card_valid(79927398715))

print (10 * '-')


def group(arr):
    temp_array = []
    result = []

    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:
            temp_array.append(arr[i])
            if i + 1 == len(arr) - 1:
                temp_array.append(arr[i + 1])
                result += [temp_array]
        else:
            temp_array.append(arr[i])
            result += [temp_array]
            temp_array = []

    return result

print (group([1, 1, 1, 2, 3, 1, 1]))
print (group([1, 2, 1, 2, 3, 3]))

print (10 * '-')


def groupby(func, seq):
    result = {}
    keys = set([func(x) for x in seq])

    for key in keys:
        result.update({key: [x for x in seq if func(x) == key]})

    return result


print (groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
print (groupby(lambda x: 'odd' if x % 2 else 'even',
               [1, 2, 3, 5, 8, 9, 10, 12]))
print (groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

print (10 * '-')


def goldbach(n):
    if odd(n) or n <= 2:
        return False

    result = [(x, n - x)
              for x in range(2, n // 2 + 1) if is_prime(x) and is_prime(n - x)]

    return result

print (goldbach(4))
print (goldbach(6))
print (goldbach(8))
print (goldbach(10))
print (goldbach(100))

print (10 * '-')


def is_an_bn(word):
    if word == "":
        return True
    if len(word) % 2 != 0:
        return False

    counter_a = 0
    counter_b = 0

    for i in range(0, len(word) // 2):
        if word[i] == 'a':
            counter_a += 1
        else:
            return False

    for i in range(len(word) // 2, len(word)):
        if word[i] == 'b':
            counter_b += 1
        else:
            return False

    return counter_a == counter_b

print (is_an_bn(""))
print (is_an_bn("rado"))
print (is_an_bn("aaabb"))
print (is_an_bn("aaabbb"))
print (is_an_bn("aabbaabb"))
print (is_an_bn("bbbaaa"))
print (is_an_bn("aaaaabbbbb"))

print (10 * '-')


def reduce_file_path(path):
    splitted_path = path.split('/')

    while '.' in splitted_path:
        splitted_path.remove('.')

    while '' in splitted_path:
        splitted_path.remove('')

    rev_splitted_path = splitted_path[::-1]
    index = 0

    while index < len(splitted_path):
        if rev_splitted_path[index] == '..':
            rev_splitted_path[index] = '*'
            if index + 1 < len(splitted_path):
                rev_splitted_path[index + 1] = '*'
                index += 1
        index += 1

    while '*' in rev_splitted_path:
        rev_splitted_path.remove('*')

    print ('/' + '/'.join(rev_splitted_path[::-1]))


def reduce_file_path2(path):
    pass

reduce_file_path("/")
reduce_file_path("/srv/../")
reduce_file_path("/srv/www/htdocs/wtf/")
reduce_file_path("/srv/www/htdocs/wtf")
reduce_file_path("/srv/./././././")
reduce_file_path("/etc//wtf/")
reduce_file_path("/etc/../etc/../etc/../")
reduce_file_path("//////////////")
reduce_file_path("/../")


print (10 * '-')


def is_leap_year(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


from dateutil.rrule import *
from datetime import date


def friday_years(start, end):
    friday_years = 0

    # monday - 0, friday - 4, sunday - 6
    start_date = date(start, 1, 1)
    end_date = date(start, 12, 31)

    for year in range(start, end + 1):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        number_fridays = rrule(
            WEEKLY, byweekday=(FR), dtstart=start_date, until=end_date).count()
        if number_fridays == 53:
            friday_years += 1

    return friday_years


print (friday_years(1000, 2000))
print (friday_years(1753, 2000))
print (friday_years(1990, 2015))
