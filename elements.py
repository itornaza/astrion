#
# elements
#

import re
from element import Element
from constants import *

class Elements:
    
    fire_ = Element(FIRE, "Imagination", "Calcinatio", "Choleric", "Intuition", "Wands", "Conception", "So much confidence")
    earth_ = Element(EARTH, "Demonstration", "Coagulatio", "Melacholic", "Sensation", "Pentacles", "Incarnation", "So much security")
    air_ = Element(AIR, "Inteligence", "Sublimatio", "Sanguine", "Thinking", "Swords", "Separation and relationship", "So much thinking")
    water_ = Element(WATER, "Opinion", "Solutio", "Phlegmatic", "Feeling", "Cups", "Merging", "So much emotions")

    keywords_ = {
        FIRE: ["enthusiastic", "optimistic", "confident", "dramatic", "warm"],
        EARTH: ["practical", "sensible", "sensual", "realistic", "reliable", "down to earth"],
        AIR: ["civilised", "detaches", "objective", "impersonal", "rational", "verbal"],
        WATER: ["sympathetic", "receptive", "imaginative", "emotional", "intuitive"]
    }

    elements_ = [fire_, earth_, air_, water_]    

    def get(self, e):
        fire = re.compile(r'fir', re.IGNORECASE)
        earth = re.compile(r'ear', re.IGNORECASE)
        air = re.compile(r'air', re.IGNORECASE)
        water = re.compile(r'wat', re.IGNORECASE)

        if fire.search(e) != None:
            element = self.fire_
        elif earth.search(e) != None:
            element = self.earth_
        elif air.search(e) != None:
            element = self.air_
        elif water.search(e) != None:
            element = self.water_
        else:
            return -1
        return element

    def print(self, element):
        Element.print(element)

    def print_keywords(self, element_name):
        print("\nKeyword list for element " + element_name.upper() + ":\n")
        for k in Elements.keywords_[element_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for e in self.elements_:
            Element.print(e)