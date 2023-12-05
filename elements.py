#
# elements
#

from element import Element

class Elements:
    
    # Define all twelve signs using the Sign class
    fire_ = Element("Fire", "Imagination", "Calcinatio", "Choleric", "Intuition", "Wands", 
                    "Conception", "So much confidence")
    earth_ = Element("Earth", "Demonstration", "Coagulatio", "Melacholic", "Sensation", "Pentacles", 
                     "Incarnation", "So much security")
    air_ = Element("Air", "Inteligence", "Sublimatio", "Sanguine", "Thinking", "Swords", 
                   "Separation and relationship", "So much thinking")
    water_ = Element("Water", "Opinion", "Solutio", "Phlegmatic", "Feeling", "Cups", 
                     "Merging", "So much emotions")

    keywords_ = {
        "Fire": ["enthusiastic", "optimistic", "confident", "dramatic", "warm"],
        "Earth": ["practical", "sensible", "sensual", "realistic", "reliable", "down to earth"],
        "Air": ["civilised", "detaches", "objective", "impersonal", "rational", "verbal"],
        "Water": ["sympathetic", "receptive", "imaginative", "emotional", "intuitive"]
    }

    elements_ = [fire_, earth_, air_, water_]    

    def get(self, e):
        match(e):
            case "Fire" | "1" : 
                element = self.fire_
            case "Earth" | "2" : 
                element = self.earth_
            case "Air" | "3" : 
                element = self.air_
            case "Water" | "4" : 
                element = self.water_
            case _ :
                print("Invalid element input!")
                return -1
        return element

    def print_all(self):
        for e in self.elements_:
            Element.print(e)

    # Wrapper for the Element.print method
    def print(self, element):
        Element.print(element)

    def print_keywords(self, element_name):
        print("\nKeyword list for element " + element_name.upper() + ":\n")
        for k in Elements.keywords_[element_name]:
            print("\t- " + k)