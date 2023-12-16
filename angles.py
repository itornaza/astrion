#
# angles
#

import re
from angle import Angle
from constants import *

class Angles:
    
    asc_ = Angle(ASC, "Ascendant", "Due East")
    dsc_ = Angle(DSC, "Descendant", "Due West")
    mc_ = Angle(MC, ["Medium Coeli", "Midheaven"], "Due South")
    ic_ = Angle(IC, "Imum Coeli", "Due North")

    keywords_ = {
        ASC: [
            "The place of the rising sun and our birth and entry into the world",
            "How we approach the world and how the world sees us",
            "Beginnings – our birth moment",
            "Our momentum into life",
            "Our approach to initiation and how we start things Our body and appearance",
            "Our identity and journey of self discovery",
            "Liminal space – the great threshold"
        ],

        DSC: [
            "The journey through relationships What relationship means to us",
            "The experience we meet in relationship", 
            "How we approach relationships Qualities we admire in others", 
            "Attractions and what is attractive to us",
            "Our projections"
        ],

        MC: [
            "The middle of the heavens",
            "Our vocation, our calling",
            "Our career and the work we do",
            "Our place in the world and what we have to offer the world – our journey into this", 
            "Our achievement and attainment in the world",
            "Ambition which drives our achievement",
            "Our relationship with authority and with power",
            "The parental axis – mother/father",
            "How the world sees us – and what we project onto the world"
        ],

        IC: [
            "The bottom of the sky",
            "Our roots and foundations - anchorage",
            "Our home and experience of belonging",
            "Family life, early experience of home, and security",
            "Parental axis – father/mother – parental roots",
            "The past",
            "Private space",
            "Inner life, inner world, place of reflection and being, of mystery Place of the soul and soul-making",
            "The end of the matter",
            "... and may be unconscious"
        ]
    }

    angles_ = [asc_, dsc_, mc_, ic_]    

    def get(self, a):
        asc = re.compile(r'asc', re.IGNORECASE)
        dsc = re.compile(r'dsc', re.IGNORECASE)
        mc = re.compile(r'mc', re.IGNORECASE)
        ic = re.compile(r'ic', re.IGNORECASE)

        if asc.search(a) != None:
            angle = self.asc_
        elif dsc.search(a) != None:
            angle = self.dsc_
        elif mc.search(a) != None:
            angle = self.mc_
        elif ic.search(a) != None:
            angle = self.ic_
        else:
            return -1
        return angle

    def print(self, angle):
        Angle.print(angle)

    def print_keywords(self, angle_name):
        print("\nKeyword list for angle " + angle_name.upper() + ":\n")
        for k in Angles.keywords_[angle_name]:
            print("\t- " + k)

    # TODO: Integrate
    def print_all(self):
        for a in self.angles_:
            Angle.print(a)