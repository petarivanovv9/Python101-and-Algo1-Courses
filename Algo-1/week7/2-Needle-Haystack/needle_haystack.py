class NeedleHaystack:
    # d - length of alphabet
    # q - some prime number

    @staticmethod
    def Rabin_Karp_Matcher(text, pattern, d, q, result):
        n = len(text)
        m = len(pattern)
        h = 1
        p = 0
        t = 0

        for i in range(1, m):
            h = (h * d) % q

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        for s in range(n - m + 1):
            if p == t:
                if pattern == text[s:s + m]:
                    result.append(s)

            if s < n - m:
                t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q


def main():
    # text = 'thequickbrownfoxjumpsoverthelazydogthedogwasnotamused'
    text = str(input())
    # pattern = 'dog'
    pattern = str(input())
    result = list()
    NeedleHaystack.Rabin_Karp_Matcher(text, pattern, 256, 101, result)
    # print(result)

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
