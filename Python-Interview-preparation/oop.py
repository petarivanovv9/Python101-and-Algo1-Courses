class Stamp:

    def __init__(self, name):
        self.name = name
        self.number = 42

    def __call__(self, something):
        print("{0} was stamped by {1}".format(something, self.name))
        print("number: " + str(self.number))


stamp = Stamp("The government")
stamp("That thing there")  # That thing there was stamped by The government

print(40 * '-')

stamppp = Stamp("The government")
stamp("That thing there")

print(getattr(stamppp, 'number'))

# number = int(input("Enter a number: "))
# setattr(stamppp, 'number', int(input("Enter a number: ")))

print(getattr(stamppp, 'number'))
stamppp("Peshko")


print(40 * '-')


class Countable:
    _count = 0

    def __init__(self, data):
        self.data = data
        type(self).increase_count()

    @classmethod
    def increase_count(cls):
        cls._count += 1

    @classmethod
    def decrease_count(cls):
        cls._count -= 1

    def __del__(self):
        type(self).decrease_count()


print(40 * '-')


class GoatSimulator:
    goats = []

    @staticmethod
    def register(name):
        GoatSimulator.goats.append(name)
        print(len(GoatSimulator.goats), " goats are registered now")


GoatSimulator.register("Pip the Happy Goat")
# 1 goats are registered now
GoatSimulator.register("George the Gutsy Goat")
# 2 goats are registered now


print(40 * '-')

