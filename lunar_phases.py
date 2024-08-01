#
# lunar_phases
#

import re
from constants import *
from keywords import Keywords
from lunar_phase import LunarPhase

class LunarPhases:

    new_moon_ = LunarPhase(NEW_MOON, WAXING, [NA], [NA], [NA])
    crescent_ = LunarPhase(CRESCENT, WAXING, [NA], [NA], [NA])
    firs_quarter_ = LunarPhase(FIRST_QUARTER, WAXING, [NA], [NA], [NA])
    gibbous_ = LunarPhase(GIBBOUS, WAXING, [NA], [NA], [NA])
    full_moon_ = LunarPhase(FULL_MOON, WANNING, [NA], [NA], [NA])
    disseminating_ = LunarPhase(DISSEMINATING, WANNING, [NA], [NA], [NA])
    last_quarter_ = LunarPhase(LAST_QUARTER, WANNING, [NA], [NA], [NA])
    balsamic_ = LunarPhase(BALSAMIC, WANNING, [NA], [NA], [NA])

    def get(self, lp):
        new_moon = re.compile(r'new moon', re.IGNORECASE)
        crescent = re.compile(r'crescent', re.IGNORECASE)
        first_quarter = re.compile(r'first quarter', re.IGNORECASE)
        gibbous = re.compile(r'gibbous', re.IGNORECASE)
        full_moon = re.compile(r'full moon', re.IGNORECASE)
        disseminating = re.compile(r'disseminating', re.IGNORECASE)
        last_quarter = re.compile(r'last quarter', re.IGNORECASE)
        balsamic = re.compile(r'balsamic', re.IGNORECASE)

        if new_moon.search(lp):
            lunar_phase = self.new_moon_
        elif crescent.search(lp):
            lunar_phase = self.crescent_
        elif first_quarter.search(lp):
            lunar_phase = self.firs_quarter_
        elif gibbous.search(lp):
            lunar_phase = self.gibbous_
        elif full_moon.search(lp):
            lunar_phase = self.full_moon_
        elif disseminating.search(lp):
            lunar_phase = self.disseminating_
        elif last_quarter.search(lp):
            lunar_phase = self.last_quarter_
        elif balsamic.search(lp):
            lunar_phase = self.balsamic_
        else:
            return None
        return lunar_phase
        
    def print(self, lunar_phase):
        LunarPhase.print(lunar_phase)
    
    def print_keywords(self, lunar_phase_name):
        print("\nKeyword list for lunar phase " + lunar_phase_name.upper() + ":\n")
        for k in Keywords.lunar_phases_[lunar_phase_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.lunar_phase_:
            LunarPhase.print(p)