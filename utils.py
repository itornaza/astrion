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

def print_header(t1_header, t2_credits):
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
    time.sleep(t1_header)
    print("                                                   >>> created by ion-  ")
    print("\n")
    time.sleep(t2_credits)
    os.system("clear")

def print_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|     ---===  * Astrion Menu (v1.3.2) *  ===---    |")
    print("+-----------------------+--------------------------+")
    print("| 1.  Keywords          | 6.  Angle                |")
    print("| 2.  Planet            | 7.  Polarity             |")
    print("| 3.  Sign              | 8.  Mode                 |")
    print("| 4.  House             | 9.  Element              |")
    print("| 5.  Aspect            | 10. Signs ops menu       |")
    print("+-----------------------+--------------------------+")
    print("| m.  Menu              | q.  Quit                 |")
    print("+-----------------------+--------------------------+")

def print_signs_ops_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|        ---===  * Signs Ops Menu *  ===---        |")
    print("+-----------------------+--------------------------+")
    print("| 1.  Keyword           | 5.  Polarity + mode      |")
    print("| 2.  Sign              | 6.  Mode + element       |")
    print("| 3.  Compare signs     | 7.  Element + mode       |")
    print("| 4.  Two in common     | 8.  Dump all signs       |")
    print("+---------------+-------+--------+-----------------+")
    print("| m.  Menu      |  b.  Back      | q.  Quit        |")
    print("+---------------+----------------+-----------------+")

# Keywords
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

# Planet
def planet_handler():
    p = input("Enter planet: ") 
    planet = Planets.get(Planets, p)
    if planet == -1: 
        print("Invalid planet!")
    else:
        Planets.print(Planets, planet)

# Sign
def sign_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign!")
    else:
        Signs.print(Signs, sign)
        Signs.print_arc(Signs, sign)

# House
def house_handler():
    h = input("Enter house: ") 
    house = Houses.get(Houses, h)
    if house == -1: 
        print("Invalid house!")
    else:
        Houses.print(Houses, house)

# Aspect
def aspect_handler():
    a = input("Enter aspect: ") 
    aspect = Aspects.get(Aspects, a)
    if aspect == -1: 
        print("Invalid aspect!")
    else:
        Aspects.print(Aspects, aspect)

# Angle
def angle_handler():
    a = input("Enter angle: ") 
    angle = Angles.get(Angles, a)
    if angle == -1: 
        print("Invalid angle!")
    else:
        Angles.print(Angles, angle)

# Polarity
def polarity_handler():
    p = input("Enter polarity: ")
    polarity = Polarities.get(Polarities, p)
    if polarity == -1:
        print("Invaiid polarity!")
    else:
        Polarities.print(Polarities, polarity)
        Signs.print_signs_in_polarity(Signs, polarity.name_)

# Mode
def mode_handler():
    m = input("Enter mode: ")
    mode = Modes.get(Modes, m)
    if mode == -1:
        print("Invalid mode!")
    else:
        Modes.print(Modes, mode)
        Signs.print_signs_in_mode(Signs, mode.name_)

# Element
def element_handler():
    e = input("Enter element: ") 
    element = Elements.get(Elements, e)
    if element == -1: 
        print("Invalid element!")
    else:
        Elements.print(Elements, element)
        Signs.print_signs_in_element(Signs, element.name_)

# Compare two signs
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
    else:
        Signs.print_common_attributes(Signs, sign_a, sign_b)

# Find signs with two common attributes
def three_in_common_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign!")
    else:
        list = Signs.find_two_common_attributes(Signs, sign)
        if len(list) > 0:
            sign_names = []
            for s in list:
                sign_names.append(s.name_)
            print("\nFound", len(list), "matching signs:", sign_names)
            for s in list:
                Signs.print_common_attributes(Signs, sign, s)

# Find polarity and mode equivalent sign
def polarity_and_mode_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign!")
    else:
        Signs.print_polarity_mode(Signs, sign.polarity_, sign.mode_)

# Find polarity and mode equivalent sign
def mode_and_element_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign!")
    else:
        Signs.print_mode_element(Signs, sign.mode_, sign.element_)

# Find element and polarity equivalent sign
def element_and_polarity_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign!")
    else:
        Signs.print_element_polarity(Signs,  sign.element_, sign.polarity_)
