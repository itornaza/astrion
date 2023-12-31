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
    elements_ = [fire_, earth_, air_, water_]    

    def get(self, e):
        fire = re.compile(r'fire', re.IGNORECASE)
        earth = re.compile(r'ear', re.IGNORECASE)
        air = re.compile(r'air', re.IGNORECASE)
        water = re.compile(r'wat', re.IGNORECASE)
        
        element = None
        if fire.search(e):
            element = self.fire_
        elif earth.search(e):
            element = self.earth_
        elif air.search(e):
            element = self.air_
        elif water.search(e):
            element = self.water_
        return element

    def print(self, element):
        Element.print(element)

    def print_keywords(self, element_name):
        print("\nKeyword list for element " + element_name.upper() + ":\n")
        for k in Keywords.elements_[element_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for e in self.elements_:
            Element.print(e)