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
    def __init__(self):
        self.lat_: float
        self.long_: float
        self.h_: float

    def set_birthplace(self):
        prompt = "Please enter 'Longitude/Latitude/Elevation' separated by space: "
        while True:
            try:
                # Check if floats
                user_input = input(prompt)
                long, lat, h = map(float, user_input.split(" "))
                if long < 0 or long > 359.9999999999:
                    print("Longitude must be [0-360)")
                elif lat < 0 or lat > 89.999999999:
                    print("Latitude must be [0-90)")
                elif h < 0 or h > 8850:
                    print("Latitude must be [0-8850) meters")
                else:
                    self.long_ = long
                    self.lat_ = lat
                    self.h_ = h
                    return self
            except ValueError:
                try:
                    # If floats fail, check if integers
                    self.long_ = int(long)
                    self.lat_ = int(lat)
                    self.h_ = int(h)
                    return self
                except ValueError:
                    # Error if not an integer or float
                    print("Invalid input! " + prompt)

class Client():
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
        print(f"Long: {self.bplace_.long_}° / Lat: {self.bplace_.lat_}°, / h: {self.bplace_.h_}")

if __name__ == "__main__":
    client = Client()
    client.print()