#
# utils
#

import os # os.system()
import time # time.sleep()
from planets import Planets # Handles polarity and mode as well
from signs import Signs
from houses import Houses
from aspects import Aspects
from angles import Angles
from elements import Elements
from polarities import Polarities
from modes import Modes

planets = Planets()
signs = Signs()
houses = Houses()
aspects = Aspects()
angles = Angles()
polarities = Polarities()
modes = Modes()
elements = Elements()

def print_header(t1, t2):
    os.system("clear")
    print("\n\n")
    print("    ***       ****    ********   *****      ***     ****      **    *** ")
    print(" **    **   ***         ***      **  ***    **    **    **    ** *  **  ")
    print(" **    **    ***        ***      **   **    **    **    **    **  * **  ")
    print(" ********      ***      ***      ******     **    **    **    **   ***  ")
    print(" **    **       ***     ***      **   **    **    **    **    **    **  ")
    print(" **    **     ***       ***      **   **    **    **    **    **    **  ")
    print("***    **   ****       ****     ***   **   ***      ****     ***    **  ")
    print("\n")
    time.sleep(t1)
    print("                                                   >>> created by ion-  ")
    print("\n")
    time.sleep(t2)
    os.system("clear")

def print_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|      ---===  * Astro Menu (v1.3.0) *  ===---     |")
    print("+-----------------------+--------------------------+")
    print("| 1.  Keywords          | 6.  Angle                |")
    print("| 2.  Planet            | 7.  Polarity             |")
    print("| 3.  Sign              | 8.  Mode                 |")
    print("| 4.  House             | 9.  Element              |")
    print("| 5.  Aspect            | 10. Compare two signs    |")
    print("+-----------------------+--------------------------+")
    print("| m.  Menu              | q.  Quit                 |")
    print("+-----------------------+--------------------------+")

# 1. Keywords
def keywords_handler():
    user_keyword_input = input("Enter terms separated by space: ")
    user_input_list = user_keyword_input.split()
    for term in user_input_list:

        # Planet checks
        valid_term = Planets.get(Planets, term)
        if valid_term != -1: 
            Planets.print_keywords(Planets, valid_term.name_)
        else:
            valid_term -= 1

        # Sign checks
        valid_term = Signs.get(Signs, term)
        if valid_term != -1: 
            Signs.print_keywords(Signs, valid_term.name_)
        else:
            valid_term -= 1

        # Houses checks
        valid_term = Houses.get(Houses, term)
        if valid_term != -1: 
            Houses.print_keywords(Houses, valid_term.name_)
        else:
            valid_term -= 1

        # Aspects checks
        valid_term = Aspects.get(Aspects, term)
        if valid_term != -1: 
            Aspects.print_keywords(Aspects, valid_term.name_)
        else:
            valid_term -= 1

        # Angles checks
        valid_term = Angles.get(Angles, term)
        if valid_term != -1: 
            Angles.print_keywords(Angles, valid_term.name_)
        else:
            valid_term -= 1

        # Polarity checks
        valid_term = Polarities.get(Polarities, term)
        if valid_term != -1: 
            Polarities.print_keywords(Polarities, valid_term.name_)
        else:
            valid_term -= 1

        # Mode checks
        valid_term = Modes.get(Modes, term)
        if valid_term != -1: 
            Modes.print_keywords(Modes, valid_term.name_)
        else:
            valid_term -= 1

        # Elements checks
        valid_term = Elements.get(Elements, term)
        if valid_term != -1: 
            Elements.print_keywords(Elements, valid_term.name_)
        else:
            valid_term -= 1

        # Catch
        if valid_term == -1:
            print("\nInvalid keyword: " + term.upper())

# 2. Planet
def planet_handler():
    p = input("Enter planet: ") 
    planet = Planets.get(Planets, p)
    if planet == -1: 
        print("Invalid planet!")
    else:
        Planets.print(Planets, planet)

# 3. Sign
def sign_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign!")
    else:
        Signs.print(Signs, sign)
        Signs.print_arc(Signs, sign)

# 4. House
def house_handler():
    h = input("Enter house: ") 
    house = Houses.get(Houses, h)
    if house == -1: 
        print("Invalid house!")
    else:
        Houses.print(Houses, house)

# 5. Aspect
def aspect_handler():
    a = input("Enter aspect: ") 
    aspect = Aspects.get(Aspects, a)
    if aspect == -1: 
        print("Invalid aspect!")
    else:
        Aspects.print(Aspects, aspect)

# 6. Angle
def angle_handler():
    a = input("Enter angle: ") 
    angle = Angles.get(Angles, a)
    if angle == -1: 
        print("Invalid angle!")
    else:
        Angles.print(Angles, angle)

# 7. Polarity
def polarity_handler():
    p = input("Enter polarity: ")
    polarity = Polarities.get(Polarities, p)
    if polarity == -1:
        print("Invaiid polarity!")
    else:
        Polarities.print(Polarities, polarity)
        Signs.print_signs_in_polarity(Signs, polarity.name_)

# 8. Mode
def mode_handler():
    m = input("Enter mode: ")
    mode = Modes.get(Modes, m)
    if mode == -1:
        print("Invalid mode!")
    else:
        Modes.print(Modes, mode)
        Signs.print_signs_in_mode(Signs, mode.name_)

# 9. Element
def element_handler():
    e = input("Enter element: ") 
    element = Elements.get(Elements, e)
    if element == -1: 
        print("Invalid element!")
    else:
        Elements.print(Elements, element)
        Signs.print_signs_in_element(Signs, element.name_)

# 10. Compare two signs
def compare_signs_handler():
    user_input = input("Enter terms separated by space: ")
    signs_list = user_input.split()
    
    # Check number of signs
    if len(signs_list) != 2:
        print("Invalid number of signs given, should be two!")
        return
    
    sign_a = Signs.get(Signs, signs_list[0])
    sign_b = Signs.get(Signs, signs_list[1])
    
    # Check valid signs
    if (sign_a == -1) or (sign_b == -1):
        print("Invalid sign!")
        return
    
    # Calculate aspect data
    aspect_angle = Aspects.calculate_aspect_angle(Aspects, sign_a, sign_b)
    aspect = Aspects.get_aspect_from_aspect_angle(aspect_angle)

    # Print common and relating attribites of the signs
    similarities = 0
    print("\nSigns\t\t\t:\t", sign_a.name_.upper(), "and", sign_b.name_.upper())
    if aspect != -1:
        print("Aspect\t\t\t:\t", aspect.name_)
    print("Aspect degrees\t\t:\t", aspect_angle)
    
    if sign_a.polarity_ == sign_b.polarity_:
        print("Same polarity\t\t:\t", sign_a.polarity_)
        similarities = similarities + 1
    if sign_a.mode_ == sign_b.mode_:
        print("Same mode\t\t:\t", sign_a.mode_)
        similarities = similarities + 1
    if sign_a.element_ == sign_b.element_:
        print("Same element\t\t:\t", sign_a.element_)
        similarities = similarities + 1
    print("\n")

    if similarities == 0:
        print(sign_a.name_, "and", sign_b.name_, 
              "do not have anything in common")
    else:
        print(sign_a.name_, "and", sign_b.name_, 
              "have", similarities, "out of 3 in common")
    print("\n")
