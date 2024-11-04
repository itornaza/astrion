#
# ephimeris
#

from datetime import datetime, timezone, timedelta
from skyfield.api import load  # type: ignore
from skyfield.framelib import ecliptic_frame # type: ignore

from constants import *
from pangle import Ecliptic
from client import *

class Ephimeris():
    # https://rhodesmill.org/skyfield/examples.html

    def __init__(self, bday: datetime):
        """Get all planet longitudes for a given UTC time. Note that Chiron
        is not supported in skyfield. The provided longitude is given by
        the library directly in tropical zodiac"""

        # Members to hold the longitude of each planet in ecliptic format
        self.sun_: Ecliptic
        self.moon_: Ecliptic
        self.mercury_: Ecliptic
        self.venus_: Ecliptic
        self.mars_: Ecliptic
        self.jupiter_: Ecliptic
        self.saturn_: Ecliptic
        self.uranus_: Ecliptic
        self.neptune_: Ecliptic
        self.pluto_: Ecliptic

        # Load ephimeris
        self.ephimeris_ = load('de440.bsp') 
        ts = load.timescale()
        
        # Time set up
        # TODO: Caution!!! It will create UTC out of the date
        t = ts.utc(bday.year, bday.month, bday.day, bday.hour, bday.minute)
        self.earth_ = self.ephimeris_[EARTH].at(t)

        # Get the longitude of all planets except unsupported Chiron
        _, sun_long, _ = self.earth_.observe(self.ephimeris_[SUN]).apparent().frame_latlon(ecliptic_frame)
        _, moon_long, _ = self.earth_.observe(self.ephimeris_[MOON]).apparent().frame_latlon(ecliptic_frame)
        _, mercury_long, _ = self.earth_.observe(self.ephimeris_[MERCURY]).apparent().frame_latlon(ecliptic_frame)
        _, venus_long, _ = self.earth_.observe(self.ephimeris_[VENUS]).apparent().frame_latlon(ecliptic_frame)
        _, mars_long, _ = self.earth_.observe(self.ephimeris_['MARS BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, jupiter_long, _ = self.earth_.observe(self.ephimeris_['JUPITER BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, saturn_long, _ = self.earth_.observe(self.ephimeris_['SATURN BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, uranus_long, _ = self.earth_.observe(self.ephimeris_['URANUS BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, neptune_long, _ = self.earth_.observe(self.ephimeris_['NEPTUNE BARYCENTER']).apparent().frame_latlon(ecliptic_frame)
        _, pluto_long, _ = self.earth_.observe(self.ephimeris_['PLUTO BARYCENTER']).apparent().frame_latlon(ecliptic_frame)

        # Convert longitudes from skyfield Angles to Ecliptic format 
        self.sun_ = Ecliptic.from_angle(Ecliptic, sun_long)
        self.moon_ = Ecliptic.from_angle(Ecliptic, moon_long)
        self.mercury_ = Ecliptic.from_angle(Ecliptic, mercury_long)
        self.venus_ = Ecliptic.from_angle(Ecliptic, venus_long)
        self.mars_ = Ecliptic.from_angle(Ecliptic, mars_long)
        self.jupiter_ = Ecliptic.from_angle(Ecliptic, jupiter_long)
        self.saturn_ = Ecliptic.from_angle(Ecliptic, saturn_long)
        self.uranus_ = Ecliptic.from_angle(Ecliptic, uranus_long)
        self.neptune_ = Ecliptic.from_angle(Ecliptic, neptune_long)
        self.pluto_ = Ecliptic.from_angle(Ecliptic, pluto_long)

    def print(self):
        longs = [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_,
                   self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                   self.pluto_]
        
        planets = [SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, URANUS, NEPTUNE,
                        PLUTO]
        for i in range(10):
            self.print_planet(planets[i], longs[i])

    def print_planet(self, planet: str, e: Ecliptic):
        print(planet + ":", end=" ")
        e.print()
