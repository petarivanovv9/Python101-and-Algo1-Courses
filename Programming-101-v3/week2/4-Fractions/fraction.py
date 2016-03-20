class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if self.denominator == other.denominator:
            result_numerator = self.numerator + other.numerator
            result_denominator = self.denominator
        else:
            result_numerator = self.numerator * other.denominator + \
                self.denominator * other.numerator
            result_denominator = self.denominator * other.denominator

        return Fraction(result_numerator, result_denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            result_numerator = self.numerator - other.numerator
            result_denominator = self.denominator
        else:
            result_numerator = self.numerator * other.denominator - \
                self.denominator * other.numerator
            result_denominator = self.denominator * other.denominator

        return Fraction(result_numerator, result_denominator)

    def __mul__(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator

        return Fraction(result_numerator, result_denominator)

    def __eq__(self, other):
        if self.denominator == other.denominator:
            return self.numerator == other.numerator
        else:
            self.numerator = self.numerator * other.denominator
            other.numerator = other.numerator * self.denominator
            return self.numerator == other.numerator


def gcd(a, b):
    if a > b:
        return gcd(a - b, b)

    if a < b:
        return gcd(a, b - a)

    if a == b:
        return a

a = Fraction(1, 2)
b = Fraction(2, 4)

c = Fraction(3, 5)
d = Fraction(2, 4)

print (a + b)
print (c + d)
print (10 * '-')
print (a - b)
print (c - d)
print (10 * '-')
print (a * b)
print (c * d)
print (10 * '-')
print (a == b)
print (c == d)
