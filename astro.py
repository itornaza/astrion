#
# astro
#

import sys  # sys.exit()
import os # os.system()
import time # time.sleep()

from planets import Planets
from signs import Signs
from houses import Houses
from aspects import Aspects
from elements import Elements

def print_header():
    os.system("clear")
    print("\n\n")
    print("    **        ****    ********   *****       ****     ")
    print(" **    **   ***         ***      **  ***   **    **   ")
    print(" **    **    ***        ***      **   **   **    **   ")
    print(" ********      ***      ***      ******    **    **   ")
    print(" **    **       ***     ***      **   **   **    **   ")
    print(" **    **     ***       ***      **   **   **    **   ")
    print(" **    **   ****        ***      **   **     ****     ")
    print("\n")
    time.sleep(0.6)

def print_menu():
    os.system("clear")
    print("+---------------------------------------------------+")
    print("|      ---===  * Astro Menu (v1.1.3) *  ===---      |")
    print("+---------------------------------------------------+")
    print("| 1.  Planet keywords                               |")
    print("| 2.  Sign keywords                                 |")
    print("| 3.  House keywords                                |")
    print("| 4.  Planet + Sign + House keywords                |")
    print("| 5.  Aspect keywords                               |")
    print("| 6.  Element keywords                              |")
    print("+------------------------+--------------------------+")
    print("| 7.  Planet             | 11.  Polarity            |")
    print("| 8.  Sign               | 12.  Mode                |")
    print("| 9.  House              | 13.  Element             |")
    print("| 10. Aspect             |                          |")
    print("+------------------------+--------------------------+")
    print("| m.  Menu               | e.  Exit                 |")
    print("+------------------------+--------------------------+")

planets = Planets()
signs = Signs()
houses = Houses()
aspects = Aspects()
elements = Elements()

print_header()

print_menu()
while (True):
    c = input("> ") 
    print_menu()
    match(c):
        case "1" : # Keywords for planet
            while (True): 
                p = input("Enter planet name or number: ") 
                planet = Planets.get(Planets, p)
                if planet == -1: 
                    break
                Planets.print_keywords(Planets, planet.name_)
                break
        
        case "2" : # Keywords for sign
            while (True):
                s = input("Enter sign name or number: ") 
                sign = Signs.get(Signs, s)
                if sign == -1: 
                    break
                Signs.print_keywords(Signs, sign.name_)
                break

        case "3" : # Keywords for house
            while (True):
                h = input("Enter house name or number: ")
                house = Houses.get(Houses, h)
                if house == -1: 
                    break
                Houses.print_keywords(Houses, house.name_)
                break

        case "4" : # Keywords for the given planet, sign, house
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

        case "5" : # Keywords for aspect
            while (True): 
                a = input("Enter aspect name or number: ") 
                aspect = Aspects.get(Aspects, a)
                if aspect == -1: 
                    break
                Aspects.print_keywords(Aspects, aspect.name_)
                break

        case "6" : # Keywords for element
            while (True):
                e = input("Enter element name or number: ")
                element = Elements.get(Elements, e)
                if element == -1: 
                    break
                Elements.print_keywords(Elements, element.name_)
                break

        case "7" : # Planet
            while (True):
                p = input("Enter planet name or number: ") 
                planet = Planets.get(Planets, p)
                if planet == -1: 
                    break
                Planets.print(Planets, planet)
                break
        
        case "8" : # Sign
            while (True):
                s = input("Enter sign name or number: ") 
                sign = Signs.get(Signs, s)
                if sign == -1: 
                    break
                Signs.print(Signs, sign)
                break
        
        case "12" : # House
            while (True):
                h = input("Enter house name or number: ") 
                house = Houses.get(Houses, h)
                if house == -1: 
                    break
                Houses.print(Houses, house)
                break
       
        case "13" : # Aspect
            while (True):
                a = input("Enter aspect name or number: ") 
                aspect = Aspects.get(Aspects, a)
                if aspect == -1: 
                    break
                Aspects.print(Aspects, aspect)
                break

        case "9" : # Polarity
            p = input("Enter polarity (ex. +): ")
            Signs.print_polarity(Signs, p)
        
        case "10" : # Mode
            m = input("Enter mode (ex. Cardinal): ")
            Signs.print_mode(Signs, m)
        
        case "11" : # Element
            while (True):
                e = input("Enter element name or number: ") 
                element = Elements.get(Elements, e)
                if element == -1: 
                    break
                Elements.print(Elements, element)
                Signs.print_element(Signs, e)
                break

        case "m" | "menu" | "Menu" : # Show menu
            print_menu()

        case "0" | "e" | "E" | "Exit" | "exit" : # Exit program
            print("\n\nBye-bye!\n\n")
            sys.exit()
       
        case _ : # Default
            print("Invalid input, please try again!")

