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

    def get(self, input):
        t_square = re.compile(rf'^\s*{T_SQUARE}\s*$', re.IGNORECASE)
        grand_cross = re.compile(rf'^\s*{GRAND_CROSS}\s*$', re.IGNORECASE)
        finger_of_world = re.compile(rf'^\s*{FINGER_OF_WORLD}\s*$', re.IGNORECASE)
        hard_rectangle = re.compile(rf'^\s*{HARD_RECTANGLE}\s*$', re.IGNORECASE)
        grand_trine = re.compile(rf'^\s*{GRAND_TRINE}\s*$', re.IGNORECASE)
        minor_grand_trine = re.compile(rf'^\s*{MINOR_GRAND_TRINE}\s*$', re.IGNORECASE)
        kite = re.compile(rf'^\s*{KITE}\s*$', re.IGNORECASE)
        yod = re.compile(rf'^\s*{YOD}\s*$', re.IGNORECASE)
        mystic_rectangle = re.compile(rf'^\s*{MYSTIC_RECTANGLE}\s*$', re.IGNORECASE)
        grand_sextile = re.compile(rf'^\s*{GRAND_SEXTILE}\s*$', re.IGNORECASE)
        stellium = re.compile(rf'^\s*{STELLIUM}\s*$', re.IGNORECASE)
        
        if t_square.fullmatch(input):
            pattern = self.t_square_
        elif grand_cross.fullmatch(input):
            pattern = self.grand_cross_
        elif finger_of_world.fullmatch(input):
            pattern =self.finger_of_world_
        elif hard_rectangle.fullmatch(input):
            pattern = self.hard_rectangle_
        elif grand_trine.fullmatch(input):
            pattern = self.grand_trine_
        elif minor_grand_trine.fullmatch(input):
            pattern = self.minor_grand_trine_
        elif kite.fullmatch(input):
            pattern = self.kite_
        elif yod.fullmatch(input):
            pattern = self.yod_
        elif mystic_rectangle.fullmatch(input):
            pattern = self.grand_sextile_
        elif grand_sextile.fullmatch(input):
            pattern = self.grand_sextile_
        elif stellium.fullmatch(input):
            pattern = self.stellium_
        else:
            return None
        return pattern

    def print(self, pattern):
        Pattern.print(pattern)

    def print_keywords(self, keyword):
        print("\nKeyword list for pattern " + keyword.upper() + ":\n")
        for k in Keywords.patterns_[keyword]:
            print("\n\t- " + k)
