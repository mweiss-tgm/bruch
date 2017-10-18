import math

class Bruch(object):
    """
    Representing a fraction
    """
    def __init__(self, *args):
        """
        Initialises a fraction
        :param args: multiple arguments as "int", "int,int", "fraction"
        """
        if len(args) is 1:
            x = args[0]
            if isinstance(x, Bruch):
                self.zaehler = x.zaehler
                self.nenner = x.nenner
            elif isinstance(x, int):
                self.zaehler = x
                self.nenner = 1
            else:
                raise TypeError()

        if len(args) is 2:
            self.nenner = args[1]
            self.zaehler = args[0]

        if self.nenner is 0:
            raise ZeroDivisionError()
        elif isinstance(self.zaehler, float) or isinstance(self.nenner, float):
            raise TypeError()

    def __float__(self):
        """
        Converts to a float
        :return: the float of this fraction
        """
        return float(self.zaehler / self.nenner)

    def __int__(self):
        """
        Converts to an int
        :return: the int of this fraction
        """
        return int(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Converts to a complex number
        :return: the complex number of the fraction
        """
        return complex(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Inverts the numerator and the denominator
        :return: An inverted fraction
        """
        return Bruch(self.nenner, self.zaehler)

    def __pow__(self, power, modulo=None):
        """
        Powers the fraction by power
        :param power: to which the fraction is powered
        :param modulo: NONE
        :return: fraction raised to power
        """
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError()

    @staticmethod
    def __makeBruch(value):
        """
        Creates a fraction with a value
        :param value: either a Intger or a fraction
        :return: a fraction
        """
        return Bruch(value)

    def __abs__(self):
        """
        Absolute value of this fraction
        :return: absolute value
        """
        return abs(float(self))

    def __neg__(self):
        """
        Negates the fraction
        :return: a negated fraction
        """
        return Bruch(-self.zaehler, self.nenner)

    def __eq__(self, other):
        """
        Checks if self equals other
        :param other: object implementing float
        :return: True or False
        """
        return (float(self) == float(other))

    def __ge__(self, other):
        """
        Checks whether self is greater than other or self is equal to other
        :param other: object implementing float
        :return: True or False
        """
        return (float(self) >= float(other))

    def __le__(self, other):
        """
        Checks whether other is greater than self or other is equal to self
        :param other: object implementing float
        :return: True or False
        """
        return (float(self) <= float(other))

    def __gt__(self, other):
        """
        Checks if self is greater than other
        :param other: object implementing float
        :return: True or False
        """
        return (float(self) > float(other))

    def __lt__(self, other):
        """
        Checks if other is greater than self
        :param other: object implementing float
        :return: True or False
        """
        return (float(self) < float(other))

    def __str__(self):
        """
        String of the fraction
        :return: fraction as a string
        """
        return "({0}{1})".format(abs(self.zaehler), "/" + str(abs(self.nenner)))

    @staticmethod
    def __add(a, b):
        """
        Add two fractions by finding the least common denominator
        :param a: a fraction
        :param b: a fraction
        :return: a fraction with the same denominator
        """
        try:
            numerator = a.zaehler + b.zaehler
            denominator = math.gcd(a.nenner, b.nenner)
            return Bruch(numerator, denominator)
        except NameError:
            print("Methods are not defined!")

    def __add__(self, other):
        """
        Adds two fractions
        :param other: a fraction
        :return: a fraction
        """
        other = Bruch(other)
        return Bruch.__add(self, other)

    def __radd__(self, other):
        """
        reflected add
        :param other: a fraction
        :return: a fraction
        """
        return self + other

    def __iadd__(self, other):
        """
        see __add__()
        :param other: a fraction
        :return: a fraction
        """
        return other + self

    def __sub__(self, other):
        """
        Subtracts other from self
        :param other: a fraction
        :return: a fraction
        """
        other = -Bruch(other)
        return Bruch.__add(self, other)

    def __rsub__(self, other):
        """
        see __sub__()
        :param other: a fraction
        :return: a fraction
        """
        return -self + other

    def __isub__(self, other):
        """
        see __sub__()
        :param other:
        :return:
        """
        return self - other

    def __mul__(self, other):
        """
        Multiplies self with other
        :param other: a fraction
        :return: a fraction
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __rmul__(self, other):
        """
        see __mul__()
        :param other: a fraction
        :return: a fraction
        """
        return self * other

    def __imul__(self, other):
        """
        see __mul__()
        :param other: a fraction
        :return: a fraction
        """
        return self * other

    def __truediv__(self, other):
        """
        Divides self by other, using an inverted fraction
        :param other: a fraction
        :return: a fraction
        """
        other = Bruch(other)
        return self * ~other

    def __rtruediv__(self, other):
        """
        see __truediv__()
        :param other: a fraction
        :return: a fraction
        """
        return Bruch.__truediv__(other, self)

    def __itruediv__(self, other):
        """
        see __truediv__()
        :param other: a fraction
        :return: a fraction
        """
        return self / other

    def __iter__(self):
        """
        iterates the fraction
        :return: an iterator
        """
        return iter([self.zaehler, self.nenner])