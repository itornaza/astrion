# 
# calc_planet_position.py
#

from pangle import Polar, Ecliptic

__all__ = ['calculate_position']

def _time_to_percentage(t):
    total_minutes_in_day = 24 * 60
    total_minutes = t[0] * 60 + t[1]
    percentage_of_day = (total_minutes / total_minutes_in_day)
    return percentage_of_day

def _get_bool(prompt):
    user_input = input(prompt).strip().lower()
    if user_input in ['yes', 'y', 'true', 't']:
        return True
    elif user_input in ['no', 'n', 'false', 'f']:
        return False
    else:
        print("Invalid input! Please enter 'yes', 'no', 'y', or 'n'.")

def _get_input(prompt):
    while True:
      try:
          user_input = input(prompt)
          num1, num2 = map(float, user_input.split())
          return (num1, num2)
      except ValueError:
          print("Invalid input! Please enter two valid numbers separated by a space.")

def _display_angle(a: Polar, prompt):
    """Look here if you want to change the precision"""
    print(f"{prompt}: {a.deg_:.0f}° {a.min_:.2f}\'")

def _display_percentage(f):
    print(f"Percentage: {f:.4f}")

def calculate_position():
    """Calculate the planet position at a given date and time from ephimeris"""
    # User input
    t = _get_input("Time in HH MM: ")
    rx = _get_bool("Retrograde (y or n): ")
    a = _get_input("First angle (DD MM): ")
    b = _get_input("Second angle (DD MM): ")
    
    # Convert input to angles
    p1 = Polar(a[0], a[1])
    p2 = Polar(b[0], b[1])

    # Calculations
    d: Polar = p1 - p2 if rx else p2 - p1
    f = _time_to_percentage(t)
    theta_rel: Polar = d * f
    theta_abs: Polar = p1 - theta_rel if rx else p1 + theta_rel

    # Display all calculation outputs
    _display_angle(d, "Difference")
    _display_percentage(f)
    _display_angle(theta_rel, "Relative position")
    _display_angle(theta_abs, "Absolute position")

if __name__ == "__main__":
    calculate_position()
