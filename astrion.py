#
# astrion
#

from utils import *

# Print all headers
print_header(0.2, 0.8)
print_menu()

# Main loop
while (True):
    user_menu_input = input("> ") 
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
            compare_signs_handler()
        case "m" | "menu" | "Menu" : 
            print_menu()
        case "Q" | "q" | "Quit" | "quit" : 
            print_header(0.2, 1.4)
            break
        case _ : print("Invalid menu item!")
