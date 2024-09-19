# 
# calc_ecliptic_angles.py
#

__all__ = ['calculate_aspect_from_angle', 'get_ecliptic']

from signs import *
from aspects import *
from pangle import Ecliptic, Polar, to_polar

def get_ecliptic(prompt):
    while True:
        try:
            user_input = input(prompt)
            deg_str, s, min_str = map(str, user_input.split())
            deg = int(deg_str)
            min = int(min_str)
            sign = Signs.get(Signs, s)
            return (deg, sign, min)
        except ValueError:
            print("Invalid input! Please enter numberm sign number separated by a spaces.")

def calculate_aspect_from_angle():
    """Calculates the aspect formed between two ecliptic angles"""
    a = get_ecliptic("Enter first angle `dd sign mm`: ")
    b = get_ecliptic("Enter second angle `dd sign mm`: ")
    assert isinstance(a[0], int) and isinstance(a[1], Sign) and isinstance(a[2], int)
    assert isinstance(b[0], int) and isinstance(b[1], Sign) and isinstance(b[2], int)
    e1: Ecliptic = Ecliptic(a[0], a[1], a[2])
    e2: Ecliptic = Ecliptic(b[0], b[1], b[2])
    d: Polar = to_polar(e1.diff(e2))    

    # TODO, take min into the calculation as well. The current implementation
    # of Aspects.get_aspect_from_angle() takes just an int as angle
    aspect = Aspects.get_aspect_from_angle(d.deg_)
    if aspect != None:
        print(f"\n\t{d.deg_:.0f}° {d.min_:.0f}' -- {aspect.name_}")
    else:
        print(f"\n\t{d.deg_:.0f}° {d.min_:.0f}' -- Unaspected")

if __name__ == "__main__":
    calculate_aspect_from_angle()
    