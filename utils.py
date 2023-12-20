#
# utils
#

import os # os.system()
import time # time.sleep()
from constants import *
from planet import Planet
from sign import Sign
from house import House
from aspect import Aspect
from angle import Angle
from polarity import Polarity
from mode import Mode
from element import Element
from planets import Planets
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
    print("| 5.  Aspect            |                          |")
    print("+-----------+-----------+----------+---------------+")
    print("| m.  Menu  |  s.  Sign ops menu   | q.  Quit      |")
    print("+-----------+-----------+----------+---------------+")

def print_signs_ops_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|        ---===  * Signs Ops Menu *  ===---        |")
    print("+-----------------------+--------------------------+")
    print("| 1.  Keyword           | 5.  Polarity + mode      |")
    print("| 2.  Sign              | 6.  Mode + element       |")
    print("| 3.  Compare signs     | 7.  Element + mode       |")
    print("| 4.  Two in common     | 8.  Dump all signs       |")
    print("+-----------+-----------+----------+---------------+")
    print("| m.  Menu  |  s.  Sign ops menu   | q.  Quit      |")
    print("+-----------+----------------------+---------------+")

# Keywords
def keywords_handler():
    keywords_raw = input(I_KEYWORDS)
    keywords_list = keywords_raw.split()
    for k in keywords_list:
        object = get_object_from_keyword(k)
        if object == -1:
            print("\n", E_KEYWORD, ": " + k.upper())
        else:
            print_object(object)

# Planet
def planet_handler():
    p = input(I_PLANET) 
    planet = Planets.get(Planets, p)
    if planet == -1: 
        print(E_PLANET)
    else:
        Planets.print(Planets, planet)

# Sign
def sign_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print(E_SIGN)
    else:
        Signs.print(Signs, sign)
        Signs.print_arc(Signs, sign)

# House
def house_handler():
    h = input(I_HOUSE) 
    house = Houses.get(Houses, h)
    if house == -1: 
        print(E_HOUSE)
    else:
        Houses.print(Houses, house)

# Aspect
def aspect_handler():
    a = input(I_ASPECT) 
    aspect = Aspects.get(Aspects, a)
    if aspect == -1: 
        print(E_ASPECT)
    else:
        Aspects.print(Aspects, aspect)

# Angle
def angle_handler():
    a = input(I_ANGLE) 
    angle = Angles.get(Angles, a)
    if angle == -1: 
        print(E_ANGLE)
    else:
        Angles.print(Angles, angle)

# Polarity
def polarity_handler():
    p = input(I_POLARITY)
    polarity = Polarities.get(Polarities, p)
    if polarity == -1:
        print(E_POLARITY)
    else:
        Polarities.print(Polarities, polarity)
        Signs.print_signs_in_polarity(Signs, polarity.name_)

# Mode
def mode_handler():
    m = input(I_MODE)
    mode = Modes.get(Modes, m)
    if mode == -1:
        print(E_MODE)
    else:
        Modes.print(Modes, mode)
        Signs.print_signs_in_mode(Signs, mode.name_)

# Element
def element_handler():
    e = input(I_ELEMENT) 
    element = Elements.get(Elements, e)
    if element == -1: 
        print(E_ELEMENT)
    else:
        Elements.print(Elements, element)
        Signs.print_signs_in_element(Signs, element.name_)

# Compare two signs
def compare_signs_handler():
    user_input = input(I_KEYWORDS)
    signs_list = user_input.split()
    
    # Check number of signs
    if len(signs_list) != 2:
        print(E_NUMBER_OF_SIGNS)
        return
    
    sign_a = Signs.get(Signs, signs_list[0])
    sign_b = Signs.get(Signs, signs_list[1])
    
    # Check valid signs
    if (sign_a == -1) or (sign_b == -1):
        print(E_SIGN)
    else:
        Signs.print_common_attributes(Signs, sign_a, sign_b)

# Find signs with two common attributes
def three_in_common_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print(E_SIGN)
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
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print(E_SIGN)
    else:
        Signs.print_polarity_mode(Signs, sign.polarity_, sign.mode_)

# Find polarity and mode equivalent sign
def mode_and_element_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print(E_SIGN)
    else:
        Signs.print_mode_element(Signs, sign.mode_, sign.element_)

# Find element and polarity equivalent sign
def element_and_polarity_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print(E_SIGN)
    else:
        Signs.print_element_polarity(Signs,  sign.element_, sign.polarity_)

# Generic version to get any valid object
def get_object_from_keyword(k):
    object = Planets.get(Planets, k)
    if object != -1:
        return object
    object = Signs.get(Signs, k)
    if object != -1:
        return object
    object = Houses.get(Houses, k)
    if object != -1:
        return object
    object = Aspects.get(Aspects, k)
    if object != -1:
        return object
    object = Angles.get(Angles, k)
    if object != -1:
        return object
    object = Polarities.get(Polarities, k)
    if object != -1:
        return object
    object = Modes.get(Modes, k)
    if object != -1:
        return object
    object = Elements.get(Elements, k)
    if object != -1:
        return object
    return -1

# Generic version to print any valid object
def print_object(object):
    if object == -1:
        print(E_KEYWORD)
    else:
        if isinstance(object, Planet):
            Planets.print_keywords(Planets, object.name_) 
        if isinstance(object, Sign):
            Signs.print_keywords(Signs, object.name_)
        if isinstance(object, House):
            Houses.print_keywords(Houses, object.name_) 
        if isinstance(object, Aspect):
            Aspects.print_keywords(Aspects, object.name_) 
        if isinstance(object, Angle):
            Angles.print_keywords(Angles, object.name_) 
        if isinstance(object, Polarity):
            Polarities.print_keywords(Polarities, object.name_) 
        if isinstance(object, Mode):
            Modes.print_keywords(Modes, object.name_) 
        if isinstance(object, Element):
            Elements.print_keywords(Elements, object.name_) 
