#
# eclipses
#

from datetime import datetime, timezone
from pyswisseph import swe # type: ignore

from chart import ChartPlanet, ChartHouse
from pangle import Ecliptic

# TODO: Check if astronomical data on prenatal and current eclipses are 
# available from an API


class Saros:
    def __init__(self, id: int, saros_type: str):
        self.id_ = id
        self.type_ = saros_type

class Saroses:
    # TODO: Keywords and characteristics
    # Sign, 1st eclipse in the cycle, current phase of the cycle
    # North/South node series
    ...

class EclipseType:
    # TODO: annular, total, ...
    lunar_ = "Lunar"
    solar_ = "Solar"

class Eclipse:
    def __init__(self, eclipse_type: EclipseType, posit: Ecliptic, saros: Saros):
        self.type_ = eclipse_type
        self.posit_ = posit
        self.saros_ = saros

class Eclipses:
    # TODO: Keywords and characteristics
    # Solar, Lunar
    # Saros cycle
    # Sign, House, Planetary ruler (conjuncting planet within 5 orb), 
    # Umbra over the location, Partia/Annular/Total
    # Import/Export axis, 
    ...

class PrenatalEclipse(Eclipse):
    # TODO: Implement and move to chart
    # Prenatal solar eclipse position in sign and house, date, conjunct
    # and opposed planets, number of days prior to birth, planetary ruler
    # planets conjunct horizon

    def __init__(self, bday: datetime):
        # Go get the prenatal eclipse
        posit = ...
        super().__init__(EclipseType.solar_, posit)
        self.days_prior_birth_ = 0

    def get_datetime(birthdate):
        # Convert birthdate to Julian Day
        jd_birth = swe.julday(birthdate.year, birthdate.month, birthdate.day, birthdate.hour + birthdate.minute / 60.0)
        
        # Start from six months before birth to ensure we capture the last eclipse
        start_jd = jd_birth - 182  # 182 days is approximately 6 months

        # Function to check for solar eclipse
        def check_eclipse(jd):
            ret, tret, attr = swe.sol_eclipse_when_loc(jd, swe.FLG_SWIEPH, 0, 0, 0)
            if ret != swe.ERR:
                return tret[0]  # Time of maximum eclipse
            return None

        # Look for the last solar eclipse before birth
        eclipse_jd = None
        current_jd = start_jd
        while current_jd < jd_birth:
            potential_eclipse = check_eclipse(current_jd)
            if potential_eclipse:
                if potential_eclipse < jd_birth:
                    eclipse_jd = potential_eclipse
                else:
                    break
            current_jd += 1  # Increment by one day

        if eclipse_jd:
            year, month, day, hour, min, sec = swe.revjul(eclipse_jd)
            return datetime(year, month, day, int(hour), int(min), int(sec))
        else:
            return None

if __name__ == "__main__":
    # Example usage
    # birthdate = datetime(1980, 5, 15, 12, 0)  # Example birthdate: May 15, 1980, at noon
    # prenatal_eclipse = find_prenatal_solar_eclipse(birthdate)
    # print(f"Prenatal Solar Eclipse Date: {prenatal_eclipse}")
    pass    