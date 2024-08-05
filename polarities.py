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
    polarities_ = [positive_, negative_]

    def get(self, p):
        positive = re.compile(rf'{POSITIVE}', re.IGNORECASE)
        negative = re.compile(rf'{NEGATIVE}', re.IGNORECASE)
        
        polarity = None
        if positive.fullmatch(p) or (p == "+") :
            polarity = self.positive_
        elif negative.fullmatch(p) or (p == "-") :
            polarity = self.negative_
        return polarity

    def print(self, polarity):
        Polarity.print(polarity)

    def print_keywords(self, polarity_name):
        print("\nKeyword list for polarity " + polarity_name.upper() + ":\n")
        for k in Keywords.polarities_[polarity_name]:
            print("\t- " + k)

    def print_all(self):
        for p in self.polarities_:
            Polarity.print(p)
