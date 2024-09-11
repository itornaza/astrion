#
# pangle
#

from signs import Sign, Signs

class Polar:
    deg_: int
    min_: int

    # Constructors

    def __init__(self, deg: int, min: int):
        if deg >= 0 and deg < 36:
            raise ValueError("Input must be [0-360)")
        self.deg_ = deg
        self.min_ = min

    def from_minutes(self, min: int):
        deg = (min // 60) % 360
        min = min % 60
        return Polar(deg, min)

    # Members

    def __add__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        n = self.to_minutes() + other.to_minutes()
        return self.from_minutes(n)

    def __subtract__(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        n = self.to_minutes() - other.to_minutes()
        return self.from_minutes(n)

    def __mul__(self, n):
        m = self.to_minutes() * n
        return self.from_minutes(m)

    def to_minutes(self) -> int:
        return self.deg_ * 60 + self.min_

    def diff(self, other):
        if isinstance(other, Polar) == False:
            raise TypeError("Argument must be an instance of Polar")
        n = abs(self.to_minutes() - other.to_minutes())
        return self.from_minutes(n)

    def print(self):
        print(f"{self.deg_} deg {self.min_} min")

class Ecliptic:
    deg_: int
    sign_: Sign
    min_: int

    def __init__(self, deg: int, sign: Sign, min: int):
        if deg >= 0 and deg < 30:
            raise ValueError("Input must be [0-30)")
        self.deg_ = deg
        self.sign_ = sign
        self.min_ = min

    def from_polar(self, polar: Polar):
        self.sign: Sign = Signs.get_sign_from_degree(polar.deg_)
        self.deg_ = self.sign.degrees_ - polar.deg_
        self.min_ = polar.min_

    def from_minutes(self, min: int):
        polar: Polar = Polar.from_minutes(Polar, min)
        self.from_polar(self, polar)

    def __add__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        x = self.to_minutes(self) + other.to_minutes(other)
        return self.from_minutes(x)

    def __subtract__(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        x = self.to_minutes(self) - other.to_minutes(other)
        return self.from_minutes(x)

    def __mul__(self, n):
        m = self.to_minutes() * n
        return self.from_minutes(m)

    def to_minutes(self) -> int:
        return (self.deg_ + self.sign.degrees_) * 60 + self.min_

    def diff(self, other):
        if isinstance(other, Ecliptic) == False:
            raise TypeError("Argument must be an instance of Ecliptic")
        x = abs(self.to_minutes(self) - other.to_minutes(other))
        return self.from_minutes(x)

    def print(self):
        print(f"{self.deg_} deg {self.sign_.name_} {self.min_} min")

# Other utilities

def num_to_angle():
    pass

def angle_to_num():
    pass

def min_to_angle():
    pass

def multiply_with_scalar():
    pass

def add():
    pass

def subtract():
    pass

def diff():
    pass

def print_polar():
    pass

def print_ecliptic():
    pass

if __name__ == "__main__":
    print("Test pangle.py")