#
# lunar-cycles
#

import re
from constants import *
from keywords import Keywords
from lunar-cycle import LunarCycle

class LunarCycles:

    new_moon_ = LunarCycle(NEW_MOON)

    def get(self, lc):
        new_moon = re.compile(r'new moon', re.IGNORECASE)

        if new_moon.search(lc):
            lunar_cycle = self.new_moon_
        else:
            return None
        
    def print(self, lunar_cycle):
        LunarCycle.print(lunar_cycle)
    
    def print_keywords(self, lunar_cycle_name):
        print("\nKeyword list for lunar cycle " + lunar_cycle_name.upper() + ":\n")
        for k in Keywords.lunar_cycle_[lunar_cycle_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.lunar_cycles_:
            LunarCycle.print(p)