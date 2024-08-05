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
    modes_ = [cardinal_, fixed_, mutable_]    

    def get(self, m):
      cardinal = re.compile(rf'{CARDINAL}', re.IGNORECASE)
      fixed = re.compile(rf'{FIXED}', re.IGNORECASE)
      mutable = re.compile(rf'{MUTABLE}', re.IGNORECASE)
      
      mode = None
      if cardinal.fullmatch(m):
          mode = self.cardinal_
      elif fixed.fullmatch(m):
          mode =  self.fixed_
      elif mutable.fullmatch(m):
          mode = self.mutable_
      return mode

    def print(self, mode):
        Mode.print(mode)

    def print_keywords(self, mode_name):
        print("\nKeyword list for mode " + mode_name.upper() + ":\n")
        for k in Keywords.modes_[mode_name]:
            print("\t- " + k)

    # TODO: Integrate     
    def print_all(self):
        for m in self.modes_:
            Mode.print(m)
    