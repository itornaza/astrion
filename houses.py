#
# house
#

import re

from constants import *
from keywords import Keywords

class House:

    def __init__(self, house, id, sign_affinity, moto):
        self.name_ = house
        self.id_ = id
        self.sign_affinity_ = sign_affinity
        self.moto_ = moto

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nRank\t\t\t:\t", self.id_, 
              "\nSign\t\t\t:\t", self.sign_affinity_, 
              "\nMoto\t\t\t:\t", self.moto_, "\n")

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

    houses_ = [first_, second_, third_, fourth_,fifth_, sixth_, 
               seventh_, eight_, ninth_, tenth_, eleventh_, twelvth_]

    def get(self, input):
        first = re.compile(rf'^\s*({FIRST}|{"1"})\s*$', re.IGNORECASE)
        second = re.compile(rf'^\s*({SECOND}|{"2"})\s*$', re.IGNORECASE)
        third = re.compile(rf'^\s*({THIRD}|{"3"})\s*$', re.IGNORECASE)
        fourth = re.compile(rf'^\s*({FOURTH}|{"4"})\s*$', re.IGNORECASE)
        fifth = re.compile(rf'^\s*({FIFTH}|{"5"})\s*$', re.IGNORECASE)
        sixth = re.compile(rf'^\s*({SIXTH}|{"6"})\s*$', re.IGNORECASE)
        seventh = re.compile(rf'^\s*({SEVENTH}|{"7"})\s*$', re.IGNORECASE)
        eight = re.compile(rf'^\s*({EIGHT}|{"8"})\s*$', re.IGNORECASE)
        ninth = re.compile(rf'^\s*({NINTH}|{"9"})\s*$', re.IGNORECASE)
        tenth = re.compile(rf'^\s*({TENTH}|{"10"})\s*$', re.IGNORECASE)
        eleventh = re.compile(rf'^\s*({ELEVENTH}|{"11"})\s*$', re.IGNORECASE)
        twelvth = re.compile(rf'^\s*({TWELVTH}|{"12"})\s*$', re.IGNORECASE)
        
        if first.fullmatch(input):
            house = self.first_
        elif second.fullmatch(input):
            house = self.second_
        elif third.fullmatch(input):
            house = self.third_
        elif fourth.fullmatch(input):
            house = self.fourth_
        elif fifth.fullmatch(input):
            house = self.fifth_
        elif sixth.fullmatch(input):
            house = self.sixth_
        elif seventh.fullmatch(input):
            house = self.seventh_
        elif eight.fullmatch(input):
            house = self.eight_
        elif ninth.fullmatch(input):
            house = self.ninth_
        elif tenth.fullmatch(input):
            house = self.tenth_
        elif eleventh.fullmatch(input):
            house = self.eleventh_
        elif twelvth.fullmatch(input):
            house = self.twelvth_
        else:
            return None
        return house
    
    def print(self, house):
        House.print(house)

    def print_keywords(self, keyword):
        print("\nKeyword list for the " + keyword.upper() + " house:\n")
        for k in Keywords.houses_[keyword]:
            print("\t- " + k)
