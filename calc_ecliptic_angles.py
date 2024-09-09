# 
# calc_ecliptic_angles.py
#

__all__ = ['calculate_aspect_from_angle', 
           'get_decimal_angle',
           'decimal_to_ecliptic',
           'get_ecliptic_angle',
           'ecliptic_to_decimal'
           ]

from signs import *
from aspects import *

def get_decimal_angle():
    while True:
        user_input = input("Enter Angle `dd  mm`: ")
        deg, min = map(str, user_input.split())
        deg = float(deg)
        min = float(min)
        rem = min // 60
        min = min % 60
        deg = (deg + rem) % 360
        return (deg, min)

def decimal_to_ecliptic(deg: float, min: float):
    """Converts an angle from decimal format [0 - 360) to ecliptic format
    00 Aries 00 - 29 Pisces 59"""
    rem = min // 60
    min = min % 60 
    deg = (deg + rem) % 360
    
    sign: Sign = Signs.get_sign_from_degree(Signs, deg)
    deg = deg - sign.degrees_
    return (float(deg), sign, float(min))

def get_ecliptic_angle():
    while True:
        user_input = input("Enter Angle `dd sign mm`: ")
        deg, s, min = map(str, user_input.split())
        sign = Signs.get(Signs, s)
        if sign != None:
            return (float(deg), sign, float(min))
        elif sign == None:
            print("There is no such sign! Give it another try.")
        else:
            print("Invalid input! Please enter `dd sign mm` separated by a spaces.")

def ecliptic_to_decimal(deg: float, sign: Sign, min: float):
    """Converts an angle from ecliptic format 00 Aries 00 - 29 Pisces 59 to
    decimal format (0 - 360)"""

    # TODO move min remainder to degrees

    return (sign.degrees_ + deg, min)

def calculate_angle_diff():
    a = get_ecliptic_angle()
    b = get_ecliptic_angle()
    
    # TODO: Fix subtraction of degrees and minutes
    alpha = ecliptic_to_decimal(a[0], a[1], a[2])
    beta = ecliptic_to_decimal(b[0], b[1], b[2])
    d = abs(alpha - beta)
    return d if d <=180 else 360 - d

def decimal_to_degrees_minutes(a):
    deg = int(a)
    min = (a - deg) * 60
    return deg, min

def calculate_aspect_from_angle():
    angle = calculate_angle_diff()
    aspect = Aspects.get_aspect_from_angle(angle)
    deg, min = decimal_to_degrees_minutes(angle)
    if aspect != None:
        print(f"\n\t{deg:.0f} deg {min:.0f} min -- {aspect.name_}")
    else:
        print(f"\n\t{deg:.0f} deg {min:.0f} min -- Unaspected")

if __name__ == "__main__":
    calculate_aspect_from_angle()
    