import sys
from random import randint

def generate_number_in_file():
    my_file = open(sys.argv[1], "w+")
    numbers = []
    n = int(sys.argv[2])
    for i in range(0, n):
        numbers.append(str(randint(1, n)))

    #numbers = str(numbers)
    my_file.write(' '.join(numbers))
    my_file.close()


def main():
    generate_number_in_file()

if __name__ == '__main__':
    main()
