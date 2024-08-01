#
# aspects
#

import re
from constants import *
from keywords import Keywords
from aspect import Aspect
from sign import Sign

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
    
    aspects_ = [conjunction_, opposition_, trine_, square_, sextile_, 
                semisquare_, sesquiquadrate_, semisextile_, quincunx_]

    def get(self, a):    
        conjunction = re.compile(r'con', re.IGNORECASE)
        opposition = re.compile(r'opp', re.IGNORECASE)
        trine = re.compile(r'tri', re.IGNORECASE)
        square = re.compile(r'squ', re.IGNORECASE)
        sextile = re.compile(r'sex', re.IGNORECASE)
        semisquare = re.compile(r'semisq', re.IGNORECASE)
        sesquiquadrate = re.compile(r'ses', re.IGNORECASE)
        semisextile = re.compile(r'semise', re.IGNORECASE)
        quincunx = re.compile(r'qui', re.IGNORECASE)
        
        aspect = None
        if conjunction.search(a):
            aspect = self.conjunction_
        elif opposition.search(a):
            aspect = self.opposition_
        elif trine.search(a):
            aspect = self.trine_
        elif square.search(a):
            aspect = self.square_
        elif sextile.search(a):
            aspect = self.sextile_
        elif semisquare.search(a):
            aspect = self.semisquare_
        elif sesquiquadrate.search(a):
            aspect = self.sesquiquadrate_
        elif semisextile.search(a):
            aspect = self.semisextile_
        elif quincunx.search(a):
            aspect = self.quincunx_
        return aspect

    def get_aspect_from_aspect_angle(aspect_angle):
        match aspect_angle:
            case 0: return Aspects.conjunction_
            case 30: return Aspects.semisextile_
            case 45: return Aspects.semisquare_
            case 60: return Aspects.sextile_
            case 90: return Aspects.square_
            case 120: return Aspects.trine_
            case 135: return Aspects.sesquiquadrate_
            case 150: return Aspects.quincunx_
            case 180: return Aspects.opposition_
            case _ :
                return None
    
    def get_aspect_from_angle(angle):
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

    def print_keywords(self, aspect_name):
        print("\nKeyword list for a " + aspect_name.upper() + " aspect:\n")
        for k in Keywords.aspects_[aspect_name]:
            print("\n\t- " + k)

    # TODO: Integrate
    def print_all(self):
        for a in self.aspects_:
            Aspect.print(a)