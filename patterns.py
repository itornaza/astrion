#
# planets
#

import re
from constants import *
from keywords import Keywords
from aspect import Aspect
from pattern import Pattern

class Patterns:

    t_square_ = Pattern(T_SQUARE, HARD, [SQUARE, OPPOSITION])
    grand_cross_ = Pattern(GRAND_CROSS, HARD, [SQUARE, OPPOSITION])
    finger_of_world_ = Pattern(FINGER_OF_WORLD, HARD, [SESQUIQUADRATE, SQUARE])
    hard_rectangle_ = Pattern(HARD_RECTANGLE, HARD, SEMISQUARE, SESQUIQUADRATE, OPPOSITION)
    grand_trine_ = Pattern(GRAND_TRINE, SOFT, TRINE)
    minor_grand_trine_ = Pattern(MINOR_GRAND_TRINE, SOFT, [SEXTILE, TRINE])
    kite_ = Pattern(KITE, MIXED, [SEXTILE, TRINE, OPPOSITION])
    yod_ = Pattern(YOD, MIXED, [QUINCUNX, SEXTILE])
    mystic_rectangle_ = Pattern(MYSTIC_RECTANGLE, MIXED, SEXTILE, TRINE, OPPOSITION)
    grand_sextile_ = Pattern(GRAND_SEXTILE, SOFT, SEXTILE)
    stellium_ = Pattern(STELLIUM, SOFT, CONJUNCTION)
    
    patterns_ = [t_square_, grand_cross_, finger_of_world_, hard_rectangle_, 
                 grand_trine_, minor_grand_trine_, kite_, yod_, 
                 mystic_rectangle_, grand_sextile_, stellium_]

    def get(self, p):
        t_square = re.compile(r't-square', re.IGNORECASE)
        grand_cross = re.compile(r'grand cross', re.IGNORECASE)
        finger_of_world = re.compile(r'finger of the world', re.IGNORECASE)
        hard_rectangle = re.compile(r'hard rectangle', re.IGNORECASE)
        grand_trine = re.compile(r'grand trine', re.IGNORECASE)
        minor_grand_trine = re.compile(r'minor grand trine', re.IGNORECASE)
        kite = re.compile(r'kite', re.IGNORECASE)
        yod = re.compile(r'yod', re.IGNORECASE)
        mystic_rectangle = re.compile(r'mystic rectangle', re.IGNORECASE)
        grand_sextile = re.compile(r'grand sextile', re.IGNORECASE)
        stellium = re.compile(r'stellium', re.IGNORECASE)
        
        if t_square.search(p):
            pattern = self.t_square_
        elif grand_cross.search(p):
            pattern = self.grand_cross_
        elif finger_of_world.search(p):
            pattern =self.finger_of_world_
        elif hard_rectangle.search(p):
            pattern = self.hard_rectangle_
        elif grand_trine.search(p):
            pattern = self.grand_trine_
        elif minor_grand_trine.search(p):
            pattern = self.minor_grand_trine_
        elif kite.search(p):
            pattern = self.kite_
        elif yod.search(p):
            pattern = self.yod_
        elif mystic_rectangle.search(p):
            pattern = self.grand_sextile_
        elif grand_sextile.search(p):
            pattern = self.grand_sextile_
        elif stellium.search(p):
            pattern = self.stellium_
        else:
            return None
        return pattern

    def print(self, pattern):
        Pattern.print(pattern)
        # TODO: Print associated aspects to get all the associated info
        for aspect in pattern:
            Aspect.print(aspect)

    def print_keywords(self, pattern_name):
        print("\nKeyword list for pattern " + pattern_name.upper() + ":\n")
        for k in Keywords.patterns_[pattern_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.patterns_:
            Pattern.print(p)