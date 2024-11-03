#
# ephimeris
#

from datetime import datetime, timezone, timedelta
from skyfield.api import load  # type: ignore
from skyfield.framelib import ecliptic_frame # type: ignore

from constants import *

class Ephimeris():

    # TODO: Get time up to the minute

    def __init__(self, year: int, month: int, day: int, hour: int):
        """Get all planet longitudes for a given UTC time. Note that Chiron
        is not supported in skyfield. The provided longitude is given by
        the library directly in tropical zodiac"""

        # Load ephimeris
        self.ephimeris_ = load('de440.bsp') 
        ts = load.timescale()
        utc_time = ts.utc(year, month, day, hour)
        self.earth_ = self.ephimeris_[EARTH].at(utc_time)

        # Get the longitude of all planets except unsupported Chiron
        _, self.sun_, _ = self.earth_.observe(self.ephimeris_[SUN]).apparent().frame_latlon(ecliptic_frame)
        _, self.moon_, _ = self.earth_.observe(self.ephimeris_[MOON]).apparent().frame_latlon(ecliptic_frame)
        _, self.mercury_, _ = self.earth_.observe(self.ephimeris_[MERCURY]).apparent().frame_latlon(ecliptic_frame)
        _, self.venus_, _ = self.earth_.observe(self.ephimeris_[VENUS]).apparent().frame_latlon(ecliptic_frame)
        _, self.mars_, _ = self.earth_.observe(self.ephimeris_['MARS BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, self.jupiter_, _ = self.earth_.observe(self.ephimeris_['JUPITER BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, self.saturn_, _ = self.earth_.observe(self.ephimeris_['SATURN BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, self.uranus_, _ = self.earth_.observe(self.ephimeris_['URANUS BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, self.neptune_, _ = self.earth_.observe(self.ephimeris_['NEPTUNE BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, self.pluto_, _ = self.earth_.observe(self.ephimeris_['PLUTO BARYCENTER']).apparent().frame_latlon(ecliptic_frame)

        self.planets_long = [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_,
                   self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                   self.pluto_]
        
        self.planet_names = [SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, URANUS, NEPTUNE,
                        PLUTO]

    def print_all(self):
        print("\n* EPHIMERIS - LONGITUDES *\n")
        for i in range(10):
            self.print(self.planet_names[i], self.planets_long[i])

    def print(self, planet, long):
        print(planet + ": {:.5f}°".format(long.degrees))

if __name__ == "__main__":
    eph = Ephimeris(2024, 11, 2, 21)
    eph.print_all()