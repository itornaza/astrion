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
    def __init__(self, message="There are no floating point numbers in the response"):
        self.message = message
        super().__init__(self.message)

class planet_id():
    chiron: str = "2060"

def extract_longitude(text):
    placeholder = r'\$\$SOE(.*?)\$\$EOE'
    response = re.findall(placeholder, text, re.DOTALL)[0]
    is_float = r'[-+]?\d*\.\d+'
    coordinates = re.findall(is_float, response)
    if not coordinates:
        raise HorizonsError(response)
    return float(coordinates[0])

def get_planet_long(planet_id: int, planet_name: str):
    # Define today's date and set time to 12:00 UTC
    now_utc = datetime.now(timezone.utc)
    today_date = now_utc.date()
    start_time = datetime(today_date.year, today_date.month, today_date.day, 21, 0, 0, tzinfo=timezone.utc)
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
    horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    # Prepare request
    request_url = f"{horizons_url}?{urllib.parse.urlencode(params)}"
    print(planet_name + ":", end=" ")

    # Send request
    try:
        with urllib.request.urlopen(request_url) as response:
            position = response.read()
            print(extract_longitude(position.decode()))

    except HorizonsError as e:
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
    get_planet_long(planet_id.chiron, CHIRON)
