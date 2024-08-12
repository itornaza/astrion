#
# angles
#

import re
from constants import *
from keywords import Keywords
from angle import Angle

class Angles:
    
    asc_ = Angle(ASC, "Ascendant", "Due East")
    dsc_ = Angle(DSC, "Descendant", "Due West")
    mc_ = Angle(MC, ["Medium Coeli", "Midheaven"], "Due South")
    ic_ = Angle(IC, "Imum Coeli", "Due North")

    def get(self, input):
        asc = re.compile(rf'^\s*{ASC}\s*$', re.IGNORECASE)
        dsc = re.compile(rf'^\s*{DSC}\s*$', re.IGNORECASE)
        mc = re.compile(rf'^\s*{MC}\s*$', re.IGNORECASE)
        ic = re.compile(rf'^\s*{IC}\s*$', re.IGNORECASE)

        if asc.fullmatch(input):
            angle = self.asc_
        elif dsc.fullmatch(input):
            angle = self.dsc_
        elif mc.fullmatch(input):
            angle = self.mc_
        elif ic.fullmatch(input):
            angle = self.ic_
        else:
            return None
        return angle

    def print(self, angle):
        Angle.print(angle)

    def print_keywords(self, keyword):
        print("\nKeyword list for angle " + keyword.upper() + ":\n")
        for k in Keywords.angles_[keyword]:
            print("\t- " + k)
