#
# signs
#

import re

from aspects import *
from constants import *
from elements import *
from keywords import Keywords
from modes import *
from polarities import *

class Sign:

    def __init__(self, sign, id, degrees, polarity, element, mode, ruler, 
                 detriment, exalted, fall, body, moto):
        self.name_ = sign
        self.id_ = id
        self.degrees_ = degrees
        self.polarity_ = polarity
        self.element_ = element
        self.mode_ = mode
        self.ruler_ = ruler
        self.detriment_ = detriment
        self.exalted_ = exalted
        self.fall_ = fall
        self.body_ = body
        self.moto_ = moto

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nRank\t\t\t:\t", self.id_, 
              "\nStarts at\t\t:\t", self.degrees_, "degrees",
              "\nPolarity\t\t:\t", self.polarity_, 
              "\nElement\t\t\t:\t", self.element_, 
              "\nMode\t\t\t:\t", self.mode_, 
              "\nRuler\t\t\t:\t", self.ruler_,
              "\nDetriment\t\t:\t", self.detriment_,
              "\nExalted\t\t\t:\t", self.exalted_,
              "\nFall\t\t\t:\t", self.fall_, 
              "\nBody part\t\t:\t", self.body_, 
              "\nMoto\t\t\t:\t", self.moto_)

class Signs:
    
    aries_ = Sign(ARIES, 1, 0, POSITIVE, FIRE, CARDINAL, MARS, VENUS, SUN, SATURN, "Head", "I am")
    taurus_ = Sign(TAURUS, 2, 30, NEGATIVE, EARTH, FIXED, VENUS, MARS, MOON, NA, "Neck and throat", "I possess")
    gemini_ = Sign(GEMINI, 3, 60, POSITIVE, AIR, MUTABLE, MERCURY, JUPITER, NA, NA, "Arms hands and lungs", "I think")
    cancer_ = Sign(CANCER, 4, 90, NEGATIVE, WATER, CARDINAL, MOON, SATURN, JUPITER, MARS, "Breasts and stomach", "I feel")
    leo_ = Sign(LEO, 5, 120, POSITIVE, FIRE, FIXED, SUN, SATURN, NA, NA, "Heart", "I will")
    virgo_ = Sign(VIRGO, 6, 150, NEGATIVE, EARTH, MUTABLE, MERCURY, JUPITER, NA, VENUS, "Digestive system and bowel", "I analyze")
    libra_ = Sign(LIBRA, 7, 180, POSITIVE, AIR, CARDINAL, VENUS, MARS, SATURN, SUN, "Kidneys", "I balance")
    scorpio_ = Sign(SCORPIO, 8, 210, NEGATIVE, WATER, FIXED, [MARS, PLUTO], VENUS, NA, MOON,  "Reproductive organs", "I desire")
    sagittarius_ = Sign(SAGITTARIUS, 9, 240, POSITIVE, FIRE, MUTABLE, JUPITER, MERCURY, NA, NA, "Hips and thighs", "I seek")
    capricorn_ = Sign(CAPRICORN, 10, 270, NEGATIVE, EARTH, CARDINAL, SATURN, MOON, MARS, JUPITER, "Knees", "I achieve")
    aquarius_ = Sign(AQUARIUS, 11, 300, POSITIVE, AIR, FIXED, [SATURN, URANUS], SUN, NA, NA, "Shins and ankles", "I know")
    pisces_ = Sign(PISCES, 12, 330, NEGATIVE, WATER, MUTABLE, [JUPITER, NEPTUNE], MERCURY, VENUS, NA, "Feet", "I believe")

    signs_ = [aries_, taurus_, gemini_, cancer_, leo_, virgo_,
              libra_, scorpio_, sagittarius_, capricorn_, aquarius_, pisces_]

    def get(self, input):
        aries = re.compile(rf'^\s*{ARIES}\s*$', re.IGNORECASE)
        taurus = re.compile(rf'^\s*{TAURUS}\s*$', re.IGNORECASE)
        gemini = re.compile(rf'^\s*{GEMINI}\s*$', re.IGNORECASE)
        cancer = re.compile(rf'^\s*{CANCER}\s*$', re.IGNORECASE)
        leo = re.compile(rf'^\s*{LEO}\s*$', re.IGNORECASE)
        virgo = re.compile(rf'^\s*{VIRGO}\s*$', re.IGNORECASE)
        libra = re.compile(rf'^\s*{LIBRA}\s*$', re.IGNORECASE)
        scorpio = re.compile(rf'^\s*{SCORPIO}\s*$', re.IGNORECASE)
        sagittarius = re.compile(rf'^\s*{SAGITTARIUS}\s*$', re.IGNORECASE)
        capricorn = re.compile(rf'^\s*{CAPRICORN}\s*$', re.IGNORECASE)
        aquarius = re.compile(rf'^\s*{AQUARIUS}\s*$', re.IGNORECASE)
        pisces = re.compile(rf'^\s*{PISCES}\s*$', re.IGNORECASE)
        
        if aries.fullmatch(input):
            sign = self.aries_
        elif taurus.fullmatch(input):
            sign = self.taurus_
        elif gemini.fullmatch(input):
            sign = self.gemini_
        elif cancer.fullmatch(input):
            sign = self.cancer_
        elif leo.fullmatch(input):
            sign = self.leo_
        elif virgo.fullmatch(input):
            sign = self.virgo_
        elif libra.fullmatch(input):
            sign = self.libra_
        elif scorpio.fullmatch(input):
            sign = self.scorpio_
        elif sagittarius.fullmatch(input):
            sign = self.sagittarius_
        elif capricorn.fullmatch(input):
            sign = self.capricorn_
        elif aquarius.fullmatch(input):
            sign = self.aquarius_
        elif pisces.fullmatch(input):
            sign = self.pisces_
        else:
            return None
        return sign

    def find_common_planet(self, sign_a: Sign, sign_b: Sign):
        planet = None
        planet_a_is_list = False
        planet_b_is_list = False

        if isinstance(sign_a.ruler_, list):
            planet_a_is_list = True
        if isinstance(sign_b.ruler_, list):
            planet_b_is_list = True

        if (planet_a_is_list == True) and (planet_b_is_list == True):
            for i in range(0, 1):
                for j in range(0, 1):
                    if sign_a.ruler_[i] == sign_b.ruler_[j]:
                        planet = sign_a.planet_[i]
        elif (planet_a_is_list == True) and (planet_b_is_list == False):
            for i in range(0, 1):
                if sign_b.ruler_ == sign_a.ruler_[i]:
                    planet = sign_b.ruler_
        elif (planet_a_is_list == False) and (planet_b_is_list == True):
            for i in range(0, 1):
                if sign_a.ruler_ == sign_b.ruler_[i]:
                    planet = sign_a.ruler_
        else:
            if sign_a.ruler_ == sign_b.ruler_:
                planet = sign_a.ruler_

        return planet

    def print(self, sign):
        Sign.print(sign)

    def print_keywords(self, keyword):
        print("\nKeyword list for sign " + keyword.upper() + ":\n")
        for k in Keywords.signs_[keyword]:
            print("\t- " + k)

    def print_arc(self, sign):
        print("Degrees\t\t\t:\t[", sign.degrees_, ",", sign.degrees_ + 30, ")\n")

    def print_signs_in_polarity(self, p):
        polarity = Polarities.get(Polarities, p)
        if polarity == None:
            print(E_POLARITY)
            return
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity.name_:
                list.append(s.name_)
        print(polarity.name_, "signs\t\t:\t", list)
        print("\n")

    def print_signs_in_mode(self, m):
        mode = Modes.get(Modes, m)
        if mode == None:
            print(E_MODE)
            return
        list = []
        for s in self.signs_:
            if s.mode_ == mode.name_:
                list.append(s.name_)
        print(mode.name_, "signs\t\t:\t", list)
        print("\n")

    def print_signs_in_element(self, e):
        element = Elements.get(Elements, e)
        if element == None:
            print(E_ELEMENT)
            return
        list = []
        for s in self.signs_:
            if s.element_ == element.name_:
                list.append(s.name_)
        print(element.name_, "signs\t\t:\t", list)
        print("\n")

    def find_two_common_attributes(self, sign):
        list = []
        for s in Signs.signs_:
            similarities = 0
            if sign.name_ == s.name_:
                continue
            if sign.polarity_ == s.polarity_:
                similarities = similarities + 1
            if sign.mode_ == s.mode_:
                similarities = similarities + 1
            if sign.element_ == s.element_:
                similarities = similarities + 1
            planet = Signs.find_common_planet(Signs, sign, s)
            if planet != None:
                similarities = similarities + 1
            if similarities > 1:
                list.append(s)
        return list

    def print_common_attributes(self, sign_a, sign_b):
        similarities = 0

        # Print common and relating attribites of the signs
        print("\nSigns\t\t\t:\t", sign_a.name_.upper(), "and", sign_b.name_.upper())
        
        # 1. Check aspect
        aspect_angle = Aspects.calculate_aspect_angle(Aspects, sign_a, sign_b)
        aspect = Aspects.get_aspect_from_angle(aspect_angle)
        if aspect != None:
            print("Aspect\t\t\t:\t", aspect.name_)
        print("Aspect degrees\t\t:\t", aspect_angle)
        
        # 2. Check polarity
        if sign_a.polarity_ == sign_b.polarity_:
            print("Same polarity\t\t:\t", sign_a.polarity_)
            similarities = similarities + 1

        # 3. Check mode
        if sign_a.mode_ == sign_b.mode_:
            print("Same mode\t\t:\t", sign_a.mode_)
            similarities = similarities + 1

        # 4. Check element
        if sign_a.element_ == sign_b.element_:
            print("Same element\t\t:\t", sign_a.element_)
            similarities = similarities + 1

        # 5. Check planet
        planet = Signs.find_common_planet(Signs, sign_a, sign_b)
        if planet != None:
            print ("Same ruler\t\t:\t", planet)
            similarities = similarities + 1

        # 6. Sum up
        print("\n")
        if similarities == 0:
            print(sign_a.name_, "and", sign_b.name_, 
                "do not have anything in common")
        else:
            print(sign_a.name_, "and", sign_b.name_, 
                "have", similarities, "out of 4 attributes in common")
        print("\n")

    def print_polarity_mode(self, polarity, mode):
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity and s.mode_ == mode:
                list.append(s.name_)
        print(polarity, "and", mode, "\t:\t", list)

    def print_mode_element(self, mode, element):
        list = []
        for s in self.signs_:
            if s.element_ == element and s.mode_ == mode:
                list.append(s.name_)
        print(mode, "/", element, "\t:\t", list)

    def print_element_polarity(self, element, polarity):
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity and s.element_ == element:
                list.append(s.name_)
        print(element, "/", polarity, "\t:\t", list)

    def get_sign_from_degree(self, deg: float):
        deg = deg % 360
        if deg >= self.aries_.degrees_ and deg < self.taurus_.degrees_:
            sign = self.aries_
        elif deg >= self.taurus_.degrees_ and deg < self.gemini_.degrees_:
            sign = self.taurus_
        elif deg >= self.gemini_.degrees_ and deg < self.cancer_.degrees_:
            sign = self.gemini_
        elif deg >= self.cancer_.degrees_ and deg < self.leo_.degrees_:
            sign = self.cancer_
        elif deg >= self.leo_.degrees_ and deg < self.virgo_.degrees_:
            sign = self.leo_
        elif deg >= self.virgo_.degrees_ and deg < self.libra_.degrees_:
            sign = self.virgo_
        elif deg >= self.libra_.degrees_ and deg < self.scorpio_.degrees_:
            sign = self.libra_
        elif deg >= self.scorpio_.degrees_ and deg < self.sagittarius_.degrees_:
            sign = self.scorpio_
        elif deg >= self.sagittarius_.degrees_ and deg < self.capricorn_.degrees_:
            sign = self.sagittarius_
        elif deg >= self.capricorn_.degrees_ and deg < self.aquarius_.degrees_:
            sign = self.capricorn_
        elif deg >= self.aquarius_.degrees_ and deg < self.pisces_.degrees_:
            sign = self.aquarius_
        elif deg >= self.pisces_.degrees_ and deg < self.pisces_.degrees_ + 30: # = 360
            sign = self.pisces_
        else:
            return None
        return sign
