#
# swiss_ephimeris
#

import swisseph as swe # type: ignore

from client import Birthplace
from datetime import datetime
from pangle import Ecliptic

class SwissEphimeris():
    """Calculates house cusps for Placidus only and the Lunar Nodes"""

    def __init__(self, bday: datetime, bplace: Birthplace):
        self.cusps_: Ecliptic = []
        self.nodes_: Ecliptic = []

        # Convert to Julian Day
        jd = swe.julday(bday.year, bday.month, bday.day, 
                        (bday.hour + bday.minute / 60))

        # Get house cusps and Ascendant/MC for Placidus system (hsys='P')
        # The cusps and are degrees on the ecliptic in float numbers
        cusps, _ = swe.houses(jd, bplace.lat_, bplace.long_, b'P')
        for cusp in cusps:
            self.cusps_.append(Ecliptic.from_float(Ecliptic, cusp))

        # Get the True Node and calculate the South Node from it
        north_node_tuple, _ = swe.calc_ut(jd, 11)
        north_node: float = north_node_tuple[0]

        # Set the Nodes
        self.nodes_.append(Ecliptic.from_float(Ecliptic, north_node))
        self.nodes_.append(self.nodes_[0] - 180)

    # TODO: This print is only for debugging
    def print(self):
        i: int = 1
        for cusp in self.cusps_:
            if i == 1:
                print("* Asc:", end=" ")
            elif i == 4:
                print("* IC:", end=" ")
            elif i == 7:
                print("* Dsc:", end=" ")
            elif i == 10:
                print("* MC:", end=" ")
            else:
                print(f"Cusp {i}:", end=" ")
            cusp.print()
            i += 1

        print("North Node: ", end=" ")
        self.nodes_[0].print()
        print("South Node: ",  end=" ")
        self.nodes_[1].print()

if __name__ == "__main__":
    bday = datetime(1975, 3, 28, 10, 39)
    bplace = Birthplace(38.02, 24.8)
    posits = SwissEphimeris(bday, bplace)
    posits.print()