#
# lunar_phases
#

import re
from constants import *
from keywords import Keywords
from lunar_phase import LunarPhase

class LunarPhases:

    new_moon_ = LunarPhase(NEW_MOON, WAXING, [0.0, 45.0], [0.0, 3.5], [CONJUNCTION, SEMISEXTILE, SEMISQUARE])
    crescent_ = LunarPhase(CRESCENT, WAXING, [45.0, 90.0], [3.5, 7.0], [SEMISQUARE, SEXTILE, SQUARE])
    firs_quarter_ = LunarPhase(FIRST_QUARTER, WAXING, [90.0, 135.0], [7.0, 10.5], [SQUARE, TRINE, SESQUIQUADRATE])
    gibbous_ = LunarPhase(GIBBOUS, WAXING, [135.0, 180.0], [10.5, 14.0], [SESQUIQUADRATE, QUINCUNX, OPPOSITION])
    full_moon_ = LunarPhase(FULL_MOON, WANNING, [180.0, 225.0], [14.0, 17.5], [OPPOSITION, QUINCUNX, SESQUIQUADRATE])
    disseminating_ = LunarPhase(DISSEMINATING, WANNING, [225.0, 270.0], [17.5, 21.0], [SESQUIQUADRATE, TRINE, SQUARE])
    last_quarter_ = LunarPhase(LAST_QUARTER, WANNING, [270.0, 315.0], [21.0, 24.5], [SQUARE, SEXTILE, SEMISQUARE])
    balsamic_ = LunarPhase(BALSAMIC, WANNING, [315.0, 0.0], [24.5, 28.0], [SEMISQUARE, SEMISEXTILE, CONJUNCTION])

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
            print("\n\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.lunar_phase_:
            LunarPhase.print(p)