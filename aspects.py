#
# aspects
#

import re
from constants import *
from aspect import Aspect
from sign import Sign

class Aspects:

    conjunction_ = Aspect(CONJUNCTION, 0, "1:1", 1, "8°", "Sign", NA)    
    opposition_ = Aspect(OPPOSITION, 180, "1:2", 2, "8°", ["Polarity", "Mode"], [["Cardinal", "Fixed", "Mutable"], ["Positive", "Negative"]])
    trine_ = Aspect(TRINE, 120, "1:3", 3, "8°", "Element", ["Fire", "Earth", "Air", "Water"])
    square_ = Aspect(SQUARE, 90, "1:4", 2, "8°", "Mode", ["Cardinal", "Fixed", "Mutable"])
    sextile_ = Aspect(SEXTILE, 60, "1:6", [2, 3], "4°", ["Polarity", "Compatible element"], [["Positive", "Negative"], ["Fire to Air", "Air to Fire", "Earth to water", "Water to earth"]])
    semisquare_ = Aspect(SEMISQUARE, 45, "1:8", 2, "2°", NA, NA)
    sesquiquadrate_ = Aspect(SESQUIQUADRATE, 135, "3:8", [2, 3], "2°", NA, NA)
    semisextile_ = Aspect(SEMISEXTILE, 30, "1:12", [2, 3], "2°", "Nothing", NA)
    quincunx_ = Aspect(QUINCUNX, 150, "5:12", [2, 3, 5], "2°", "Nothing", NA)
    aspects_ = [conjunction_, opposition_, trine_, square_, sextile_, 
                semisquare_, sesquiquadrate_, semisextile_, quincunx_]
    keywords_ = {
        CONJUNCTION: [
            "...... and ...... are at one with each other",
            "...... automatically combines with ......",
            "There is a synthesis between ...... and ......",
            "The expression of ...... is obscured by ......",
            "It is impossible to ...... without also ......",
            "The individual cannot differentiate between ...... and ...... ",
            "There is a natural affinity between ...... and ......",
            "There is a concentrated focus of ...... and ......"
        ],

        OPPOSITION: [
            "An inner conflict between ...... and ......", 
            "Swinging between ...... and ......",
            "Feeling split between ...... and ......",
            "Unable to decide whether to ...... or ......",
            "The ability to develop a healthy balance between ...... and ...... ",
            "Learning to recognise both ...... and ......"
        ],

        TRINE: [
            "He/she is easy and comfortable when it comes to ......", 
            "He/she enjoys and finds pleasure in ......",
            "He/she adopts the line of least resistance by ......", 
            "He/she takes it for granted that ......"
        ],

        SQUARE: [
            "He/she struggles to actively and effectively integrate ......",
            "He/she is confronted by the need to ......",
            "He/she finds themselves challenged to ......",
            "He/she seems to be frustrated and blocked by ......",
            "It is a big challenge for him/her to ......",
            "He/she gets a great deal of personal satisfaction when he/she achieves ......"            
        ],

        SEXTILE: [
            "He/she is motivated to ......",
            "He/she can skilfully work towards ......",
            "He/she can ......",
            "He/she is able to combine ......"
        ],
        
        SEMISQUARE: [
            "He/she achieves productive and tangible results when he/she combines ......", 
            "He/she is determined to ......",
            "He/she finds it necessary to manifest ......",
            "He/she can produce ......",
            "He/she puts effort into ......",
            "He/she struggles or works hard to achieve ......"
        ],
        
        SESQUIQUADRATE: [
            "He/she achieves productive and tangible results when he/she combines ......", 
            "He/she is determined to ......",
            "He/she finds it necessary to manifest ......",
            "He/she can produce ......",
            "He/she puts effort into ......",
            "He/she struggles or works hard to achieve ......"
        ],
        
        SEMISEXTILE: [
            "He/she is constantly adjusting ......",
            "He/she feels uncomfortable with ......",
            "He/she is uneasy about ......",
            "He/she finds it difficult to see how ...... can work effectively together with ......",
            "He/she makes attempts to accommodate both ...... and ......"
        ],
        
        QUINCUNX: [
            "He/she is constantly adjusting ......",
            "He/she feels uncomfortable with ......",
            "He/she is uneasy about ......",
            "He/she finds it difficult to see how ...... can work effectively together with ......",
            "He/she makes attempts to accommodate both ...... and ......"
        ]
    }

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
        match(aspect_angle):
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
        for k in Aspects.keywords_[aspect_name]:
            print("\n\t- " + k)

    # TODO: Integrate
    def print_all(self):
        for a in self.aspects_:
            Aspect.print(a)