#
# astrion
#

import sys
from utils import *

###############################################################################
#                                 HELPERS                                     #
###############################################################################

def exit_submenu(sub_choice: str, error_report: str) -> bool:
    """Helper function to exit submenus for code reuse. The return variable
    is used to break the while loop that the caller of this function is"""
    break_loop = False
    if sub_choice == "M" or sub_choice == "m" or \
       sub_choice == "Menu" or sub_choice ==  "menu": 
        print_menu()
        break_loop = True
    elif sub_choice == "S" or sub_choice == "s": 
        print_signs_ops_menu()
    elif sub_choice == "C" or sub_choice == "c": 
        print_calculator_menu() 
    elif sub_choice == "*":
        print_chart_menu()
    elif sub_choice == "Q" or sub_choice == "q" or \
            sub_choice == "Quit" or sub_choice == "quit": 
        os.system("clear")
        sys.exit(0)
    else: 
        print(error_report)
    return break_loop

###############################################################################
#                              CLI - MAIN LOOP                                #
###############################################################################

# Print all headers
print_header(0.2, 0.8)
print_menu()    

while (True):

    # Main menu
    menu_choice = input("> ") 
    print_menu()
    if menu_choice == M_KEYWORD:
        keywords_handler()
    elif menu_choice == M_PLANET: 
        planet_handler()
    elif menu_choice == M_SIGN: 
        sign_handler()
    elif menu_choice == M_HOUSE: 
        house_handler()
    elif menu_choice == M_ASPECT: 
        aspect_handler()
    elif menu_choice == M_ANGLE: 
        angle_handler()
    elif menu_choice == M_POLARITY: 
        polarity_handler()
    elif menu_choice == M_MODE: 
        mode_handler()
    elif menu_choice == M_ELEMENT: 
        element_handler()
    elif menu_choice == M_PATTERN:
        pattern_handler()
    elif menu_choice == M_LUNAR_PHASE:
        lunar_phase_handler()
    elif menu_choice == "M" or menu_choice == "m" or \
         menu_choice == "Menu" or menu_choice ==  "menu": 
        print_menu()
    elif menu_choice == "S" or menu_choice == "s": 

        # Signs Ops Menu
        print_signs_ops_menu() 
        while (True):
            sub_choice = input("> ")
            print_signs_ops_menu() 
            if sub_choice == "1":
                keywords_handler()
            elif sub_choice ==  "2": 
                sign_handler()
            elif sub_choice == "3": 
                compare_signs_handler()
            elif sub_choice == "4": 
                three_in_common_handler()
            elif sub_choice == "5": 
                polarity_and_mode_handler()
            elif sub_choice == "6": 
                mode_and_element_handler()
            elif sub_choice == "7": 
                element_and_polarity_handler()
            
            elif exit_submenu(sub_choice, E_SUB_MENU):
                break

    elif menu_choice == "C" or menu_choice == "c": 

        # Calculator Menu
        print_calculator_menu()
        while (True):
            sub_choice = input("> ")
            print_calculator_menu()
            if sub_choice == "1":
                planet_calculator_handler()
            elif sub_choice == "2":
                aspect_from_ecliptic_angless_handler()
            elif sub_choice == "3":
                ecliptic_to_polar_handler()
            elif sub_choice == "4":
                polar_to_ecliptic_handler()
            
            elif exit_submenu(sub_choice, E_CALC_MENU):
                break

    elif menu_choice == "*": 
        
        # Chart menu
        print_chart_menu()
        while(True):
            sub_choice = input("> ")
            print_chart_menu()
            if sub_choice == "1":
                chart_new_chart_handler()
            elif sub_choice == "2":
                chart_load_chart_handler()
            elif sub_choice == "3":
                chart_house_cusps_handler()
            elif sub_choice == "4":
                chart_placements_handler()
            elif sub_choice == "5":
                chart_aspects_handler()
            elif sub_choice == "6":
                chart_polarity_handler()
            elif sub_choice == "7":
                chart_elements_handler()
            elif sub_choice == "8":
                chart_mode_handler()
            elif sub_choice == "9":
                chart_hemispheres_handler()
            elif sub_choice == "10":
                chart_triple_handler()
            elif sub_choice == "11":
                chart_quadrant_handler()
            elif sub_choice == "12":
                chart_lunar_phase_handler()
            elif sub_choice == "13":
                chart_dignities_debilities_handler()
            elif sub_choice == "14":
                chart_rulerships_handler()
            elif sub_choice == "15":
                chart_mutual_reception_handler()
            elif sub_choice == "16":
                chart_all_handler()
            
            elif exit_submenu(sub_choice, E_CHART_MENU):
                break

    # Exit menu options
    elif menu_choice == "Q" or menu_choice == "q" or \
         menu_choice == "Quit" or menu_choice == "quit": 
        os.system("clear")
        break
    else: 
        print(E_MENU)
