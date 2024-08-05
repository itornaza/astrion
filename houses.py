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
        first = re.compile(rf'{FIRST}|{"1"}', re.IGNORECASE)
        second = re.compile(rf'{SECOND}|{"2"}', re.IGNORECASE)
        third = re.compile(rf'{THIRD}|{"3"}', re.IGNORECASE)
        fourth = re.compile(rf'{FOURTH}|{"4"}', re.IGNORECASE)
        fifth = re.compile(rf'{FIFTH}|{"5"}', re.IGNORECASE)
        sixth = re.compile(rf'{SIXTH}|{"6"}', re.IGNORECASE)
        seventh = re.compile(rf'{SEVENTH}|{"7"}', re.IGNORECASE)
        eight = re.compile(rf'{EIGHT}|{"8"}', re.IGNORECASE)
        ninth = re.compile(rf'{NINTH}|{"9"}', re.IGNORECASE)
        tenth = re.compile(rf'{TENTH}|{"10"}', re.IGNORECASE)
        eleventh = re.compile(rf'{ELEVENTH}|{"11"}', re.IGNORECASE)
        twelvth = re.compile(rf'{TWELVTH}|{"12"}', re.IGNORECASE)
        
        house = None
        if (first.fullmatch(h)):
            house = self.first_
        elif (second.fullmatch(h)):
            house = self.second_
        elif (third.fullmatch(h)):
            house = self.third_
        elif (fourth.fullmatch(h)):
            house = self.fourth_
        elif (fifth.fullmatch(h)):
            house = self.fifth_
        elif (sixth.fullmatch(h)):
            house = self.sixth_
        elif (seventh.fullmatch(h)):
            house = self.seventh_
        elif (eight.fullmatch(h)):
            house = self.eight_
        elif (ninth.fullmatch(h)):
            house = self.ninth_
        elif (tenth.fullmatch(h)):
            house = self.tenth_
        elif (eleventh.fullmatch(h)):
            house = self.eleventh_
        elif (twelvth.fullmatch(h)):
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
