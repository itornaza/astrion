#
# lunar_phases
#

import re
from constants import *
from keywords import Keywords

class LunarPhase:

    def __init__(self, name, phase, arc_ahead_of_sun, days_ahead_of_sun, aspects):
        self.name_ = name
        self.phase_ = phase
        self.arc_ahead_of_sun_ = arc_ahead_of_sun # From-to angles ahead
        self.days_ahead_of_sun_ = days_ahead_of_sun # From-to days ahead
        self.aspects_ = aspects 

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nPhase\t\t\t:\t", self.phase_, 
              "\nArc ahead\t\t:\t", self.arc_ahead_of_sun_, 
              "\nDays ahead\t\t:\t", self.days_ahead_of_sun_, 
              "\nAspects\t\t\t:\t", self.aspects_, "\n")

class LunarPhases:

    new_moon_ = LunarPhase(NEW_MOON, WAXING, [0.0, 45.0], [0.0, 3.5], [CONJUNCTION, SEMISEXTILE, SEMISQUARE])
    crescent_ = LunarPhase(CRESCENT, WAXING, [45.0, 90.0], [3.5, 7.0], [SEMISQUARE, SEXTILE, SQUARE])
    first_quarter_ = LunarPhase(FIRST_QUARTER, WAXING, [90.0, 135.0], [7.0, 10.5], [SQUARE, TRINE, SESQUIQUADRATE])
    gibbous_ = LunarPhase(GIBBOUS, WAXING, [135.0, 180.0], [10.5, 14.0], [SESQUIQUADRATE, QUINCUNX, OPPOSITION])
    full_moon_ = LunarPhase(FULL_MOON, WANNING, [180.0, 225.0], [14.0, 17.5], [OPPOSITION, QUINCUNX, SESQUIQUADRATE])
    disseminating_ = LunarPhase(DISSEMINATING, WANNING, [225.0, 270.0], [17.5, 21.0], [SESQUIQUADRATE, TRINE, SQUARE])
    last_quarter_ = LunarPhase(LAST_QUARTER, WANNING, [270.0, 315.0], [21.0, 24.5], [SQUARE, SEXTILE, SEMISQUARE])
    balsamic_ = LunarPhase(BALSAMIC, WANNING, [315.0, 0.0], [24.5, 28.0], [SEMISQUARE, SEMISEXTILE, CONJUNCTION])

    lunar_phases_ = [new_moon_, crescent_, first_quarter_, gibbous_,
                     full_moon_, disseminating_, last_quarter_, balsamic_]

    def get(self, input):
        new_moon = re.compile(rf'^\s*{NEW_MOON}\s*$', re.IGNORECASE)
        crescent = re.compile(rf'^\s*{CRESCENT}\s*$', re.IGNORECASE)
        first_quarter = re.compile(rf'^\s*{FIRST_QUARTER}\s*$', re.IGNORECASE)
        gibbous = re.compile(rf'^\s*{GIBBOUS}\s*$', re.IGNORECASE)
        full_moon = re.compile(rf'^\s*{FULL_MOON}\s*$', re.IGNORECASE)
        disseminating = re.compile(rf'^\s*{DISSEMINATING}\s*$', re.IGNORECASE)
        last_quarter = re.compile(rf'^\s*{LAST_QUARTER}\s*$', re.IGNORECASE)
        balsamic = re.compile(rf'^\s*{BALSAMIC}\s*$', re.IGNORECASE)

        if new_moon.fullmatch(input):
            lunar_phase = self.new_moon_
        elif crescent.fullmatch(input):
            lunar_phase = self.crescent_
        elif first_quarter.fullmatch(input):
            lunar_phase = self.first_quarter_
        elif gibbous.fullmatch(input):
            lunar_phase = self.gibbous_
        elif full_moon.fullmatch(input):
            lunar_phase = self.full_moon_
        elif disseminating.fullmatch(input):
            lunar_phase = self.disseminating_
        elif last_quarter.fullmatch(input):
            lunar_phase = self.last_quarter_
        elif balsamic.fullmatch(input):
            lunar_phase = self.balsamic_
        else:
            return None
        return lunar_phase
        
    def get_from_angle(self, angle: int):
        if angle >= self.new_moon_.arc_ahead_of_sun_[0] and angle < self.new_moon_.arc_ahead_of_sun_[1]:
            return self.new_moon_
        elif angle >= self.crescent_.arc_ahead_of_sun_[0] and angle < self.crescent_.arc_ahead_of_sun_[1]:
            return self.crescent_
        elif angle >= self.first_quarter_.arc_ahead_of_sun_[0] and angle < self.first_quarter_.arc_ahead_of_sun_[1]:
            return self.first_quarter_
        elif angle >= self.gibbous_.arc_ahead_of_sun_[0] and angle < self.gibbous_.arc_ahead_of_sun_[1]:
            return self.gibbous_
        elif angle >= self.full_moon_.arc_ahead_of_sun_[0] and angle < self.full_moon_.arc_ahead_of_sun_[1]:
            return self.full_moon_
        elif angle >= self.disseminating_.arc_ahead_of_sun_[0] and angle < self.disseminating_.arc_ahead_of_sun_[1]:
            return self.disseminating_
        elif angle >= self.last_quarter_.arc_ahead_of_sun_[0] and angle < self.last_quarter_.arc_ahead_of_sun_[1]:
            return self.last_quarter_
        elif angle >= self.balsamic_.arc_ahead_of_sun_[0] and angle < self.balsamic_.arc_ahead_of_sun_[1]:
            return self.balsamic_

    def print(self, lunar_phase):
        LunarPhase.print(lunar_phase)
    
    def print_keywords(self, keyword):
        print("\nKeyword list for lunar phase " + keyword.upper() + ":\n")
        for k in Keywords.lunar_phases_[keyword]:
            print("\t- " + k)
