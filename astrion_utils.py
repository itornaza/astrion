#
# astrion_utils
#

import os # os.system()
import time # time.sleep()

from planets import Planets # Handles polarity and mode as well
from signs import Signs
from houses import Houses
from aspects import Aspects
from angles import Angles
from elements import Elements

planets = Planets()
signs = Signs()
houses = Houses()
aspects = Aspects()
elements = Elements()

def print_header():
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
    time.sleep(0.2)
    print("                                                   >>> created by ion-  ")
    print("\n")
    time.sleep(0.8)

def print_menu():
    os.system("clear")
    print("+---------------------------------------------------+")
    print("|      ---===  * Astro Menu (v1.3.0) *  ===---      |")
    print("+------------------------+--------------------------+")
    print("| 1.  Keywords           | 6.  Angle                |")
    print("| 2.  Planet             | 7.  Polarity             |")
    print("| 3.  Sign               | 8.  Mode                 |")
    print("| 4.  House              | 9.  Element              |")
    print("| 5.  Aspect             | 10. Compare two signs    |")
    print("+------------------------+--------------------------+")
    print("| m.  Menu               | q.  Quit                 |")
    print("+------------------------+--------------------------+")

def keywords_handler():
    user_keyword_input = input("Enter terms separated by space: ")
    user_input_list = user_keyword_input.split()
    for term in user_input_list:

      # 1. Planet checks
      valid_term = Planets.get(Planets, term)
      if valid_term != -1: 
          Planets.print_keywords(Planets, valid_term.name_)
      else:
          valid_term -= 1
      
      # 2. Sign checks
      valid_term = Signs.get(Signs, term)
      if valid_term != -1: 
          Signs.print_keywords(Signs, valid_term.name_)
      else:
          valid_term -= 1
      
      # 3. Houses checks
      valid_term = Houses.get(Houses, term)
      if valid_term != -1: 
          Houses.print_keywords(Houses, valid_term.name_)
      else:
          valid_term -= 1
      
      # 4. Aspects checks
      valid_term = Aspects.get(Aspects, term)
      if valid_term != -1: 
          Aspects.print_keywords(Aspects, valid_term.name_)
      else:
          valid_term -= 1
      
      # 5. Angles checks
      valid_term = Angles.get(Angles, term)
      if valid_term != -1: 
          Angles.print_keywords(Angles, valid_term.name_)
      else:
          valid_term -= 1

      # 6. Elements checks
      valid_term = Elements.get(Elements, term)
      if valid_term != -1: 
          Elements.print_keywords(Elements, valid_term.name_)
      else:
          valid_term -= 1

      # Catch
      if valid_term == -1:
          print("\nInvalid keyword input: " + term.upper())

def planet_handler():
    p = input("Enter planet: ") 
    planet = Planets.get(Planets, p)
    if planet == -1: 
        print("Invalid planet input!")
    else:
        Planets.print(Planets, planet)

def sign_handler():
    s = input("Enter sign: ") 
    sign = Signs.get(Signs, s)
    if sign == -1: 
        print("Invalid sign input!")
    else:
        Signs.print(Signs, sign)
        Signs.print_arc(Signs, sign)

def house_handler():
    h = input("Enter house: ") 
    house = Houses.get(Houses, h)
    if house == -1: 
        print("Invalid house input!")
    else:
        Houses.print(Houses, house)

def aspect_handler():
    a = input("Enter aspect: ") 
    aspect = Aspects.get(Aspects, a)
    if aspect == -1: 
        print("Invalid aspect input!")
    else:
        Aspects.print(Aspects, aspect)

def angle_handler():
    a = input("Enter angle: ") 
    angle = Angles.get(Angles, a)
    if angle == -1: 
        print("Invalid angle input!")
    else:
        Angles.print(Angles, angle)

def polarity_handler():
    p = input("Enter polarity (ex. +): ")
    Signs.print_polarity(Signs, p)

def mode_handler():
    m = input("Enter mode (ex. Cardinal): ")
    Signs.print_mode(Signs, m)

def element_handler():
    e = input("Enter element: ") 
    element = Elements.get(Elements, e)
    if element == -1: 
        print("Invalid element input!")
    else:
        Elements.print(Elements, element)
        Signs.print_element(Signs, e)

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
        print("Invalid sign name!")
        return
    
    # Print common and relating attribites of the signs
    aspect_angle = abs(sign_a.degrees_ - sign_b.degrees_)
    aspect = Aspects.get_aspect_from_aspect_angle(aspect_angle)

    if aspect != -1:
        print("Aspect:\t\t", aspect.name_)
    
    print("Aspect degrees:\t", aspect_angle)
    if sign_a.polarity_ == sign_b.polarity_:
        print("Same polarity:\t ", sign_a.polarity_)
    if sign_a.mode_ == sign_b.mode_:
        print("Same mode:\t ", sign_a.mode_)
    if sign_a.element_ == sign_b.element_:
        print("Same element:\t ", sign_a.element_)
