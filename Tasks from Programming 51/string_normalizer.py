class StringNormalizer:

    @staticmethod
    def normalize_string(string):
        string = string.lower()
        words = string.split()

        result = []
        temp = ""

        for word in words:
            temp += word[0].upper()
            temp += word[1:]
            result.append(temp)
            temp = ""

        return " ".join(result)


def main():
    string = input()

    print(StringNormalizer.normalize_string(string))


if __name__ == '__main__':
    main()
