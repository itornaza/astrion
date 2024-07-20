# 
# planet_position.py
#

__all__ = ['calculate_position']

def _degrees_and_minutes_to_minutes(degrees, minutes):
    """Convert degrees and minutes to total minutes."""
    return degrees * 60 + minutes

def _minutes_to_degrees_and_minutes(total_minutes):
    """Convert total minutes back to degrees and minutes."""
    degrees = total_minutes // 60
    minutes = total_minutes % 60
    return degrees, minutes

def _add_angles(angle1, angle2):
    """Add two angles given in degrees and minutes."""
    total_minutes1 = _degrees_and_minutes_to_minutes(*angle1)
    total_minutes2 = _degrees_and_minutes_to_minutes(*angle2)
    total_minutes_sum = total_minutes1 + total_minutes2
    return _minutes_to_degrees_and_minutes(total_minutes_sum)

def _subtract_angles(angle1, angle2):
    """Subtract the second angle from the first angle given in degrees and 
    minutes."""
    total_minutes1 = _degrees_and_minutes_to_minutes(*angle1)
    total_minutes2 = _degrees_and_minutes_to_minutes(*angle2)
    total_minutes_difference = total_minutes1 - total_minutes2
    return _minutes_to_degrees_and_minutes(total_minutes_difference)

def _time_to_percentage(t):
    total_minutes_in_day = 24 * 60
    total_minutes = t[0] * 60 + t[1]
    percentage_of_day = (total_minutes / total_minutes_in_day)
    return percentage_of_day

def _multiply_angle_by_percentage(angle, percentage):
    """Multiply an angle given in degrees and minutes by a percentage 
    factor."""
    total_minutes = _degrees_and_minutes_to_minutes(*angle)
    resulting_minutes = total_minutes * percentage
    return _minutes_to_degrees_and_minutes(resulting_minutes)

def _get_bool(prompt):
    user_input = input(prompt).strip().lower()
    if user_input in ['yes', 'y', 'true', 't']:
        return True
    elif user_input in ['no', 'n', 'false', 'f']:
        return False
    else:
        print("Invalid input! Please enter 'yes', 'no', 'y', or 'n'.")

def _get_hours_or_degrees_and_minutes(prompt):
    while True:
      try:
          user_input = input(prompt)
          num1, num2 = map(float, user_input.split())
          return (num1, num2)
      except ValueError:
          print("Invalid input! Please enter two valid numbers separated by a space.")

def _get_integer(prompt):
    while True:
      try:
          user_input = input(prompt)
          integer_value = int(user_input)
          return integer_value
      except ValueError:
          print("Invalid input! Please enter a valid integer.")

def _display_angle(a, prompt):
    """Look here if you want to change the precision"""
    print(f"{prompt}: {a[0]:.0f}° {a[1]:.2f}\'")

def _display_percentage(f):
    print(f"Percentage: {f:.4f}")

def calculate_position():
    """Calculate the planet position at a given date and time from ephimeris"""
    # User input
    t = _get_hours_or_degrees_and_minutes("Time in HH MM: ")
    rx = _get_bool("Retrograde (y or n): ")
    a = _get_hours_or_degrees_and_minutes("First angle (DD MM): ")
    b = _get_hours_or_degrees_and_minutes("Second angle (DD MM): ")
    
    # Calculations
    d = _subtract_angles(a, b) if rx else _subtract_angles(b, a)
    f = _time_to_percentage(t)
    theta_rel = _multiply_angle_by_percentage(d, f)
    theta_abs = _subtract_angles(a, theta_rel) if rx else _add_angles(a, theta_rel)

    # Display all calculation outputs
    _display_angle(d, "Difference")
    _display_percentage(f)
    _display_angle(theta_rel, "Relative position")
    _display_angle(theta_abs, "Absolute position")

if __name__ == "__main__":
    calculate_position()
