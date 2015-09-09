class PhoneBook:
    def __init__(self):
        self.numbers = dict()

    def insert(self, name, number):
        self.numbers[name] = number

    def remove(self, name):
        del self.numbers[name]

    def lookup(self, name):
        if name in self.numbers:
            return self.numbers[name]
        else:
            return 'NOT FOUND'

    def list(self):
        names = list(self.numbers.keys())
        names.sort()
        for name in names:
            print("{} {}".format(name, self.numbers[name]))


def main():
    pass


if __name__ == '__main__':
    main()
