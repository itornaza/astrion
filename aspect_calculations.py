# 
# aspect_calculations.py
#

# __all__ = ['calculate_aspect']

from signs import Signs
from aspects import Aspects

def _angle_to_decimal(deg: float, sign: str, min: float):
    s = Signs.get(Signs, sign)
    return s.degrees_ + deg + (min / 60.0)

def _get_angle():
    while True:
      try:
          user_input = input("Enter Angle in format `DD SIGN MM` example 07 Aries 01: ")
          deg, s, min = map(str, user_input.split())
          return (float(deg), s, float(min))
      except ValueError:
          print("Invalid input! Please enter DEG SIGN MIN separated by a spaces.")

def calculate_difference():
    # Convert the angles to decimal degrees
    a = _get_angle()
    b = _get_angle()

    alpha = _angle_to_decimal(a[0], a[1], a[2])
    beta = _angle_to_decimal(b[0], b[1], b[2])

    # Calculate the difference
    dif = abs(alpha - beta)
    return dif

def get_aspect():
    angle = calculate_difference()
    
    aspect = Aspects.get_aspect_from_angle(angle)
    print(f"The difference between the two angles is {angle:.2f} degrees.")
    print(f"Aspected in {aspect.name_}!")

if __name__ == "__main__":
    get_aspect()