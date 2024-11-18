#
# hemispheres
#

import re

from constants import *
from keywords import Keywords

class Hemisphere:

    def __init__(self, name):
        self.name_ = name

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), "\n")

# Only supports keywords and no extra information about the hemispheres
class Hemispheres:
    
    north_ = Hemisphere(NORTH)
    south_ = Hemisphere(SOUTH)
    east_ = Hemisphere(EAST)
    west_ = Hemisphere(WEST)

    hemispheres_ = [north_, south_, east_, west_]

    def get(self, input):
        north = re.compile(rf'^\s*({NORTH}|{"H1"})\s*$', re.IGNORECASE)
        south = re.compile(rf'^\s*({SOUTH}|{"H2"})\s*$', re.IGNORECASE)
        east = re.compile(rf'^\s*({EAST}|{"H3"})\s*$', re.IGNORECASE)
        west = re.compile(rf'^\s*({WEST}|{"H4"})\s*$', re.IGNORECASE)

        if north.fullmatch(input):
            hemisphere = self.north_
        elif south.fullmatch(input):
            hemisphere = self.south_
        elif east.fullmatch(input):
            hemisphere = self.east_
        elif west.fullmatch(input):
            hemisphere = self.west_
        else:
            return None
        return hemisphere
    
    def print(self, hemisphere):
        Hemisphere.print(hemisphere)

    def print_keywords(self, keyword):
        print("\nKeyword list for hemisphere " + keyword.upper() + ":\n")
        for k in Keywords.hemispheres_[keyword]:
            print("\t- " + k)
