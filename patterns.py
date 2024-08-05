#
# patterns
#

import re
from constants import *
from keywords import Keywords
from pattern import Pattern

class Patterns:

    t_square_ = Pattern(T_SQUARE, HARD, [SQUARE, OPPOSITION], [CARDINAL, FIXED, MUTABLE])
    grand_cross_ = Pattern(GRAND_CROSS, HARD, [SQUARE, OPPOSITION], [CARDINAL, FIXED, MUTABLE])
    finger_of_world_ = Pattern(FINGER_OF_WORLD, HARD, [SESQUIQUADRATE, SQUARE], [NA])
    hard_rectangle_ = Pattern(HARD_RECTANGLE, HARD, [SEMISQUARE, SESQUIQUADRATE, OPPOSITION], [NA])
    grand_trine_ = Pattern(GRAND_TRINE, SOFT, [TRINE], [FIRE, EARTH, AIR, WATER])
    minor_grand_trine_ = Pattern(MINOR_GRAND_TRINE, SOFT, [SEXTILE, TRINE], [NA])
    kite_ = Pattern(KITE, MIXED, [SEXTILE, TRINE, OPPOSITION], [NA])
    yod_ = Pattern(YOD, MIXED, [QUINCUNX, SEXTILE], [NA])
    mystic_rectangle_ = Pattern(MYSTIC_RECTANGLE, MIXED, [SEXTILE, TRINE, OPPOSITION], [NA])
    grand_sextile_ = Pattern(GRAND_SEXTILE, SOFT, [SEXTILE], [NA])
    stellium_ = Pattern(STELLIUM, NA, [CONJUNCTION], [NA])
    
    patterns_ = [t_square_, grand_cross_, finger_of_world_, hard_rectangle_, 
                 grand_trine_, minor_grand_trine_, kite_, yod_, 
                 mystic_rectangle_, grand_sextile_, stellium_]

    def get(self, p):
        t_square = re.compile(rf'{T_SQUARE}', re.IGNORECASE)
        grand_cross = re.compile(rf'{GRAND_CROSS}', re.IGNORECASE)
        finger_of_world = re.compile(rf'{FINGER_OF_WORLD}', re.IGNORECASE)
        hard_rectangle = re.compile(rf'{HARD_RECTANGLE}', re.IGNORECASE)
        grand_trine = re.compile(rf'{GRAND_TRINE}', re.IGNORECASE)
        minor_grand_trine = re.compile(rf'{MINOR_GRAND_TRINE}', re.IGNORECASE)
        kite = re.compile(rf'{KITE}', re.IGNORECASE)
        yod = re.compile(rf'{YOD}', re.IGNORECASE)
        mystic_rectangle = re.compile(rf'{MYSTIC_RECTANGLE}', re.IGNORECASE)
        grand_sextile = re.compile(rf'{GRAND_SEXTILE}', re.IGNORECASE)
        stellium = re.compile(rf'{STELLIUM}', re.IGNORECASE)
        
        if t_square.fullmatch(p):
            pattern = self.t_square_
        elif grand_cross.fullmatch(p):
            pattern = self.grand_cross_
        elif finger_of_world.fullmatch(p):
            pattern =self.finger_of_world_
        elif hard_rectangle.fullmatch(p):
            pattern = self.hard_rectangle_
        elif grand_trine.fullmatch(p):
            pattern = self.grand_trine_
        elif minor_grand_trine.fullmatch(p):
            pattern = self.minor_grand_trine_
        elif kite.fullmatch(p):
            pattern = self.kite_
        elif yod.fullmatch(p):
            pattern = self.yod_
        elif mystic_rectangle.fullmatch(p):
            pattern = self.grand_sextile_
        elif grand_sextile.fullmatch(p):
            pattern = self.grand_sextile_
        elif stellium.fullmatch(p):
            pattern = self.stellium_
        else:
            return None
        return pattern

    def print(self, pattern):
        Pattern.print(pattern)

    def print_keywords(self, pattern_name):
        print("\nKeyword list for pattern " + pattern_name.upper() + ":\n")
        for k in Keywords.patterns_[pattern_name]:
            print("\n\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.patterns_:
            Pattern.print(p)