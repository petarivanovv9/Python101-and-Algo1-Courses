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


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def __getitem__(self, i):
    #     return (self.x, self.y, self.z)[i]

    # def __setitem__(self, index, value):
    #     if index == 0:
    #         self.x = value
    #     elif index == 1:
    #         self.y = value
    #     elif index == 2:
    #         self.z = value
    #     else:
    # pass

    def __getitem__(self, index):
        return getattr(self, ('x', 'y', 'z')[index])

    def __setitem__(self, index, value):
        return setattr(self, ('x', 'y', 'z')[index], value)

    def __str__(self,):
        return str((self.x, self.y, self.z))

    def __len__(self):
        return 3

    def __add__(self, other):
        return Vector(*map(sum, zip(self, other)))


print(40 * '-')


class Spam:

    def __init__(self):
        self.eggs = 'larodi'
        self.__var = 42

    def __getattr__(self, name):
        return name.upper()

    # def __setattr__(self, name, value):
    #     print("Setting {0} to {1}".format(name, value))
    #     return object.__setattr__(self, name.upper(), value + 10)

    # def foo(self):
    #     return 1

    def answer(self):
        return 42

spam = Spam()
spam.eggs = "Eggs"
print(spam.foo)  # FOO
print(spam.bar)  # BAR
print(spam.eggs)  # Eggs
print(spam.answer())  # 42


spam.foo = 1
spam.bar = 2
print(spam.__dict__)  # {'foo': 1, 'bar': 2}
print(spam.__class__)  # <class '__main__.Spam'>
print(spam.__class__ is Spam)  # True


print(40 * '-')


class Base:

    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def report_base(self):
        print("Base:", self.__name, self._age)


class Derived(Base):

    def __init__(self, name, age, derived_name):
        Base.__init__(self, name, age)
        self.__name = derived_name
        self._age = 33

    def report_derived(self):
        print("Derived:", self.__name, self._age)

derived = Derived("John", 0, "Doe")
print(derived.report_base())  # Base: John 33
print(derived.report_derived())  # Derived: Doe 33
print(derived._Base__name, derived._Derived__name)  # John, Doe


# Mixins


class Screen:  # ...
    pass


class RadioTransmitter:  # ...
    pass


class GSMTransmitter(RadioTransmitter):  # ...
    pass


class Input:  # ...
    pass


class MultiTouchInput(Input):  # ...
    pass


class ButtonInput(Input):  # ...
    pass


class MassStorage:  # ...
    pass


class ProcessingUnit:  # ...
    pass


class Phone(ProcessingUnit, Screen, GSMTransmitter,
            MultiTouchInput, ButtonInput, MassStorage):  # ...
    pass


class Tablet(ProcessingUnit, Screen, RadioTransmitter,
             MultiTouchInput, MassStorage):  # ...
    pass
