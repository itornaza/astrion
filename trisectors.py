#
# trisectors
#

import re
from constants import *
from keywords import Keywords

class Trisector:

    def __init__(self, name):
        self.name_ = name

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), "\n")

# Only supports keywords and no extra information about the trisectors
class Trisectors:
    
    personal_ = Trisector(PERSONAL)
    social_ = Trisector(SOCIAL)
    universal_ = Trisector(UNIVERSAL)

    trisectors_ = [personal_, social_, universal_]

    def get(self, input):
        personal = re.compile(rf'^\s*({PERSONAL}|{"T1"})\s*$', re.IGNORECASE)
        social = re.compile(rf'^\s*({SOCIAL}|{"T2"})\s*$', re.IGNORECASE)
        universal = re.compile(rf'^\s*({UNIVERSAL}|{"T3"})\s*$', re.IGNORECASE)

        if personal.fullmatch(input):
            trisector = self.personal_
        elif social.fullmatch(input):
            trisector = self.social_
        elif universal.fullmatch(input):
            trisector = self.universal_
        else:
            return None
        return trisector
    
    def print(self, trisector):
        Trisector.print(trisector)

    def print_keywords(self, keyword):
        print("\nKeyword list for trisector " + keyword.upper() + ":\n")
        for k in Keywords.trisectors_[keyword]:
            print("\t- " + k)
