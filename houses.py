#
# house
#

import re
from constants import *
from keywords import Keywords
from house import House

class Houses:

    first_ = House(FIRST, 1, ARIES, "I am")
    second_ = House(SECOND, 2, TAURUS, "I possess")
    third_ = House(THIRD, 3, GEMINI, "I think")
    fourth_ = House(FOURTH, 4, CANCER, "I belong")
    fifth_ = House(FIFTH, 5, LEO, "I generate")
    sixth_ = House(SIXTH, 6, VIRGO, "I attend to")
    seventh_ = House(SEVENTH, 7, LIBRA, "I relate")
    eight_ = House(EIGHT, 8, SCORPIO, "I deepen")
    ninth_ = House(NINTH, 9, SAGITTARIUS, "I beleive")
    tenth_ = House(TENTH, 10, CAPRICORN, "I aspire")
    eleventh_ = House(ELEVENTH, 11, AQUARIUS, "I participate")
    twelvth_ = House(TWELVTH, 12, PISCES, "I release")
    houses_ = [first_, second_, third_, fourth_, fifth_, sixth_, seventh_, 
               eight_, ninth_, tenth_, eleventh_, twelvth_]

    def get(self, h):
        first = re.compile(r'firs', re.IGNORECASE)
        second = re.compile(r'sec', re.IGNORECASE)
        third = re.compile(r'thi', re.IGNORECASE)
        fourth = re.compile(r'fou', re.IGNORECASE)
        fifth = re.compile(r'fif', re.IGNORECASE)
        sixth = re.compile(r'six', re.IGNORECASE)
        seventh = re.compile(r'sev', re.IGNORECASE)
        eight = re.compile(r'eig', re.IGNORECASE)
        ninth = re.compile(r'nin', re.IGNORECASE)
        tenth = re.compile(r'ten', re.IGNORECASE)
        eleventh = re.compile(r'ele', re.IGNORECASE)
        twelvth = re.compile(r'twe', re.IGNORECASE)
        
        house = None
        if (first.search(h)) or (h == "1"):
            house = self.first_
        elif (second.search(h)) or (h == "2"):
            house = self.second_
        elif (third.search(h)) or (h == "3"):
            house = self.third_
        elif (fourth.search(h)) or (h == "4"):
            house = self.fourth_
        elif (fifth.search(h)) or (h == "5"):
            house = self.fifth_
        elif (sixth.search(h)) or (h == "6"):
            house = self.sixth_
        elif (seventh.search(h)) or (h == "7"):
            house = self.seventh_
        elif (eight.search(h)) or (h == "8"):
            house = self.eight_
        elif (ninth.search(h)) or (h == "9"):
            house = self.ninth_
        elif (tenth.search(h)) or (h == "10"):
            house = self.tenth_
        elif (eleventh.search(h)) or (h == "11"):
            house = self.eleventh_
        elif (twelvth.search(h)) or (h == "12"):
            house = self.twelvth_
        return house
    
    def print(self, house):
        House.print(house)

    def print_keywords(self, house_name):
        print("\nKeyword list for the " + house_name.upper() + " house:\n")
        for k in Keywords.houses_[house_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for h in self.houses_:
            House.print(h)
