import sys


def sum_numbers():
    my_file = open(sys.argv[1], "r")
    numbers = my_file.read().split(' ')
    numbers_int = [int(x) for x in numbers]
    sum_numbers = sum(numbers_int)
    my_file.close()
    return sum_numbers


def main():
    print (sum_numbers())

if __name__ == '__main__':
    main()
