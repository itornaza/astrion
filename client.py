#
# client
#

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

class Client():
    def __init__(self):
        self.name_ = input("Name: ")
        self.lastname_ = input("Last name: ")

        # Get the date and time 
        prompt = "Please enter YYYY-MM-DD-HH-MM in UTC separated by a dash (-): "
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
                    self.bday_ = datetime(year, month, day, hour, min, 0, 
                                          tzinfo=timezone.utc)
                    break
            except ValueError:
                print("Invalid input! " + prompt)

    def print(self):
        print("\n* CLIENT *\n")
        print(self.name_ + self.lastname_)
        print(self.bday_.tzinfo.tzname)
        print(self.bday_.strftime('%Y-%m-%dT%H:%M'))