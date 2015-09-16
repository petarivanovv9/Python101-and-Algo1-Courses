def make_letter_dict(word):
    result = {}
    word = list(word)

    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    return result


def main():
    word = input()

    n = int(input())

    counter = 0

    word_dict = make_letter_dict(word)

    while n != 0:
        n -= 1

        temp = str(input())

        if len(word) != len(temp):
            continue

        temp_dict = make_letter_dict(temp)

        if word_dict == temp_dict:
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
