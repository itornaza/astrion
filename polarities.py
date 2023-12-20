#
# polarities
#

import re
from constants import *
from polarity import Polarity

class Polarities:
    
    positive_ = Polarity(POSITIVE)
    negative_ = Polarity(NEGATIVE)
    
    keywords_ = {
        POSITIVE: [NA],
        NEGATIVE: [NA],
    }

    polarities_ = [positive_, negative_]    

    def get(self, p):
        positive = re.compile(r'pos', re.IGNORECASE)
        negative = re.compile(r'neg', re.IGNORECASE)

        if (positive.search(p) != None) or (p == "+") :
            polarity = self.positive_
        elif (negative.search(p) != None) or (p == "-") :
            polarity = self.negative_
        else:
            return -1
        return polarity

    def print(self, polarity):
        Polarity.print(polarity)

    def print_keywords(self, polarity_name):
        print("\nKeyword list for polarity " + polarity_name.upper() + ":\n")
        for k in Polarities.keywords_[polarity_name]:
            print("\t- " + k)

    def print_all(self):
        for p in self.polarities_:
            Polarity.print(p)
