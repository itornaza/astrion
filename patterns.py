#
# planets
#

import re
from constants import *
from keywords import Keywords
from pattern import Pattern

class Patterns:

    t_square_ = Pattern("T-square")
    grand_cross_ = Pattern("Grand cross")
    finger_of_world_ = Pattern("Finger of the world")
    hard_rectangle_ = Pattern("Hard rectangle")
    grand_trine_ = Pattern("Grand trine")
    minor_grand_trine_ = Pattern("Minor grand trine")
    kite_ = Pattern("Kite")
    yod_ = Pattern("Yod, aka Finger of fate")
    mystic_rectangle_ = Pattern("Mystic rectangle")
    grand_sextile_ = Pattern("Grand sextile")
    stellium_ = Pattern("Stellium")
    
    patterns_ = [t_square_, grand_cross_, finger_of_world_, hard_rectangle_, 
                 grand_trine_, minor_grand_trine_, kite_, yod_, mystic_rectangle_, 
                 grand_sextile_, stellium_]

    def get(self, p):
        t_square = re.compile(r't-sq', re.IGNORECASE)
        
        if t_square.search(p):
            pattern = self.t_square_
        else:
            return None
        return pattern

    def print(self, pattern):
        Pattern.print(pattern)

    def print_keywords(self, pattern_name):
        print("\nKeyword list for pattern " + pattern_name.upper() + ":\n")
        for k in Keywords.patterns_[pattern_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.patterns_:
            Pattern.print(p)