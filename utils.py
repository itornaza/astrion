#
# utils
#

import os # os.system()
import time # time.sleep()

from constants import *
from planets import *
from signs import *
from houses import *
from aspects import *
from angles import *
from elements import *
from polarities import *
from modes import *
from patterns import *
from lunar_phases import *
from lunar_nodes import *
from hemispheres import *
from trisectors import *
from quadrants import *
from chart import *

from pangle import *
import calc_planet_position
import calc_ecliptic_angles

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

###############################################################################
#                               MAIN MENU                                     #
###############################################################################

def print_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|   ---===  * Astrion Menu (", VERSION, ") *  ===---      |")
    print("+-----------------------+--------------------------+")
    print("| 1.  Keywords          | 7.  Polarity             |")
    print("| 2.  Planet            | 8.  Mode                 |")
    print("| 3.  Sign              | 9.  Element              |")
    print("| 4.  House             | 10. Aspects in pattern   |")
    print("| 5.  Aspect            | 11. Lunar phase          |")
    print("| 6.  Angle             | 12. Chart                |")
    print("|                       |                          |")
    print("+-----------+-----------+---+-----------+----------+")
    print("| m.  Menu  |  s.  Sign ops |  c. Calc  | q.  Quit |")
    print("+-----------+---------------+-----------+----------+")
    print("|              *. Chart analysis                   |")
    print("+--------------------------------------------------+")

# Keywords
def keywords_handler():
    """Extract keywords using ',' and 'in' as delimetters"""
    keywords_raw = input(I_KEYWORDS)
    keywords_comma = keywords_raw.split(',')
    keywords = []
    for phrases in keywords_comma:
        keywords += phrases.split(' in ')
    for keyword in keywords:
        object = get_object_from_keyword(keyword)
        if object:
            print_object(object)
        else:
            print("\n", E_KEYWORD, ": " + keyword.upper())

# Generic version to get any valid object from the corresponding keyword
def get_object_from_keyword(k):
    object = None 
    tmp = None
    if tmp := Planets.get(Planets, k): object = tmp
    if tmp := Signs.get(Signs, k): object = tmp
    if tmp := Houses.get(Houses, k): object = tmp
    if tmp := Aspects.get(Aspects, k): object = tmp
    if tmp := Angles.get(Angles, k): object = tmp
    if tmp := Polarities.get(Polarities, k): object = tmp
    if tmp := Modes.get(Modes, k): object = tmp
    if tmp := Elements.get(Elements, k): object = tmp
    if tmp := Patterns.get(Patterns, k): object = tmp
    if tmp := LunarPhases.get(LunarPhases, k): object = tmp
    if tmp := LunarNodes.get(LunarNodes, k): object = tmp
    if tmp := Hemispheres.get(Hemispheres, k): object = tmp
    if tmp := Trisectors.get(Trisectors, k): object = tmp
    if tmp := Quadrants.get(Quadrants, k): object = tmp
    return object

# Generic version to print any valid object's keywords
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
        if isinstance(object, Pattern):
            Patterns.print_keywords(Patterns, object.name_)
        if isinstance(object, LunarPhase):
            LunarPhases.print_keywords(LunarPhases, object.name_)
        if isinstance(object, LunarNode):
            LunarNodes.print_keywords(LunarNodes, object.name_)
        if isinstance(object, Hemisphere):
            Hemispheres.print_keywords(Hemispheres, object.name_)
        if isinstance(object, Trisector):
            Trisectors.print_keywords(Trisectors, object.name_)
        if isinstance(object, Quadrant):
            Quadrants.print_keywords(Quadrants, object.name_)
    else:
        print(E_KEYWORD)

# Planet
def planet_handler():
    p = input(I_PLANET) 
    planet = Planets.get(Planets, p)
    Planets.print(Planets, planet) if planet else print(E_PLANET)

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
    Houses.print(Houses, house) if house else print(E_HOUSE)

# Aspect
def aspect_handler():
    a = input(I_ASPECT) 
    aspect = Aspects.get(Aspects, a)
    Aspects.print(Aspects, aspect) if aspect else print(E_ASPECT)

# Angle
def angle_handler():
    a = input(I_ANGLE) 
    angle = Angles.get(Angles, a)
    Angles.print(Angles, angle) if angle else print(E_ANGLE)

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

# Pattern
def pattern_handler():
    p = input(I_PATTERN)
    pattern = Patterns.get(Patterns, p)
    if pattern:
        Patterns.print(Patterns, pattern)
        for a in pattern.aspects_:
            aspect = Aspects.get(Aspects, a)
            Aspect.print(aspect)
    else:
        print(E_PATTERN)

# Lunar phase
def lunar_phase_handler():
    lp = input(I_LUNAR_PHASE)
    lunar_phase = LunarPhases.get(LunarPhases, lp)
    LunarPhases.print(LunarPhases, lunar_phase) if lunar_phase else print(E_LUNAR_PHASE)

###############################################################################
#                              SIGN OPS MENU                                  #
###############################################################################

def print_signs_ops_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|        ---===  * Signs Ops Menu *  ===---        |")
    print("+-----------------------+--------------------------+")
    print("| 1.  Keyword           | 5.  Polarity + mode      |")
    print("| 2.  Sign              | 6.  Mode + element       |")
    print("| 3.  Compare signs     | 7.  Element + mode       |")
    print("| 4.  Two in common     |                          |")
    print("|                       |                          |")
    print("+-----------+-----------+---+-----------+----------+")
    print("| m.  Menu  |  s.  Sign ops |  c. Calc  | q.  Quit |")
    print("+-----------+---------------+-----------+----------+")
    print("|              *. Chart analysis                   |")
    print("+--------------------------------------------------+")

