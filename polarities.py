#
# polarities
#

import re
from constants import *
from keywords import Keywords
from polarity import Polarity

class Polarities:
    
    positive_ = Polarity(POSITIVE)
    negative_ = Polarity(NEGATIVE)

    def get(self, input):
        positive = re.compile(rf'^\s*{POSITIVE}\s*$', re.IGNORECASE)
        negative = re.compile(rf'^\s*{NEGATIVE}\s*$', re.IGNORECASE)
        
        if positive.fullmatch(input) or (input == "+") :
            polarity = self.positive_
        elif negative.fullmatch(input) or (input == "-") :
            polarity = self.negative_
        else:
            return None
        return polarity

    def print(self, polarity):
        Polarity.print(polarity)

    def print_keywords(self, keyword):
        print("\nKeyword list for polarity " + keyword.upper() + ":\n")
        for k in Keywords.polarities_[keyword]:
            print("\t- " + k)
