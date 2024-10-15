#
# aspects
#

import re
from constants import *
from keywords import Keywords

class Aspect:
   
    def __init__(self, name, angle, fraction, root_numbers, orb, same, types):
        self.name_ = name
        self.angle_ = angle
        self.fraction_ = fraction
        self.root_numbers_ = root_numbers
        self.orb_ = orb
        self.same_ = same
        self.types_ = types
    
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(),
              "\nAngle\t\t\t:\t", self.angle_, "degrees",
              "\nFraction\t\t:\t", self.fraction_,
              "\nRoot numbers\t\t:\t", self.root_numbers_,
              "\nOrb\t\t\t:\t", self.orb_,
              "\nSame\t\t\t:\t", self.same_,
              "\nTypes\t\t\t:\t", self.types_, "\n")

class Aspects:

    conjunction_ = Aspect(CONJUNCTION, 0, "1:1", 1, 8, "Sign", NA)    
    opposition_ = Aspect(OPPOSITION, 180, "1:2", 2, 8, ["Polarity", "Mode"], [["Cardinal", "Fixed", "Mutable"], ["Positive", "Negative"]])
    trine_ = Aspect(TRINE, 120, "1:3", 3, 8, "Element", ["Fire", "Earth", "Air", "Water"])
    square_ = Aspect(SQUARE, 90, "1:4", 2, 8, "Mode", ["Cardinal", "Fixed", "Mutable"])
    sextile_ = Aspect(SEXTILE, 60, "1:6", [2, 3], 4, ["Polarity", "Compatible element"], [["Positive", "Negative"], ["Fire to Air", "Air to Fire", "Earth to water", "Water to earth"]])
    semisquare_ = Aspect(SEMISQUARE, 45, "1:8", 2, 2, NA, NA)
    sesquiquadrate_ = Aspect(SESQUIQUADRATE, 135, "3:8", [2, 3], 2, NA, NA)
    semisextile_ = Aspect(SEMISEXTILE, 30, "1:12", [2, 3], 2, "Nothing", NA)
    quincunx_ = Aspect(QUINCUNX, 150, "5:12", [2, 3, 5], 2, "Nothing", NA)

    # TODO: Add a custom aspect that can be set from the user at execution time and 
    # persistently stored

    # TODO: add this functionality to the custom aspect
    # - Get favorite number
    # - 360 / favorite number
    # - Report in the chart
    
    # TODO: Make the orbs configurable from the user as well with an option to be
    # reset to defaults

    aspects_ = [conjunction_, opposition_, trine_, square_,
                sextile_, semisquare_, sesquiquadrate_, 
                semisextile_, quincunx_]

    def get(self, input):    
        conjunction = re.compile(rf'^\s*{CONJUNCTION}\s*$', re.IGNORECASE)
        opposition = re.compile(rf'^\s*{OPPOSITION}\s*$', re.IGNORECASE)
        trine = re.compile(rf'^\s*{TRINE}\s*$', re.IGNORECASE)
        square = re.compile(rf'^\s*{SQUARE}\s*$', re.IGNORECASE)
        sextile = re.compile(rf'^\s*{SEXTILE}\s*$', re.IGNORECASE)
        semisquare = re.compile(rf'^\s*{SEMISQUARE}\s*$', re.IGNORECASE)
        sesquiquadrate = re.compile(rf'^\s*{SESQUIQUADRATE}\s*$', re.IGNORECASE)
        semisextile = re.compile(rf'^\s*{SEMISEXTILE}\s*$', re.IGNORECASE)
        quincunx = re.compile(rf'^\s*{QUINCUNX}\s*$', re.IGNORECASE)
        
        if conjunction.fullmatch(input):
            aspect = self.conjunction_
        elif opposition.fullmatch(input):
            aspect = self.opposition_
        elif trine.fullmatch(input):
            aspect = self.trine_
        elif square.fullmatch(input):
            aspect = self.square_
        elif sextile.fullmatch(input):
            aspect = self.sextile_
        elif semisquare.fullmatch(input):
            aspect = self.semisquare_
        elif sesquiquadrate.fullmatch(input):
            aspect = self.sesquiquadrate_
        elif semisextile.fullmatch(input):
            aspect = self.semisextile_
        elif quincunx.fullmatch(input):
            aspect = self.quincunx_
        else:
            return None
        return aspect
    
    def get_aspect_from_angle(angle: float):
        """Gets the angle as a float to incorporate minutes and compares it
        to the angle of the sign itself"""
        if angle <= Aspects.conjunction_.angle_ + Aspects.conjunction_.orb_ and \
            angle >= Aspects.conjunction_.angle_ - Aspects.conjunction_.orb_:
            return Aspects.conjunction_
        elif angle <= Aspects.semisextile_.angle_ + Aspects.semisextile_.orb_ and \
            angle >= Aspects.semisextile_.angle_ - Aspects.semisextile_.orb_:
            return Aspects.semisextile_
        elif angle <= Aspects.semisquare_.angle_ + Aspects.semisquare_.orb_ and \
            angle >= Aspects.semisquare_.angle_ - Aspects.semisquare_.orb_:
            return Aspects.semisquare_
        elif angle <= Aspects.sextile_.angle_ + Aspects.sextile_.orb_ and \
            angle >= Aspects.sextile_.angle_ - Aspects.sextile_.orb_:
            return Aspects.sextile_
        elif angle <= Aspects.square_.angle_ + Aspects.square_.orb_ and \
            angle >= Aspects.square_.angle_ - Aspects.square_.orb_:
            return Aspects.square_
        elif angle <= Aspects.trine_.angle_+ Aspects.trine_.orb_ and \
            angle >= Aspects.trine_.angle_ - Aspects.trine_.orb_:
            return Aspects.trine_
        elif angle <= Aspects.sesquiquadrate_.angle_ + Aspects.sesquiquadrate_.orb_ and \
            angle >= Aspects.sesquiquadrate_.angle_ - Aspects.sesquiquadrate_.orb_:
            return Aspects.sesquiquadrate_
        elif angle <= Aspects.quincunx_.angle_ + Aspects.quincunx_.orb_ and \
            angle >= Aspects.quincunx_.angle_ - Aspects.quincunx_.orb_:
            return Aspects.quincunx_
        elif angle <= Aspects.opposition_.angle_ + Aspects.opposition_.orb_ and \
            angle >= Aspects.opposition_.angle_ - Aspects.opposition_.orb_:
            return Aspects.opposition_
        else:
            return None

    def calculate_aspect_angle(self, sign_a, sign_b):
        aspect_angle = abs(sign_a.degrees_ - sign_b.degrees_)
        if aspect_angle > 180:
            d_180 = aspect_angle - 180
            aspect_angle = 180 - d_180
        return aspect_angle

    def print(self, aspect):
        Aspect.print(aspect)

    def print_keywords(self, keyword):
        print("\nKeyword list for a " + keyword.upper() + " aspect:\n")
        for k in Keywords.aspects_[keyword]:
            print("\n\t- " + k)
