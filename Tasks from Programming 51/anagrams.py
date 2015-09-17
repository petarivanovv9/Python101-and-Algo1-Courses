class Anagrams:

    @staticmethod
    def are_anagrams(a, b):
        a = a.lower()
        a = list(a)
        a = sorted(a)

        b = b.lower()
        b = list(b)
        b = sorted(b)

        if a is b:
            return True
        else:
            return False


def main():
    word_1 = input()
    word_2 = input()

    if Anagrams.are_anagrams(word_1, word_2) is True:
        print("ANAGRAMS")
    else:
        print("NOT ANAGRAMS")


if __name__ == '__main__':
    main()
