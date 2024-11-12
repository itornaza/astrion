#
# ephimeris_handler
#

from client import *
from horizons_ephimeris import *
from skyfield_ephimeris import *
from swiss_ephimeris import *

class EphimerisHandler():
    def __init__(self):
        self.client_ = Client()
        self.all_planets_except_chiron_ = SkyfieldEphimeris(self.client_.bday_)
        self.chiron_ = HorizonsEphimeris(self.client_.bday_)
        self.houses_and_nodes_ = SwissEphimeris(self.client_.bday_, self.client_.bplace_)

    # TODO: This shall be left only for debugging. Actual printing to be done 
    # from within the chart
    def print(self):
        self.client_.print()
        print("\n* PLANETS POSITIONS (LONGITUDES) *\n")
        self.all_planets_except_chiron_.print()
        self.chiron_.print()
        print("\n* HOUSE CUSPS POSITIONS (LONGITUDES) *\n")
        self.houses_and_nodes_.print()

if __name__ == "__main__":
    longs = EphimerisHandler()
    longs.print()
