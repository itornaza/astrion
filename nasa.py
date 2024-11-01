#
# nasa
#

from datetime import datetime, timezone, timedelta
import re
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

from constants import *

class NasaError(Exception):
    """Exception raised when the NASA API response does not contain floats"""
    def __init__(self, message="There are no floating point numbers in the response"):
        self.message = message
        super().__init__(self.message)

class planet_id():
    ssb: str = "0"
    sun: str = "10"
    mercury: str = "199"
    venus: str = "299"
    earth: str = "399"
    moon: str = "301"
    mars: str = "499"
    jupiter: str = "599"
    saturn: str = "699"
    uranus: str = "799"
    neptune: str = "899"
    pluto: str = "999"
    chiron: str = "2060"

def extract_longitude(text):
    pattern = r'\$\$SOE(.*?)\$\$EOE' # Ephimeris data
    nasa_response = re.findall(pattern, text, re.DOTALL)[0]
    pattern = r'[-+]?\d*\.\d+' # Floats
    coordinates = re.findall(pattern, nasa_response)
    if not coordinates:
        raise NasaError(nasa_response)
    return float(coordinates[0]) # Longitude

def get_planet_long(planet_id: int, planet_name: str):
    # Define today's date and set time to 12:00 UTC
    now_utc = datetime.now(timezone.utc)
    today_date = now_utc.date()
    start_time = datetime(today_date.year, today_date.month, today_date.day, 12, 0, 0, tzinfo=timezone.utc)
    stop_time = start_time + timedelta(minutes=1)

    # Format dates for Horizons (ISO 8601 format with 'T' between date and time)
    f_start_time = start_time.strftime('%Y-%m-%dT%H:%M')
    f_stop_time = stop_time.strftime('%Y-%m-%dT%H:%M')

    # Parameters for the given planet in ecliptic coordinates) with the center 
    # set to Earth
    params = {
        "format": "json",
        "COMMAND": planet_id,
        "EPHEM_TYPE": "OBSERVER",
        "REF_PLANE": "ECLIPTIC",
        "CENTER": "500@399",
        "START_TIME": f_start_time,
        "STOP_TIME": f_stop_time,
        "QUANTITIES": "18",  
        "ANG_FORMAT": "DEG"  
    }

    # NASA JPL Horizons API URL
    nasa_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    # Prepare request
    url = f"{nasa_url}?{urllib.parse.urlencode(params)}"
    print(planet_name + ":", end=" ")

    # Send request
    try:
        with urllib.request.urlopen(url) as response:
            position = response.read()
            print(extract_longitude(position.decode()))

    except NasaError as e:
        print(f"NASA error occured: {e.message}")
        # TODO - for debugging: print(position.decode())
    except HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL error occurred: {e.reason}")
    except TypeError as e:
        print(f"Type error occured: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_planet_long(planet_id.moon, MOON)
    get_planet_long(planet_id.mercury, MERCURY)
    get_planet_long(planet_id.venus, VENUS)
    get_planet_long(planet_id.mars, MARS)
    get_planet_long(planet_id.saturn, SATURN)
    get_planet_long(planet_id.jupiter, JUPITER)
    get_planet_long(planet_id.uranus, URANUS)
    get_planet_long(planet_id.neptune, NEPTUNE)
    get_planet_long(planet_id.pluto, PLUTO)
    get_planet_long(planet_id.chiron, CHIRON)
    # get_planet_long(planet_id.sun, SUN)
