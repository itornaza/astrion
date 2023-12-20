#
# modes
#

import re
from constants import *
from mode import Mode

class Modes:
    
    cardinal_ = Mode(CARDINAL)
    fixed_ = Mode(FIXED)
    mutable_ = Mode(MUTABLE)
    modes_ = [cardinal_, fixed_, mutable_]    
    keywords_ = {
        CARDINAL: [NA],
        FIXED: [NA],
        MUTABLE: [NA]
    }

    def get(self, m):
      cardinal = re.compile(r'car', re.IGNORECASE)
      fixed = re.compile(r'fix', re.IGNORECASE)
      mutable = re.compile(r'mut', re.IGNORECASE)

      if cardinal.search(m) != None:
          mode = self.cardinal_
      elif fixed.search(m) != None:
          mode =  self.fixed_
      elif mutable.search(m) != None:
          mode = self.mutable_
      else:
          return -1
      return mode

    def print(self, mode):
        Mode.print(mode)

    def print_keywords(self, mode_name):
        print("\nKeyword list for mode " + mode_name.upper() + ":\n")
        for k in Modes.keywords_[mode_name]:
            print("\t- " + k)

    # TODO: Integrate     
    def print_all(self):
        for m in self.modes_:
            Mode.print(m)