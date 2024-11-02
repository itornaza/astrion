#
# ephimeris
#

from datetime import datetime, timezone, timedelta
from skyfield.api import load  # type: ignore
from skyfield.framelib import ecliptic_frame # type: ignore

from constants import *

class Ephimeris():
    def __init__(self, utc_time):
        """Get all planet longitudes for a given UTC time. Note that Chiron
        is not supported in skyfield. The provided longitude is given by
        the library directly in tropical zodiac"""

        # Load ephimeris
        self.ephimeris_ = load('de440.bsp') 
        self.earth_ = self.ephimeris_[EARTH].at(utc_time)

        # Load solar system data
        self.sun_ = self.earth_.observe(self.ephimeris_[SUN]).apparent()
        self.moon_ = self.earth_.observe(self.ephimeris_[MOON]).apparent()
        self.mercury_ = self.earth_.observe(self.ephimeris_[MERCURY]).apparent()
        self.venus_ = self.earth_.observe(self.ephimeris_[VENUS]).apparent()
        self.mars_ = self.earth_.observe(self.ephimeris_['MARS BARYCENTER']).apparent()
        self.jupiter_ = self.earth_.observe(self.ephimeris_['JUPITER BARYCENTER']).apparent()
        self.saturn_ = self.earth_.observe(self.ephimeris_['SATURN BARYCENTER']).apparent()
        self.uranus_ = self.earth_.observe(self.ephimeris_['URANUS BARYCENTER']).apparent()
        self.neptune_ = self.earth_.observe(self.ephimeris_['NEPTUNE BARYCENTER']).apparent()
        self.pluto_ = self.earth_.observe(self.ephimeris_['PLUTO BARYCENTER']).apparent()
        # Chiron unsupported

        planets = [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_,
                   self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                   self.pluto_]
        
        planet_names = [SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, URANUS, NEPTUNE,
                 PLUTO]
        
        print("\n* EPHIMERIS - LONGITUDES *\n")
        for i in range(10):
            _, long, _ = planets[i].frame_latlon(ecliptic_frame)
            self.print_planet_position(planet_names[i], long)

    def print_planet_position(self, planet, long):
        print(planet + ": {:.5f}°".format(long.degrees))

if __name__ == "__main__":
    ts = load.timescale()
    eph = Ephimeris(ts.utc(2024, 11, 2, 21))
    eph.get_aries_zero()