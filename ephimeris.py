#
# ephimeris
#

from datetime import datetime, timezone, timedelta
from skyfield.api import load
from skyfield.framelib import ecliptic_frame

class Ephimeris():
    def __init__(self):
        data = load('de421.bsp')  # Load the DE421 ephemeri
        sun = data['sun']
        moon = data['moon']
        mercury = data['mercury']
        venus = data['venus']
        mars = data['mars']
        # jupiter = data['jupiter']
        # saturn = data['saturn']
        # uranus = data['uranus']
        # neptune = data['neptune']
        # pluto = data['pluto']
        # chiron = data['chiron']

def get_aries_zero():
    ephimeris = load('de421.bsp')  # Load the DE421 ephemeris
    ts = load.timescale()
    equinox_date = datetime(2024, 3, 20, 12, 0, 0, tzinfo=timezone.utc)
    t = ts.utc(equinox_date.year, equinox_date.month, equinox_date.day)
    sun = ephimeris['sun']
    earth = ephimeris['earth']
    e = earth.at(t)
    s = e.observe(sun).apparent()
    lat, long, _ = s.frame_latlon(ecliptic_frame)
    print('Sun  {:.5f}° {:.5f}°'.format(lat.degrees, long.degrees))

    j2000_julian_date = 2451545.0  # Julian date for J2000.0 epoch
    current_julian_date = t.utc_jpl()[0]  # This should give you the Julian date
    # days_since_j2000 = current_julian_date - j2000_julian_date
    # tropical_long = (long - (360 * days_since_j2000 / 36525)) % 360

    print(t.utc_jpl()[0])
    print(t.utc_jpl())
    # print('Sun tropical  {:.5f}°'.format(tropical_long))

if __name__ == "__main__":

    eph = Ephimeris()

    # Load ephemeris data
    ts = load.timescale()
    t = ts.utc(2024, 11, 1, 12)

    # Load solar system data
    ephimeris = load('de421.bsp')
    sun = ephimeris['sun']
    earth = ephimeris['earth']
    mars = ephimeris['mars']

    e = earth.at(t)
    s = e.observe(sun).apparent()
    m = e.observe(mars).apparent()
    lat, lon, _ = s.frame_latlon(ecliptic_frame)
    print('Sun  {:.5f}° {:.5f}°'.format(lat.degrees, lon.degrees))

    lat, lon, _ = m.frame_latlon(ecliptic_frame)
    print('Mars  {:.5f}° {:.5f}°'.format(lat.degrees, lon.degrees))