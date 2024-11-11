#
# swiss_ephimeris
#

import swisseph as swe # type: ignore

from client import Birthplace
from datetime import datetime
from pangle import Ecliptic

class SwissEphimeris():
    def __init__(self, bday: datetime, bplace: Birthplace):
        self.cusps_: Ecliptic = []

        # Convert to Julian Day
        jd = swe.julday(bday.year, bday.month, bday.day, (bday.hour + bday.minute / 60))

        # Get house cusps and Ascendant/MC for Placidus system (hsys='P')
        # The cusps and are degrees on the ecliptic in float
        # Use ascmc in the second return value to get the asc, mc, vertex, etc if needed
        cusps, _ = swe.houses(jd, bplace.lat_, bplace.long_, b'P')
        for cusp in cusps:
            self.cusps_.append(Ecliptic.from_float(Ecliptic, cusp))

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
            
