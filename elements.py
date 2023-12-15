#
# elements
#

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
        match(e):
            case "Fire" | "fire" : 
                element = self.fire_
            case "Earth" | "earth" : 
                element = self.earth_
            case "Air" | "air" : 
                element = self.air_
            case "Water" | "water" : 
                element = self.water_
            case _ :
                return -1
        return element

    def print_all(self):
        for e in self.elements_:
            Element.print(e)

    def print(self, element):
        Element.print(element)

    def print_keywords(self, element_name):
        print("\nKeyword list for element " + element_name.upper() + ":\n")
        for k in Elements.keywords_[element_name]:
            print("\t- " + k)