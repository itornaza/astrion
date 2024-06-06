# 
# planet_position.py
#

###############################################################################
#                               HELPER FUNCTIONS                              #
###############################################################################

def degrees_and_minutes_to_minutes(degrees, minutes):
    """Convert degrees and minutes to total minutes."""
    return degrees * 60 + minutes

def minutes_to_degrees_and_minutes(total_minutes):
    """Convert total minutes back to degrees and minutes."""
    degrees = total_minutes // 60
    minutes = total_minutes % 60
    return degrees, minutes

def add_angles(angle1, angle2):
    """Add two angles given in degrees and minutes."""
    total_minutes1 = degrees_and_minutes_to_minutes(*angle1)
    total_minutes2 = degrees_and_minutes_to_minutes(*angle2)
    total_minutes_sum = total_minutes1 + total_minutes2
    return minutes_to_degrees_and_minutes(total_minutes_sum)

def subtract_angles(angle1, angle2):
    """Subtract the second angle from the first angle given in degrees and 
    minutes."""
    total_minutes1 = degrees_and_minutes_to_minutes(*angle1)
    total_minutes2 = degrees_and_minutes_to_minutes(*angle2)
    total_minutes_difference = total_minutes1 - total_minutes2
    return minutes_to_degrees_and_minutes(total_minutes_difference)

def time_to_percentage(t):
    total_minutes_in_day = 24 * 60
    total_minutes = t[0] * 60 + t[1]
    percentage_of_day = (total_minutes / total_minutes_in_day)
    return percentage_of_day

def multiply_angle_by_percentage(angle, percentage):
    """Multiply an angle given in degrees and minutes by a percentage 
    factor."""
    total_minutes = degrees_and_minutes_to_minutes(*angle)
    resulting_minutes = total_minutes * percentage
    return minutes_to_degrees_and_minutes(resulting_minutes)

def get_bool(prompt):
    user_input = input(prompt).strip().lower()
    if user_input in ['yes', 'y', 'true', 't']:
        return True
    elif user_input in ['no', 'n', 'false', 'f']:
        return False
    else:
        print("Invalid input. Please enter 'yes', 'no', 'true', or 'false'.")

def get_hours_minutes(prompt):
    while True:
      try:
          user_input = input(prompt)
          num1, num2 = map(float, user_input.split())
          return (num1, num2)
      except ValueError:
          print("Invalid input. Please enter two valid numbers separated by a space.")

def get_integer(prompt):
    while True:
      try:
          user_input = input(prompt)
          integer_value = int(user_input)
          return integer_value
      except ValueError:
          print("Invalid input. Please enter a valid integer.")

def display_angle(a, prompt):
    print(f"{prompt}:\t {a[0]:.0f}° {a[1]:.0f}\'")

def display_percentage(f):
    print(f"Day percentage:\t\t {f:.4f}")

###############################################################################
#                                   USER INPUT                                #
###############################################################################

# Get the time we want to calculate the angle for
t = get_hours_minutes("Time? ")

# Is the planet in retrograde motion? 
rx = get_bool("Retrograde? ")

# Get the angles from ephimeris in the order they appear there
a = get_hours_minutes("Set the first angle in degrees and minutes: ")
b = get_hours_minutes("Set the second angle in degrees and minutes: ")

###############################################################################
#                                  CALCULATIONS                               #
###############################################################################

# Calculate the difference between the angles
d = subtract_angles(a, b) if rx else subtract_angles(b, a)

# Get the percentage of the day as a factor
f = time_to_percentage(t)

# Calculate the angle difference from that time to the previous angle
theta = multiply_angle_by_percentage(d, f)

# Calculate the resulting absolute angle
phi = subtract_angles(a, theta) if rx else add_angles(a, theta)

###############################################################################
#                                     REPORT                                  #
###############################################################################

display_angle(d, "Angles difference")
display_percentage(f)
display_angle(theta, "Angle diff at time")
display_angle(phi, "Position at time")
