#
# aspects
#

from aspect import Aspect
from constants import *

class Aspects:

    conjunction_ = Aspect(CONJUNCTION, 0, "1:1", 1, "8°", "Sign")    
    opposition_ = Aspect(OPPOSITION, 180, "1:2", 2, "8°", ["Polarity", "Mode"])
    trine_ = Aspect(TRINE, 120, "1:3", 3, "8°", "Element")
    square_ = Aspect(SQUARE, 90, "1:4", 2, "8°", "Mode")
    sextile_ = Aspect(SEXTILE, 60, "1:6", [2, 3], "4°", ["Polarity", "Compatible element"])
    semisquare_ = Aspect(SEMISQUARE, 45, "1:8", 2, "2°", "N/A")
    sesquiquadrate_ = Aspect(SESQUIQUADRATE, 135, "3:8", [2, 3], "2°", "N/A")
    semisextile_ = Aspect(SEMISEXTILE, 30, "1:12", [2, 3], "2°", "Nothing")
    quincunx_ = Aspect(QUINCUNX, 150, "5:12", [2, 3, 5], "2°", "Nothing")

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
    
    planets_ = [conjunction_, opposition_, trine_, square_, sextile_, semisquare_, sesquiquadrate_,
                semisextile_, quincunx_]

    def get(self, i):
        match(i):
            case "Conjunction" | "conjunction" | "CO" | "co" : 
                aspect = self.conjunction_
            case "Opposition" | "opposition" | "OP" | "op" : 
                aspect = self.opposition_
            case "Trine" | "trine" | "TR" | "tr" : 
                aspect = self.trine_
            case "Square" | "square" | "SQ" | "sq" : 
                aspect = self.square_
            case "Sextile" | "sextile" | "SX" | "sx" : 
                aspect = self.sextile_
            case "Semisquare" | "semisquare" | "SSQ" | "ssq" : 
                aspect = self.semisquare_
            case "Sesquiquadrate" | "sesquiquadrate" | "SES" | "ses" : 
                aspect = self.sesquiquadrate_
            case "Semisextile" | "semisextile" | "SS" | "ss" : 
                aspect = self.semisextile_
            case "Quincunx" | "quincunx" | "QN" | "qn" : 
                aspect = self.quincunx_
            case _ :
                return -1
        return aspect

    def print(self, aspect):
        Aspect.print(aspect)

    def print_keywords(self, aspect_name):
        print("\nKeyword list for a " + aspect_name.upper() + " aspect:\n")
        for k in Aspects.keywords_[aspect_name]:
            print("\n\t- " + k)

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
                return -1