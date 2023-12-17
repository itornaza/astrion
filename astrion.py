#
# astrion
#

import sys
from utils import *

# Print all headers
print_header(0.2, 0.8)
print_menu()    

# Main loop
while (True):
    user_menu_input = input("> ") 
    
    # Main menu
    print_menu()

    match(user_menu_input):
        case "1" : 
            keywords_handler()
        case "2" : 
            planet_handler()
        case "3" : 
            sign_handler()
        case "4" : 
            house_handler()
        case "5" : 
            aspect_handler()
        case "6" : 
            angle_handler()
        case "7" : 
            polarity_handler()
        case "8" : 
            mode_handler()
        case "9" : 
            element_handler()
        case "10": 

            # Signs Ops Menu
            print_signs_ops_menu() 
            while (True):
                user_sign_ops_menu_input = input("> ")
                print_signs_ops_menu() 
                match(user_sign_ops_menu_input):
                    case "1" : 
                        keywords_handler()
                    case "2" : 
                        sign_handler()
                    case "3" : 
                        compare_signs_handler()
                    case "4" : 
                        three_in_common_handler()
                    case "5" : 
                        polarity_and_mode_handler()
                    case "6" : 
                        mode_and_element_handler()
                    case "7" : 
                        element_and_polarity_handler()
                    case "8" :
                        Signs.print_all(Signs)
                    case "M" | "m" | "Menu" | "menu" : 
                        print_menu()
                    case "S" | "s" : 
                        print_signs_ops_menu() 
                    case "Q" | "q" | "Quit" | "quit" : 
                        print_header(0.2, 1.4)
                        sys.exit(0)
                    case "B" | "b" | "Back" | "back" : 
                        print_menu()
                    case _ : 
                        print("Invalid sign ops menu item!")

        case "M" | "m" | "Menu" | "menu" : 
            print_menu()
        case "S" | "s" : 
            print_signs_ops_menu() 
        case "Q" | "q" | "Quit" | "quit" : 
            print_header(0.2, 1.4)
            break
        case _ : 
            print("Invalid menu item!")