# Compare two signs
def compare_signs_handler():
    user_input = input(I_KEYWORDS)
    signs_list = user_input.split(',')
    
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

###############################################################################
#                             CALCULATOR MENU                                 #
###############################################################################

def print_calculator_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|        ---===  * Calculator Menu *  ===---       |")
    print("+-----------------------+--------------------------+")
    print("| 1. Planet positions   | 3. Ecliptic to polar     |")
    print("| 2. Aspect from angles | 4. Polar to ecliptic     |")
    print("|                       |                          |")
    print("+-----------+-----------+---+-----------+----------+")
    print("| m.  Menu  |  s.  Sign ops |  c. Calc  | q.  Quit |")
    print("+-----------+---------------+-----------+----------+")
    print("|              *. Chart analysis                   |")
    print("+--------------------------------------------------+")

# Planet calculator handler
def planet_calculator_handler():
    calc_planet_position.calculate_position()

# Aspect from ecliptic angles handler
def aspect_from_ecliptic_angless_handler():
    calc_ecliptic_angles.calculate_aspect_from_angle()
    
def polar_to_ecliptic_handler():
    p: Polar = calc_planet_position.get_polar("Enter angle `dd mm`: ")
    e: Ecliptic = to_ecliptic(p)
    e.print()

def ecliptic_to_polar_handler():
    e: Ecliptic = calc_ecliptic_angles.get_ecliptic("Enter angle `dd sign mm`: ")
    p: Polar = to_polar(e)
    p.print()

###############################################################################
#                               CHART MENU                                    #
###############################################################################

# Global chart variable used by all handlers below to access objects data
chart = None

def print_chart_full_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|          ---===  * Chart Menu *  ===---          |")
    print("+-----------------------+--------------------------+")
    print("| 1.  New chart         | 9.  Hemispheres          |")
    print("| 2.  Load chart        | 10. Triples              |")
    print("| 3.  House cusps       | 11. Quadrants            |")
    print("| 4.  Placements        | 12. Lunar phase          |")
    print("| 5.  Aspects           | 13. Dignities/Debilities |")
    print("| 6.  Polarity          | 14. Rulerships           |")
    print("| 7.  Elements          | 15. Mutual reception     |")
    print("| 8.  Modes             | 16. All                  |")
    print("+-----------+-----------+---+-----------+----------+")
    print("| m.  Menu  |  s.  Sign ops |  c. Calc  | q.  Quit |")
    print("+-----------+---------------+-----------+----------+")
    print("|              *. Chart analysis                   |")
    print("+--------------------------------------------------+")

def print_chart_short_menu():
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|          ---===  * Chart Menu *  ===---          |")
    print("+-----------------------+--------------------------+")
    print("| 1.  New chart         |                          |")
    print("| 2.  Load chart        |                          |")
    print("+-----------+-----------+---+-----------+----------+")
    print("| m.  Menu  |  s.  Sign ops |  c. Calc  | q.  Quit |")
    print("+-----------+---------------+-----------+----------+")
    print("|              *. Chart analysis                   |")
    print("+--------------------------------------------------+")

def print_chart_menu():
    print_chart_full_menu() if chart else print_chart_short_menu()

def chart_new_chart_handler():
    global chart
    chart = Chart("", Chart.get_house_system())

def chart_load_chart_handler():
    global chart
    chart = Chart(Chart.get_filename(), Chart.get_house_system())    

# TODO: Add the chart ruler here

def chart_house_cusps_handler():
    if chart is not None:
        chart.get_house_cusps()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_placements_handler():
    if chart is not None:
        chart.get_entities_in_signs_and_houses()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_aspects_handler():
    if chart is not None:
        chart.get_aspects()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_polarity_handler():
    if chart is not None:
        chart.get_polarity()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_elements_handler():
    if chart is not None:
        chart.get_elements()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_mode_handler():
    if chart is not None:
        chart.get_modes()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_hemispheres_handler():
    if chart is not None:
        chart.get_hemispheres()
    else: 
        print("Load or input chart data using menu options 1 or 2")
    
def chart_triple_handler():
    if chart is not None:
        chart.get_triple_division()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_quadrant_handler():
    if chart is not None:
        chart.get_quadrant_division()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_lunar_phase_handler():
    if chart is not None:
        chart.get_lunar_phase()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_dignities_debilities_handler():
    if chart is not None:
        chart.get_dignities_debilities()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_rulerships_handler():
    if chart is not None:
        chart.get_rulerships()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_mutual_reception_handler():
    if chart is not None:
        chart.get_mutual_receptions()
    else: 
        print("Load or input chart data using menu options 1 or 2")

def chart_all_handler():
    if chart is not None:
        chart.get_house_cusps()
        chart.get_entities_in_signs_and_houses()
        chart.get_aspects()
        chart.get_polarity()
        chart.get_elements()
        chart.get_modes()
        chart.get_hemispheres()
        chart.get_triple_division()
        chart.get_quadrant_division()
        chart.get_lunar_phase()
        chart.get_dignities_debilities()
        chart.get_rulerships()
        chart.get_mutual_receptions()
    else: 
        print("Load or input chart data using menu options 1 or 2")