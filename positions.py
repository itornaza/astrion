#
# positions
#

from client import *
from horizons_ephimeris import *
from skyfield_ephimeris import *
from swiss_ephimeris import *

class Positions():
    def __init__(self):
        self.client_ = Client()
        self.all_planets_except_chiron_ = SkyfieldEphimeris(self.client_.bday_)
        self.chiron_ = HorizonsEphimeris(self.client_.bday_)

        # TODO: Get all angles from the pyswisseph
        self.houses_ = SwissEphimeris(self.client_.bday_, self.client_.bplace_)

    def print(self):
        self.client_.print()
        print("\n* PLANETS POSITIONS (LONGITUDES) *\n")
        self.all_planets_except_chiron_.print()
        self.chiron_.print()
        print("\n* HOUSE CUSPS POSITIONS (LONGITUDES) *\n")
        self.houses_.print()

if __name__ == "__main__":
    longs = Positions()
    longs.print()
