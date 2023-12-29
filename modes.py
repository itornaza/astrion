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
        CARDINAL: ["instigating", "initiating", "initiate and generate energy", "doing", "motion", "pioneering", "start things up", "accept challenges", "goal oriented", "centrifugal radiating energy"],
        FIXED: ["steadfast", "stable", "concentrate energy and sustain it", "consolidate", "put down roots", "preservation and continuation", "stamina", "loyalty", "persistence", "perseverence", "constant", "patience", "self-control", "endurance"],
        MUTABLE: ["adaptable", "flexible", "disperse, distribute and transform energy", "state of flux", "restless", "changeable", "going with the flow", "changing direction", "resolve stalemates", "versatile", "restless"]
    }

    def get(self, m):
      cardinal = re.compile(r'car', re.IGNORECASE)
      fixed = re.compile(r'fix', re.IGNORECASE)
      mutable = re.compile(r'mut', re.IGNORECASE)
      
      mode = None
      if cardinal.search(m):
          mode = self.cardinal_
      elif fixed.search(m):
          mode =  self.fixed_
      elif mutable.search(m):
          mode = self.mutable_
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