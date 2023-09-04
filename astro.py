#
# astro
#

import sys  # sys.exit()
import os # os.system()

from planets import Planets
from signs import Signs
from houses import Houses

def print_menu():
    os.system("clear")
    print("+---------------------------------------------------+")
    print("|          ---===  * Astro Menu *  ===---           |")
    print("+---------------------------------------------------+")
    print("| 1. Planet                                         |")
    print("| 2. Keywords for planet                            |")
    print("| 3. Sign                                           |")
    print("| 4. Polarity                                       |")
    print("| 5. Mode                                           |")
    print("| 6. Element                                        |")
    print("| 7. Keywords for sign                              |")
    print("| 8. House                                          |")
    print("| 9. Keywords for house                             |")
    print("| 10. Keywords for planet, sign and house           |")
    print("| 0. Exit                                           |")
    print("+---------------------------------------------------+")

planets = Planets()
signs = Signs()
houses = Houses()

print_menu()
while (True):
    c = input("> ") 
    print_menu()
    match(c):
        case "1" : # Planet
            p = input("Enter planet name or number: ") 
            planet = Planets.get(Planets, p)
            Planets.print(Planets, planet)
        
        case "2" : # Keywords for planet
            p = input("Enter planet name or number: ") 
            planet = Planets.get(Planets, p)
            Planets.print_keywords(Planets, planet.name_)
        
        case "3" : # Sign
            s = input("Enter sign name or number: ") 
            sign = Signs.get(Signs, s)
            Signs.print(Signs, sign)
        
        case "4" : # Polarity
            p = input("Enter polarity (ex. +): ")
            Signs.print_polarity(Signs, p)
        
        case "5" : # Mode
            m = input("Enter mode (ex. Cardinal): ")
            Signs.print_mode(Signs, m)
        
        case "6" : # Element
            e = input("Enter element (ex. Fire): ")
            Signs.print_element(Signs, e)
        
        case "7" : # Keywords for the given sign
            s = input("Enter sign name or number: ") 
            sign = Signs.get(Signs, s)
            Signs.print_keywords(Signs, sign.name_)
        
        case "8" : # House
            i = input("Enter house name or number: ") 
            h = Houses.get(Houses, i)
            Houses.print(Houses, h)
            pass
        
        case "9" : # Keywords for the given house
            h = input("Enter house name or number: ")
            house = Houses.get(Houses, h)
            Houses.print_keywords(Houses, house.name_)
        
        case "10" : # Keywords for the given planet, sign, house
            # Get user input
            p = input("Enter planet name or number: ") 
            s = input("Enter sign name or number: ") 
            h = input("Enter house name or number: ")
            
            # Get the foundations
            planet = Planets.get(Planets, p)
            sign = Signs.get(Signs, s)
            house = Houses.get(Houses, h)
            
            # Print results
            print("\n")
            Planets.print_keywords(Planets, planet.name_)
            print("\n")
            Signs.print_keywords(Signs, sign.name_)
            print("\n")
            Houses.print_keywords(Houses, house.name_)
            print("\n")
       
        case "c" | "clear" : # Clear terminal
            print_menu()

        case "0" | "e" | "exit" : # Exit program
            sys.exit()
       
        case _ : # Default
            print("Invalid input, please try again!")

