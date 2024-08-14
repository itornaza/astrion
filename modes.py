#
# modes
#

import re
from constants import *
from keywords import Keywords

class Mode:

    def __init__(self, mode):
        self.name_ = mode
        
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper())

class Modes:
    
    cardinal_ = Mode(CARDINAL)
    fixed_ = Mode(FIXED)
    mutable_ = Mode(MUTABLE)

    modes_ = [cardinal_, fixed_, mutable_]

    def get(self, input):
        cardinal = re.compile(rf'^\s*{CARDINAL}\s*$', re.IGNORECASE)
        fixed = re.compile(rf'^\s*{FIXED}\s*$', re.IGNORECASE)
        mutable = re.compile(rf'^\s*{MUTABLE}\s*$', re.IGNORECASE)

        if cardinal.fullmatch(input):
            mode = self.cardinal_
        elif fixed.fullmatch(input):
            mode =  self.fixed_
        elif mutable.fullmatch(input):
            mode = self.mutable_
        else:
            return None
        return mode

    def print(self, mode):
        Mode.print(mode)

    def print_keywords(self, keyword):
        print("\nKeyword list for mode " + keyword.upper() + ":\n")
        for k in Keywords.modes_[keyword]:
            print("\t- " + k)
    