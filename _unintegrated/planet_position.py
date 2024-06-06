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

def time_to_percentage(hours, minutes):
    total_minutes_in_day = 24 * 60
    total_minutes = hours * 60 + minutes
    percentage_of_day = (total_minutes / total_minutes_in_day)
    return percentage_of_day

def multiply_angle_by_percentage(angle, percentage):
    """Multiply an angle given in degrees and minutes by a percentage 
    factor."""
    total_minutes = degrees_and_minutes_to_minutes(*angle)
    resulting_minutes = total_minutes * percentage
    return minutes_to_degrees_and_minutes(resulting_minutes)

###############################################################################
#                                   USER INPUT                                #
###############################################################################

# Is the planet in retrograde motion?
rx = False

# Get the angles from ephimeris in the order they appear there
prev_angle = (1, 58)
next_angle = (3, 11)  

# Get the time we want to calculate the angle for
hours = 2
minutes = 52

###############################################################################
#                                  CALCULATIONS                               #
###############################################################################

# 1. Calculate the difference between the angles
if rx:
  delta_angle = subtract_angles(prev_angle, next_angle)
else:
  delta_angle = subtract_angles(next_angle, prev_angle)

# Get the percentage of the day as a factor
percentage = time_to_percentage(hours, minutes)

# 3. Calculate the angle difference from that time to the previous angle
resulting_angle = multiply_angle_by_percentage(delta_angle, percentage)

# 4. Calculate the resulting absolute angle
if rx:
  result = subtract_angles(prev_angle, resulting_angle)
else: 
  result = add_angles(prev_angle, resulting_angle)

###############################################################################
#                                     REPORT                                  #
###############################################################################

print("Angles difference:\t", delta_angle)
print(f"Day percentage ({hours}, {minutes}):\t {percentage:.4f}")
print(f"Angle diff at time:\t ({resulting_angle[0]}, {resulting_angle[1]:.4f})")
print(f"Position:\t\t ({result[0]:.0f}, {result[1]:.0f})")
