#
# hemispheres
#

import re
from constants import *
from keywords import Keywords
from hemisphere import Hemisphere

# Only supports keywords and no extra information about the nodes
class LunarNodes:
    
    north_ = Hemisphere(NORTH)
    south_ = Hemisphere(SOUTH)
    east_ = Hemisphere(EAST)
    west_ = Hemisphere(WEST)

    def get(self, input):
        north = re.compile(rf'^\s*{NORTH}\s*$', re.IGNORECASE)
        south = re.compile(rf'^\s*{SOUTH}\s*$', re.IGNORECASE)
        east = re.compile(rf'^\s*{EAST}\s*$', re.IGNORECASE)
        west = re.compile(rf'^\s*{west}\s*$', re.IGNORECASE)

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
            print("\n\t- " + k)
            