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
    print("|     ---===  * Astrion Menu (1.3.3) *  ===---     |")
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
        if object:
            print_object(object)
        else:
            print("\n", E_KEYWORD, ": " + k.upper())

# Planet
def planet_handler():
    p = input(I_PLANET) 
    planet = Planets.get(Planets, p)
    if planet: 
        Planets.print(Planets, planet)
    else:
        print(E_PLANET)

# Sign
def sign_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign: 
        Signs.print(Signs, sign)
        Signs.print_arc(Signs, sign)
    else:
        print(E_SIGN)

# House
def house_handler():
    h = input(I_HOUSE) 
    house = Houses.get(Houses, h)
    if house: 
        Houses.print(Houses, house)
    else:
        print(E_HOUSE)

# Aspect
def aspect_handler():
    a = input(I_ASPECT) 
    aspect = Aspects.get(Aspects, a)
    if aspect: 
        Aspects.print(Aspects, aspect)
    else:
        print(E_ASPECT)

# Angle
def angle_handler():
    a = input(I_ANGLE) 
    angle = Angles.get(Angles, a)
    if angle: 
        Angles.print(Angles, angle)
    else:
        print(E_ANGLE)

# Polarity
def polarity_handler():
    p = input(I_POLARITY)
    polarity = Polarities.get(Polarities, p)
    if polarity:
        Polarities.print(Polarities, polarity)
        Signs.print_signs_in_polarity(Signs, polarity.name_)
    else:
        print(E_POLARITY)

# Mode
def mode_handler():
    m = input(I_MODE)
    mode = Modes.get(Modes, m)
    if mode:
        Modes.print(Modes, mode)
        Signs.print_signs_in_mode(Signs, mode.name_)
    else:
        print(E_MODE)

# Element
def element_handler():
    e = input(I_ELEMENT) 
    element = Elements.get(Elements, e)
    if element: 
        Elements.print(Elements, element)
        Signs.print_signs_in_element(Signs, element.name_)
    else:
        print(E_ELEMENT)

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
    if sign_a and sign_b:
        Signs.print_common_attributes(Signs, sign_a, sign_b)
    else:
        print(E_SIGN)

# Find signs with two common attributes
def three_in_common_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign: 
        list = Signs.find_two_common_attributes(Signs, sign)
        if len(list) > 0:
            sign_names = []
            for s in list:
                sign_names.append(s.name_)
            print("\nFound", len(list), "matching signs:", sign_names)
            for s in list:
                Signs.print_common_attributes(Signs, sign, s)
    else:
        print(E_SIGN)

# Find polarity and mode equivalent sign
def polarity_and_mode_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign: 
        Signs.print_polarity_mode(Signs, sign.polarity_, sign.mode_)
    else:
        print(E_SIGN)

# Find polarity and mode equivalent sign
def mode_and_element_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign: 
        Signs.print_mode_element(Signs, sign.mode_, sign.element_)
    else:
        print(E_SIGN)

# Find element and polarity equivalent sign
def element_and_polarity_handler():
    s = input(I_SIGN) 
    sign = Signs.get(Signs, s)
    if sign: 
        Signs.print_element_polarity(Signs,  sign.element_, sign.polarity_)
    else:
        print(E_SIGN)

# Generic version to get any valid object
def get_object_from_keyword(k):
    object = None 
    tmp = None

    tmp = Planets.get(Planets, k)
    if tmp: 
        object = tmp
    tmp = Signs.get(Signs, k)
    if tmp: 
        object = tmp
    tmp = Houses.get(Houses, k)
    if tmp: 
        object = tmp
    tmp = Aspects.get(Aspects, k)
    if tmp: 
        object = tmp
    tmp = Angles.get(Angles, k)
    if tmp: 
        object = tmp
    tmp = Polarities.get(Polarities, k)
    if tmp: 
        object = tmp
    tmp = Modes.get(Modes, k)
    if tmp: 
        object = tmp
    tmp = Elements.get(Elements, k)
    if tmp: 
        object = tmp
    return object

# Generic version to print any valid object
def print_object(object):
    if object:
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
    else:
        print(E_KEYWORD)