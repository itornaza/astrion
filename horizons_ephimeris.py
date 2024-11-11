#
# horizons_ephimeris
#

from datetime import datetime, timedelta
import re
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

from client import *
from constants import *
from pangle import Ecliptic

class HorizonsError(Exception):
    """Exception raised when the NASA API response does not contain floats"""
    def __init__(self, message="No floating point numbers in response"):
        self.message = message
        super().__init__(self.message)

class HorizonsEphimeris():
    # https://ssd-api.jpl.nasa.gov/doc/horizons.html
    # https://ssd.jpl.nasa.gov/horizons/manual.html

    def __init__(self, bday: datetime):
        """Get the longitude of Chiron on the ecliptic. We get the positions
        of all other planets from the ephimeris module"""
        
        # Members to hold the longitude of each planet in ecliptic format
        self.chiron_: Ecliptic

        # Caution: In order for the calculation to be executed this time difference is 
        # needed. While for Chiron makes no-difference, be aware if it is for faster
        # planets to be integrated here as well
        
        # Set up time interval for planet position
        t1_prep = bday
        t2_prep = t1_prep + timedelta(minutes=1)
        t1 = t1_prep.strftime('%Y-%m-%dT%H:%M')
        t2 = t2_prep.strftime('%Y-%m-%dT%H:%M')

        # Prepare the query from the parameters
        chiron_id: str = "2060"
        params = {
            "format": "json",
            "COMMAND": chiron_id,
            "EPHEM_TYPE": "OBSERVER",
            "REF_PLANE": "ECLIPTIC",
            "CENTER": "500@399",
            "START_TIME": t1,
            "STOP_TIME": t2,
            "QUANTITIES": "18",  # Ecliptic coordinates
            "ANG_FORMAT": "DEG"  
        }
        horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        request_url = f"{horizons_url}?{urllib.parse.urlencode(params)}"
        
        # Send the request to Horizons with error handling
        try:
            with urllib.request.urlopen(request_url) as response:
                position = response.read()
                chiron_long: float = self._extract_long(position.decode())
        except HorizonsError as e:
            print(f"NASA error occured: {e.message}")
        except HTTPError as e:
            print(f"HTTP error occurred: {e.code} - {e.reason}")
        except URLError as e:
            print(f"URL error occurred: {e.reason}")
        except TypeError as e:
            print(f"Type error occured: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Convert longitude from skyfield Angles to Ecliptic format 
        self.chiron_ = Ecliptic.from_float(Ecliptic, chiron_long)

    def print(self):
        print(CHIRON + ":", end=" ")
        self.chiron_.print()

    def _extract_long(self, text):
        placeholder = r'\$\$SOE(.*?)\$\$EOE'
        response = re.findall(placeholder, text, re.DOTALL)[0]
        is_float = r'[-+]?\d*\.\d+'
        coordinates = re.findall(is_float, response)
        if not coordinates:
            raise HorizonsError(response)
        return float(coordinates[0])

if __name__ == "__main__":
    pass
