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
    time.sleep(0.2)
    print("                                >>> created by ion-   ")
    print("\n")
    time.sleep(0.8)

def print_menu():
    os.system("clear")
    print("+---------------------------------------------------+")
    print("|      ---===  * Astro Menu (v1.1.3) *  ===---      |")
    print("+---------------------------------------------------+")
    print("| 1.  Keywords                                      |")
    print("+------------------------+--------------------------+")
    print("| 2.  Planet             | 6.  Polarity             |")
    print("| 3.  Sign               | 7.  Mode                 |")
    print("| 4.  House              | 8.  Element              |")
    print("| 5. Aspect              |                          |")
    print("+------------------------+--------------------------+")
    print("| m.  Menu               | 0, e, q.  Exit           |")
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
        case "1" : # Generic keyword list search         
            user_input = input("Enter search terms separated by space:\n")
            user_input_list = user_input.split()
            for term in user_input_list:

                is_valid_input = 5

                valid_term = Planets.get(Planets, term)
                if valid_term != -1: 
                    Planets.print_keywords(Planets, valid_term.name_)
                else:
                    is_valid_input -= 1
                
                valid_term = Signs.get(Signs, term)
                if valid_term != -1: 
                    Signs.print_keywords(Signs, valid_term.name_)
                else:
                    is_valid_input -= 1
                
                valid_term = Houses.get(Houses, term)
                if valid_term != -1: 
                    Houses.print_keywords(Houses, valid_term.name_)
                else:
                    is_valid_input -= 1
                
                valid_term = Aspects.get(Aspects, term)
                if valid_term != -1: 
                    Aspects.print_keywords(Aspects, valid_term.name_)
                else:
                    is_valid_input -= 1
                
                valid_term = Elements.get(Elements, term)
                if valid_term != -1: 
                    Elements.print_keywords(Elements, valid_term.name_)
                else:
                    is_valid_input -= 1

                if is_valid_input == 0:
                    print("\nInvalid input: " + term.upper())

        case "2" : # Planet
            while (True):
                p = input("Enter planet name or number: ") 
                planet = Planets.get(Planets, p)
                if planet == -1: 
                    print("Invalid planet input!")
                    break
                Planets.print(Planets, planet)
                break
        
        case "3" : # Sign
            while (True):
                s = input("Enter sign name or number: ") 
                sign = Signs.get(Signs, s)
                if sign == -1: 
                    print("Invalid sign input!")
                    break
                Signs.print(Signs, sign)
                break
        
        case "4" : # House
            while (True):
                h = input("Enter house name or number: ") 
                house = Houses.get(Houses, h)
                if house == -1: 
                    print("Invalid house input!")
                    break
                Houses.print(Houses, house)
                break
       
        case "5" : # Aspect
            while (True):
                a = input("Enter aspect name or number: ") 
                aspect = Aspects.get(Aspects, a)
                if aspect == -1: 
                    print("Invalid aspect input!")
                    break
                Aspects.print(Aspects, aspect)
                break

        case "6" : # Polarity
            p = input("Enter polarity (ex. +): ")
            Signs.print_polarity(Signs, p)
        
        case "7" : # Mode
            m = input("Enter mode (ex. Cardinal): ")
            Signs.print_mode(Signs, m)
        
        case "8" : # Element
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

        case "0" | "e" | "E" | "q" | "Q" | "Exit" | "exit" : # Exit program
            print("\n\nBye-bye!\n\n")
            sys.exit()
       
        case _ : # Default
            print("Invalid input, please try again!")
