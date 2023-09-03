#
# astro
#

import sys  # sys.exit()

from signs import Signs
from houses import Houses

def print_menu():
    print("+---------------------------------------------------+")
    print("|          ---===  * Astro Menu *  ===---           |")
    print("+---------------------------------------------------+")
    print("| 1. Sign                                           |")
    print("| 2. Polarity                                       |")
    print("| 3. Mode                                           |")
    print("| 4. Element                                        |")
    print("| 5. Keywords for sign                              |")
    print("| 6. House                                          |")
    print("| 7. Keyeords for house                             |")
    print("| 0. Exit                                           |")
    print("+---------------------------------------------------+")

signs = Signs()
houses = Houses()

print_menu()
while (True):
    c = input("> ") 
    match(c):
        case "1" : # Sign
            s = input("Enter the sign name or number: ") 
            sign = Signs.get(Signs, s)
            Signs.print(Signs, sign)
        case "2" : # Polarity
            p = input("Enter the polarity (ex. +): ")
            signs.print_polarity(signs, p)
        case "3" : # Mode
            m = input("Enter the mode (ex. Cardinal): ")
            signs.print_mode(signs, m)
        case "4" :
            # Print the signs that match the given element
            e = input("Enter the element (ex. Fire): ")
            signs.print_element(signs, e)
        case "5" : 
            # Print the keywords for the given sign
            s = input("Enter the sign name or number: ") 
            sign = Signs.get(Signs, s)
            Signs.print_keywords(Signs, sign.sign)
        case "6" :
            i = input("Enter the house name or number: ") 
            h = Houses.get(Houses, i)
            Houses.print(Houses, h)
            pass
        case "7" :
            # Print the keywords for the given house
            h = input("Enter the house name or number: ")
            house = Houses.get(Houses, h)
            Houses.print_keywords(Houses, house.house)
        case "0" : 
            sys.exit()
        case _ :
            print("Invalid input, please try again!")
