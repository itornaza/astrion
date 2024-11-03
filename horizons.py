#
# horizons
#

from datetime import datetime, timezone, timedelta
import re
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

from constants import *

class HorizonsError(Exception):
    """Exception raised when the NASA API response does not contain floats"""
    def __init__(self, message="No floating point numbers in response"):
        self.message = message
        super().__init__(self.message)

class Horizons():

    def __init__(self, year, month, day, hour, min):
        """Get the longitude of Chiron on the ecliptic. We get the positions
        of all other planets from the ephimeris module"""
        
        self.chiron_: float = 0.0

        t1_prep = datetime(year, month, day, hour, min, 0, tzinfo=timezone.utc)
        t2_prep = t1_prep + timedelta(minutes=1)
        t1 = t1_prep.strftime('%Y-%m-%dT%H:%M')
        t2 = t2_prep.strftime('%Y-%m-%dT%H:%M')

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
        try:
            with urllib.request.urlopen(request_url) as response:
                position = response.read()
                self.chiron_ = self.extract_long(position.decode())
                self.print()
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

    def print(self):
        print(CHIRON + ":", self.chiron_)

    def extract_long(self, text):
        placeholder = r'\$\$SOE(.*?)\$\$EOE'
        response = re.findall(placeholder, text, re.DOTALL)[0]
        is_float = r'[-+]?\d*\.\d+'
        coordinates = re.findall(is_float, response)
        if not coordinates:
            raise HorizonsError(response)
        return float(coordinates[0])

if __name__ == "__main__":
    chiron = Horizons(2024, 11, 2, 21, 0)
