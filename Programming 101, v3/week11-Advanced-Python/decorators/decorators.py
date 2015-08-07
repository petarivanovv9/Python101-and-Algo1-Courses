from datetime import datetime
from time import time
from functools import wraps


def accepts(*types):
    def accepter(func):
        def decorated(*values):
            for i in range(0, len(types)):
                if type(values[i]) != types[i]:
                    raise TypeError(
                        "Argument {} of {} is not {}!".format(i, func.__name__, types[i].__name__))
            return func(*values)
        return decorated
    return accepter


@accepts(str, int)
def say_hello(name, age):
    return "Hello"


print(say_hello("pesho", 4))

print(20 * '-')


def caesar_encrypt(word, n):

    list_word = list(word)
    size_list_word = len(list_word)

    for i in range(0, size_list_word):
        list_word[i] = modify_letter(list_word[i], n)

    return "".join(list_word)


def modify_letter(c, n):
    if c.isalpha() == False:
        return c

    while n != 0:
        if c == 'z':
            c = 'a'
        elif c == 'Z':
            c = 'A'
        else:
            c = chr(ord(c) + 1)
        n -= 1

    return c


def encrypt(n):
    def accepter(func):
        @wraps(func)
        def decorated():
            return caesar_encrypt(func(), n)
        return decorated
    return accepter


def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorated():
            with open(file_name, "w") as f:
            # with open(file_name, 'a') as f:
                f.write("{} was called and took {} seconds to compleat".format(
                    func.__name__, datetime.now()))
            return func()
        return decorated
    return accepter


def performance(file_name):
    def accepter(func):
        @wraps(func)
        def decorated():
            a = time()
            result = func()
            b = time()
            with open(file_name, 'w') as f:
            # with open(file_name, 'a') as f:
                f.write(
                    "{} was called and took {} seconds to compleat".format(func.__name__, b - a))
            return result
        return decorated
    return accepter


@performance("log.txt")
@encrypt(2)
def get_low():
    return "Get get get low"


a = get_low()
print(get_low())


print(20 * '-')


def memoize(func):
    values = {}

    def helper(x):
        if x not in values:
            values[x] = func(x)
        return values[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(70))
