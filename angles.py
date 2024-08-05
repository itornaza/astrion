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
    angles_ = [asc_, dsc_, mc_, ic_]  

    def get(self, a):
        asc = re.compile(rf'{ASC}', re.IGNORECASE)
        dsc = re.compile(rf'{DSC}', re.IGNORECASE)
        mc = re.compile(rf'{MC}', re.IGNORECASE)
        ic = re.compile(rf'{IC}', re.IGNORECASE)

        angle = None
        if asc.fullmatch(a):
            angle = self.asc_
        elif dsc.fullmatch(a):
            angle = self.dsc_
        elif mc.fullmatch(a):
            angle = self.mc_
        elif ic.fullmatch(a):
            angle = self.ic_
        return angle

    def print(self, angle):
        Angle.print(angle)

    def print_keywords(self, angle_name):
        print("\nKeyword list for angle " + angle_name.upper() + ":\n")
        for k in Keywords.angles_[angle_name]:
            print("\t- " + k)

    # TODO: Integrate
    def print_all(self):
        for a in self.angles_:
            Angle.print(a)