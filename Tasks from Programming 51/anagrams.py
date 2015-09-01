def main():
    word_1 = input()
    word_1 = word_1.lower()
    word_1 = list(word_1)
    # print(word_1)
    # word_1.sort()
    # print(word_1)
    word_2 = input()
    word_2 = word_2.lower()
    word_2 = list(word_2)
    # print(word_2)
    # word_2.sort()
    # print(word_2)

    if word_1 == word_2:
        print("ANAGRAMS")
    else:
        print("NOT ANAGRAMS")


if __name__ == '__main__':
    main()
