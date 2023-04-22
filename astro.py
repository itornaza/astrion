
import sys  # sys.exit()

from sign import Sign
from zodiac import Zodiac

def print_menu():
    print("+---------------------------------------------------+")
    print("|          ---===  * Astro Menu *  ===---           |")
    print("+---------------------------------------------------+")
    print("| 1. Sign                                           |")
    print("| 2. Polarity                                       |")
    print("| 3. Mode                                           |")
    print("| 4. Element                                        |")
    print("| 5.                                                |")
    print("| 6.                                                |")
    print("| 0. Exit                                           |")
    print("+---------------------------------------------------+")

# Main    

# z.print_all(z)
# z.print_polarity(z, "+")
# z.print_arc(z, "Libra")
# z.print_polarity_element(z, "+", "Fire")
# z.print_polarity_mode(z, "-", "Fixed")
# z.print_element_mode(z, "Fire", "Cardinal")
# z.print_2_commons(z, z.aries)


z = Zodiac

print_menu()
while (True):
    c = input("> ") 
    match(c):
        case "1" : # Sign
            s = input("Enter the sign (ex. Taurus): ") 
            sign = z.get_sign(z, s)
            Sign.print(sign)
        case "2" : # Polarity
            p = input("Enter the polarity (ex. +): ")
            Zodiac.print_polarity(Zodiac, p)
        case "3" : # Mode
            m = input("Enter the mode (ex. Cardinal): ")
            Zodiac.print_mode(Zodiac, m)
        case "4" :
            # Print the signs that match the given element
            e = input("Enter the element (ex. Fire): ")
            Zodiac.print_element(Zodiac, e)
        case "5" : 
            print(5)
        case "6" :
            print(6)
        case "0" : 
            sys.exit()
        case _ :
            print("Invalid input, please try again!")
