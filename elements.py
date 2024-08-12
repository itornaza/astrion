#
# elements
#

import re
from constants import *
from keywords import Keywords
from element import Element

class Elements:
    
    fire_ = Element(FIRE, "Imagination", "Calcinatio", "Choleric", "Intuition", "Wands", "Conception", "So much confidence")
    earth_ = Element(EARTH, "Demonstration", "Coagulatio", "Melacholic", "Sensation", "Pentacles", "Incarnation", "So much security")
    air_ = Element(AIR, "Inteligence", "Sublimatio", "Sanguine", "Thinking", "Swords", "Separation and relationship", "So much thinking")
    water_ = Element(WATER, "Opinion", "Solutio", "Phlegmatic", "Feeling", "Cups", "Merging", "So much emotions")

    def get(self, e):
        fire = re.compile(rf'^\s*{FIRE}\s*$', re.IGNORECASE)
        earth = re.compile(rf'^\s*{EARTH}\s*$', re.IGNORECASE)
        air = re.compile(rf'^\s*{AIR}\s*$', re.IGNORECASE)
        water = re.compile(rf'^\s*{WATER}\s*$', re.IGNORECASE)
        
        if fire.fullmatch(e):
            element = self.fire_
        elif earth.fullmatch(e):
            element = self.earth_
        elif air.fullmatch(e):
            element = self.air_
        elif water.fullmatch(e):
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
