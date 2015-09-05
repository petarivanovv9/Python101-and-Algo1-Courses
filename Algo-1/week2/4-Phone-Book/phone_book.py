# Find the names of people based on their phone numbers.
# phone_book - [(String, int)]
# numbers - [int]


def lookup_names(phone_book, numbers):
    # sort the phone book by the number
    phone_book.sort(key=lambda element: element[-1])

    result = []

    # make binary search on the numbers in the phone book
    # in order to find the number
    for number in numbers:
        left = 0
        right = len(phone_book) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if phone_book[middle][-1] == number:
                result.append(phone_book[middle][0])
                break
            elif phone_book[middle][-1] < number:
                left = middle + 1
            else:
                right = middle - 1

        if phone_book[middle][-1] != number:
            result.append(None)

    return result


def main():

    phone_book = [("Stanislav", 1), ("Rado", 15), ("Ivan", 6), ("Ivan", 8)]

    numbers = [15, 8, 6, 11, 15]

    print(lookup_names(phone_book, numbers))


if __name__ == '__main__':
    main()
