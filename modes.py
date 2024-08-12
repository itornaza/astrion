#
# modes
#

import re
from constants import *
from keywords import Keywords
from mode import Mode

class Modes:
    
    cardinal_ = Mode(CARDINAL)
    fixed_ = Mode(FIXED)
    mutable_ = Mode(MUTABLE)

    def get(self, m):
        cardinal = re.compile(rf'^\s*{CARDINAL}\s*$', re.IGNORECASE)
        fixed = re.compile(rf'^\s*{FIXED}\s*$', re.IGNORECASE)
        mutable = re.compile(rf'^\s*{MUTABLE}\s*$', re.IGNORECASE)

        if cardinal.fullmatch(m):
            mode = self.cardinal_
        elif fixed.fullmatch(m):
            mode =  self.fixed_
        elif mutable.fullmatch(m):
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
    