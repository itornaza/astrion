#
# lunar-cycles
#

import re
from constants import *
from keywords import Keywords
from lunar-cycle import LunarCycle

class LunarCycles:

    new_moon_ = LunarCycle(NEW_MOON, WAXING, NA, NA, [NA])
    crescent_ = LunarCycle(CRESCENT, WAXING, NA, NA, [NA])
    firs_quarter_ = LunarCycle(FIRST_QUARTER, WAXING, NA, NA, [NA])
    gibbous_ = LunarCycle(GIBBOUS, WAXING, NA, NA, [NA])
    full_moon_ = LunarCycle(FULL_MOON, WANNING, NA, NA, [NA])
    disseminating_ = LunarCycle(DISSEMINATING, WANNING, NA, NA, [NA])
    last_quarter_ = LunarCycle(LAST_QUARTER, WANNING, NA, NA, [NA])
    balsamic_ = LunarCycle(BALSAMIC, WANNING, NA, NA, [NA])

    def get(self, lc):
        new_moon = re.compile(r'new moon', re.IGNORECASE)
        crescent = re.compile(r'crescent', re.IGNORECASE)
        first_quarter = re.compile(r'first quarter', re.IGNORECASE)
        gibbous = re.compile(r'gibbous', re.IGNORECASE)
        full_moon = re.compile(r'full moon', re.IGNORECASE)
        disseminating = re.compile(r'disseminating', re.IGNORECASE)
        last_quarter = re.compile(r'last quarter', re.IGNORECASE)
        balsamic = re.compile(r'balsamic', re.IGNORECASE)

        if new_moon.search(lc):
            lunar_cycle = self.new_moon_
        elif crescent.search(lc):
            lunar_cycle = self.crescent_
        elif first_quarter.search(lc):
            lunar_cycle = self.firs_quarter_
        elif gibbous.search(lc):
            lunar_cycle = self.gibbous_
        elif full_moon.search(lc):
            lunar_cycle = self.full_moon_
        elif disseminating.search(lc):
            lunar_cycle = self.disseminating_
        elif last_quarter.search(lc):
            lunar_cycle = self.last_quarter_
        elif balsamic.search(lc):
            lunar_cycle = self.balsamic_
        else:
            return None
        return lunar_cycle
        
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