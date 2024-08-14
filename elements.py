#
# elements
#

import re
from constants import *
from keywords import Keywords

class Element:

    def __init__(self, element, plato, alchemy, humor, psychology, tarot, 
                 function, predominance):
        self.name_ = element
        self.plato_ = plato
        self.alchemy_ = alchemy
        self.humor_ = humor
        self.psychology_ = psychology
        self.tarot_ = tarot
        self.function_ = function
        self.predominance_ = predominance
        
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(),
              "\nPlato\t\t\t:\t", self.plato_, 
              "\nAlchemy\t\t\t:\t", self.alchemy_, 
              "\nHumor\t\t\t:\t", self.humor_, 
              "\nPsychology\t\t:\t", self.psychology_, 
              "\nTarot\t\t\t:\t", self.tarot_,
              "\nFunction\t\t:\t", self.function_,
              "\nPredominance\t\t:\t", self.predominance_)

class Elements:
    
    fire_ = Element(FIRE, "Imagination", "Calcinatio", "Choleric", "Intuition", "Wands", "Conception", "So much confidence")
    earth_ = Element(EARTH, "Demonstration", "Coagulatio", "Melacholic", "Sensation", "Pentacles", "Incarnation", "So much security")
    air_ = Element(AIR, "Inteligence", "Sublimatio", "Sanguine", "Thinking", "Swords", "Separation and relationship", "So much thinking")
    water_ = Element(WATER, "Opinion", "Solutio", "Phlegmatic", "Feeling", "Cups", "Merging", "So much emotions")

    elements_ = [fire_, earth_, air_, water_]

    def get(self, input):
        fire = re.compile(rf'^\s*{FIRE}\s*$', re.IGNORECASE)
        earth = re.compile(rf'^\s*{EARTH}\s*$', re.IGNORECASE)
        air = re.compile(rf'^\s*{AIR}\s*$', re.IGNORECASE)
        water = re.compile(rf'^\s*{WATER}\s*$', re.IGNORECASE)
        
        if fire.fullmatch(input):
            element = self.fire_
        elif earth.fullmatch(input):
            element = self.earth_
        elif air.fullmatch(input):
            element = self.air_
        elif water.fullmatch(input):
            element = self.water_
        else:
            return None
        return element

    def print(self, element):
        Element.print(element)

    def print_keywords(self, keyword):
        print("\nKeyword list for element " + keyword.upper() + ":\n")
        for k in Keywords.elements_[keyword]:
            print("\t- " + k)
