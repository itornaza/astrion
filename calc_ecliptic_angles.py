# 
# calc_ecliptic_angles.py
#

__all__ = ['calculate_aspect_from_angle']

from signs import Signs
from aspects import Aspects

def _angle_to_decimal(deg: float, sign: str, min: float):
    s = Signs.get(Signs, sign)
    return s.degrees_ + deg + (min / 60.0)

def _get_angle():
    while True:
      try:
          user_input = input("Enter Angle `dd sign mm`: ")
          deg, s, min = map(str, user_input.split())
          return (float(deg), s, float(min))
      except ValueError:
          print("Invalid input! Please enter `dd sign mm` separated by a spaces.")

def _calculate_angle_diff():
    a = _get_angle()
    b = _get_angle()
    alpha = _angle_to_decimal(a[0], a[1], a[2])
    beta = _angle_to_decimal(b[0], b[1], b[2])
    d = abs(alpha - beta)
    return d if d <=180 else 360 - d

def _decimal_to_degrees_minutes(a):
    deg = int(a)
    min = (a - deg) * 60
    return deg, min

def calculate_aspect_from_angle():
    angle = _calculate_angle_diff()
    aspect = Aspects.get_aspect_from_angle(angle)
    deg, min = _decimal_to_degrees_minutes(angle)
    if aspect != None:
        print(f"\n\t{deg:.0f} deg {min:.0f} min -- {aspect.name_}")
    else:
        print(f"\n\t{deg:.0f} deg {min:.0f} min -- Unaspected")

if __name__ == "__main__":
    calculate_aspect_from_angle()