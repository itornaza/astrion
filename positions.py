#
# positions
#

from ephimeris import *
from horizons import *
from client import *

class Positions():
    def __init__(self):
        self.client_ = Client()
        self.all_planets_except_chiron_ = Ephimeris(self.client_.bday_)
        self.chiron_ = Horizons(self.client_.bday_)

    def print(self):
        self.client_.print()
        print("\n* PLANETS POSITIONS (LONGITUDES) *\n")
        self.all_planets_except_chiron_.print()
        self.chiron_.print()

if __name__ == "__main__":
    longs = Positions()
    longs.print()
