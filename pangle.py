#
# pangle
#

from skyfield.units import Angle # type: ignore

from signs import Sign, Signs
import unittest

class Polar:
    deg_: int
    min_: int

    def __init__(self, deg: int, min: int):
        if deg < 0 or deg > 359:
            raise ValueError("Input must be [0-360)")
        if min < 0 or min > 59:
            raise ValueError("Minutes must be [0-60)")
        self.deg_ = deg
        self.min_ = min

    def from_minutes(self, min: int):
        deg = (min // 60) % 360
        min = min % 60
        return Polar(deg, min)

    def __add__(self, other):
        if isinstance(other, Polar):
            x = self.to_minutes() + other.to_minutes()
        elif isinstance(other, int):
            x = self.to_minutes() + other * 60
        else: 
            raise TypeError("Argument must be an instance of int or Polar")
        return self.from_minutes(x)

    def __sub__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        n = self.to_minutes() - other.to_minutes()
        return self.from_minutes(n)

    def __mul__(self, n):
        m = self.to_minutes() * n
        return self.from_minutes(m)

    def __eq__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        return  self.deg_ == other.deg_ and self.min_ == other.min_

    def __ge__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        return self.to_minutes() >= other.to_minutes()

    def __gt__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        return self.to_minutes() > other.to_minutes()

    def __le__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        return self.to_minutes() <= other.to_minutes()

    def __lt__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        return self.to_minutes() < other.to_minutes()

    def to_minutes(self) -> int:
        return self.deg_ * 60 + self.min_
    
    def to_decimal(self) -> float:
        return float(((self.deg_ * 60) + self.min_) / 60.0)

    def diff(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        n = abs(self.to_minutes() - other.to_minutes())
        return self.from_minutes(n)

    def print(self):
        print(f"{self.deg_}° {self.min_}'")

class TestPolar(unittest.TestCase):
    def test_polar():
        p1 = Polar(55, 23)
        assert p1.to_minutes() == 3323
        p2 = Polar(10, 23)
        assert p1 > p2 and p1 >= p2
        assert p2 < p1 and p2 <= p1
        r = p1 + p2
        assert r >= p1 + p2 and r <= p1 + p2
        assert r == Polar(65, 46)
        r = p1 - p2
        assert r == Polar(45, 0)
        assert Polar(330, 0).diff(Polar(350, 0)) == Polar(20, 0)
        assert Polar(10, 0).diff(Polar(187, 13)) == Polar(177, 13)
        assert r == Polar(45, 0)
        r = (p1 - p2) * 2 
        assert r == Polar(90, 0)
        print("TestPolar...[ok]")
class Ecliptic:
    deg_: int
    sign_: Sign
    min_: int

    def __init__(self, deg: int, sign: Sign, min: int):
        if deg < 0 or deg > 29:
            raise ValueError("Degrees must be [0-30)")
        if sign == None:
            raise ValueError("Enter a valid sign")
        if min < 0 or min > 59:
            raise ValueError("Minutes must be [0-60)")
        self.deg_ = deg
        self.sign_ = sign
        self.min_ = min

    def from_polar(self, polar: Polar):
        self.sign: Sign = Signs.get_sign_from_degree(Signs, polar.deg_)
        self.deg_ = self.sign.degrees_ - polar.deg_
        self.min_ = polar.min_

    def from_angle(self, angle: Angle):
        deg = int(angle.degrees)
        min = round((angle.degrees - deg) * 60)
        return to_ecliptic(Polar(deg, min))
    
    def from_float(self, num: float):
        deg = int(num)
        min = round((num - deg) * 60)
        return to_ecliptic(Polar(deg, min))

    def from_minutes(self, min: int):
        deg = (min // 60) % 360
        min = min % 60
        sign: Sign = Signs.get_sign_from_degree(Signs, deg)
        deg = deg - sign.degrees_
        return Ecliptic(deg, sign, min)

    def __add__(self, other):
        if isinstance(other, Ecliptic):
            x = self.to_minutes() + other.to_minutes()
        elif isinstance(other, int):
            x = self.to_minutes() + other * 60
        else: 
            raise TypeError("Argument must be an instance of int or Ecliptic")
        return self.from_minutes(x)

    def __sub__(self, other):
        if isinstance(other, Ecliptic):
            x = self.to_minutes() - other.to_minutes()
        elif isinstance(other, int):
            x = self.to_minutes() - other * 60
        else: 
            raise TypeError("Argument must be an instance of int or Ecliptic")
        return self.from_minutes(x)

    def __mul__(self, n):
        m = self.to_minutes() * n
        return self.from_minutes(m)

    def __eq__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        return self.deg_ == other.deg_ and \
            self.sign_ == other.sign_ and \
            self.min_ == other.min_

    def __ge__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        return self.to_minutes() >= other.to_minutes()

    def __gt__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        return self.to_minutes() > other.to_minutes()

    def __le__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        return self.to_minutes() <= other.to_minutes()

    def __lt__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        return self.to_minutes() < other.to_minutes()

    def to_minutes(self) -> int:
        return (self.deg_ + self.sign_.degrees_) * 60 + self.min_

    def to_decimal(self) -> float:
        deg = self.deg_ + self.sign_.degrees_
        decimal_min: float = self.min_ * 100.0 / 60.0
        return float(deg + decimal_min)

    def diff(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        x = abs(self.to_minutes() - other.to_minutes())
        return self.from_minutes(x)

    def print(self):
        print(f"{self.deg_}° {self.sign_.name_} {self.min_}'")

class TestEcliptic(unittest.TestCase):
    def test_ecliptic():
        e1 = Ecliptic(25, Signs.taurus_, 23)
        assert e1.to_minutes() == 3323
        e2 = Ecliptic(10, Signs.aries_, 23)
        assert e1 > e2 and e1 >= e2
        assert e2 < e1 and e2 <= e1
        r = e1 + e2
        assert r >= e1 + e2 and r <= e1 + e2
        assert r == Ecliptic(5, Signs.gemini_, 46)
        r = e1 - e2
        assert r == Ecliptic(15, Signs.taurus_, 0)
        assert Ecliptic(0, Signs.pisces_, 0).diff(Ecliptic(20, Signs.pisces_, 0)) == Ecliptic(20, Signs.aries_, 0)
        assert Ecliptic(10, Signs.aries_, 0).diff(Ecliptic(7, Signs.libra_, 13)) == Ecliptic(27, Signs.virgo_, 13)
        r = (e1 - e2) * 2
        assert r == Ecliptic(0, Signs.cancer_, 0)
        print("TestEcliptic...[ok]")

# Utilities for conversions

def to_ecliptic(p: Polar) -> Ecliptic:
    sign: Sign = Signs.get_sign_from_degree(Signs, p.deg_)
    deg = p.deg_ - sign.degrees_
    min = p.min_
    return Ecliptic(deg, sign, min)

def to_polar(e: Ecliptic) -> Polar:
    deg = e.deg_ + e.sign_.degrees_
    min = e.min_
    return Polar(deg, min)

def test_utilities():
    # Test utilities for conversions
    p1 = Polar(55, 23)
    e1 = Ecliptic(25, Signs.taurus_, 23)
    assert to_ecliptic(p1) == e1
    assert to_polar(e1) == p1
    print("TestUtilities...[ok]")

# Utilities for user input

def get_polar(prompt):
    while True:
        try:
            user_input = input(prompt)
            deg, min = map(float, user_input.split())
            if deg < 0 or deg > 359:
                print("Degrees must be [0-360)")
            elif min < 0 or min > 59:
                print("Minutes must be [0-60)")
            else:
                return Polar(deg, min)
        except ValueError:
            print("Invalid input! Please enter two valid numbers separated by a space.")

def get_ecliptic(prompt):
    while True:
        try:
            user_input = input(prompt)
            deg_str, s, min_str = map(str, user_input.split())
            deg = int(deg_str)
            min = int(min_str)
            sign = Signs.get(Signs, s)
            if deg < 0 or deg > 29:
                print("Degrees must be [0-30)")
            elif sign == None:
                print("Enter a valid sign")
            elif min < 0 or min > 59:
                print("Minutes must be [0-60)")
            else:
                return Ecliptic(deg, sign, min)
        except ValueError:
            print("Invalid input! Please enter number-sign-number separated by a spaces.")

if __name__ == "__main__":
    TestPolar.test_polar()
    TestEcliptic.test_ecliptic()
    test_utilities()
