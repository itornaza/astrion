#
# client
#

from datetime import datetime, timezone

class Identity():
    def __init__(self):        
        self.name_: str
        self.lastname_: str

    def set_identity(self):
        self.name_ = input("Name: ")
        self.lastname_ = input("Last name: ")
        return self

class Birthplace():
    def __init__(self, lat, long):
        assert abs(lat) < 90, "Latitude must be [0-90)"
        assert abs(long) < 180, "Longitude must be [0-180)"
        self.long_: float = long
        self.lat_: float = lat

    def set_birthplace(self):
        prompt = "Please enter 'Latitude/Longitude' separated by space: "
        while True:
            try:
                # Check if floats
                user_input = input(prompt)
                lat, long = map(float, user_input.split(" "))
                if abs(lat) > 89.9999999999:
                    print("Latitude must be [0-90) in decimal, (-) for South")
                elif abs(long) > 179.9999999999:
                    print("Longitude must be [0-180) in decimal, (-) for West")
                else:
                    self.lat_ = lat
                    self.long_ = long
                    return self
            except ValueError:
                try:
                    # If floats fail, check if integers
                    self.long_ = int(long)
                    self.lat_ = int(lat)
                    return self
                except ValueError:
                    # Error if not an integer or float
                    print("Invalid input! " + prompt)

class Client():

    # TODO: Investigate Client and Chart relationships.

    def __init__(self):
        self.id_: Identity = Identity.set_identity(Identity)
        self.bday_: datetime = self._get_date_utc()
        self.bplace_: Birthplace = Birthplace.set_birthplace(Birthplace)

    def _get_date_utc(self):
        prompt = "Please enter 'YYYY-MM-DD-HH-MM' in UTC separated by a dash (-): "
        while True:
            try:
                user_input = input(prompt)
                year, month, day, hour, min = map(int, user_input.split("-"))
                if month < 1 or month > 12:
                    print("Month must be [1-12]")
                elif hour < 0 or hour > 23:
                    print("Minutes must be [0-23]")
                elif min < 0 or min > 59:
                    print("Minutes must be [0-59]")
                else:
                    return datetime(year, month, day, hour, min, 0, 
                                    tzinfo=timezone.utc)
            except ValueError:
                print("Invalid input! " + prompt)

    def print(self):
        print("\n* CLIENT *\n")
        print(self.id_.name_ + self.id_.lastname_)
        print(self.bday_.strftime('%Y-%m-%dT%H:%M'))
        print(f"Long: {self.bplace_.long_}° / Lat: {self.bplace_.lat_}°")

if __name__ == "__main__":
    client = Client()
    client.print()