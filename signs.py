#
# signs
#

import re
from constants import *
from sign import Sign
from elements import Elements
from polarities import Polarities
from modes import Modes

class Signs:
    
    aries_ = Sign(ARIES, 1, 0, POSITIVE, FIRE, CARDINAL, MARS, "Head", "I am")
    taurus_ = Sign(TAURUS, 2, 30, NEGATIVE, EARTH, FIXED, VENUS, "Neck and throat", "I possess")
    gemini_ = Sign(GEMINI, 3, 60, POSITIVE, AIR, MUTABLE, MERCURY, "Arms hands and lungs", "I think")
    cancer_ = Sign(CANCER, 4, 90, NEGATIVE, WATER, CARDINAL, MOON, "Breasts and stomach", "I feel")
    leo_ = Sign(LEO, 5, 120, POSITIVE, FIRE, FIXED, SUN, "Heart", "I will")
    virgo_ = Sign(VIRGO, 6, 150, NEGATIVE, EARTH, MUTABLE, MERCURY, "Digestive system and bowel", "I analyze")
    libra_ = Sign(LIBRA, 7, 180, POSITIVE, AIR, CARDINAL, VENUS, "Kidneys", "I balance")
    scorpio_ = Sign(SCORPIO, 8, 210, NEGATIVE, WATER, FIXED, [MARS, PLUTO], "Reproductive organs", "I desire")
    sagittarius_ = Sign(SAGITTARIUS, 9, 240, POSITIVE, FIRE, MUTABLE, JUPITER, "Hips and thighs", "I seek")
    capricorn_ = Sign(CAPRICORN, 10, 270, NEGATIVE, EARTH, CARDINAL, SATURN, "Knees", "I achieve")
    aquarius_ = Sign(AQUARIUS, 11, 300, POSITIVE, AIR, FIXED, [SATURN, URANUS],"Shins and ankles", "I know")
    pisces_ = Sign(PISCES, 12, 330, NEGATIVE, WATER, MUTABLE, [JUPITER, NEPTUNE], "Feet", "I believe")

    keywords_ = {
        ARIES: [
            "enthusiasm", "initiative", "drive", "action", "courageous", "energetic", "sef-motivated", "decisive", 
            "rash", "wilful", "selfish", "coarse", "locking horns", "battering ram", "zestful", "exuberant", 
            "outgoing", "work alone", "lead", "imppatient", "childlike behaviour", "spontaneous"
        ],
        
        TAURUS: [
            "deliberate", "patient", "placid", "practical", "persistent", "grounded", "acquisitive", "sensual", 
            "stubborn", "unimaginative", "possessive", "self-indulgent", "simplistic", "comfort", "considered", 
            "formidable temper", "red rug to a bull", "stability", "resistance to change"
        ],
        
        GEMINI: [
            "versatile", "intellectual", "rational", "communicative", "sociable", "adaptable", "diverse", 
            "quick-witted", "flirtarious", "unpredictable", "duplicitous", "shallow", "restless", "charming", 
            "movement", "stimulation", "emotional changeability"
        ],
        
        CANCER: [
            "emotional", "receptive", "tenacious", "caring", "sensitive", "nurturing", "imaginative", "supportive", 
            "moody", "smothering", "neurotic", "domineering", "mothering", "creative", "assertive in a covert way", 
            "empathy"
        ],
        
        LEO: [
            "grand", "playful", "loyal", "creative", "generous", "confident", "authoritative", "performer", 
            "self-centered", "arrogant", "authoritarian", "attention-seeker"
        ],
        
        VIRGO: [
            "discriminating", "analytical", "methodical", "practical", "fastidious", "efficient", "compliant", 
            "effective", "fussy", "perfectionist", "submissive", "neurotic", "self-contained thinker"
        ],
        
        LIBRA: [
            "loving", "balanced", "sociable", "relationship-oriented", "fair-minded", "gracious", "co-operative", 
            "peace-loving", "indecisive", "gushing", "confrontational", "over-compromising", "diplomatic", 
            "fair play", "charming", "grace"
        ],
        
        SCORPIO: [
            "resourceful", "intuitive", "insightful", "determined", "passionate", "private", "sensitive", "powerful",
            "jealous", "secretive", "unforgiving", "overbearing", "powerful emotions", "intensity", "regeneration", 
            "fighter"
        ],
        
        SAGITTARIUS: [
            "οptimistic", "enthousiastic", "adventurous", "philosophical", "freedom-loving", "honest", "outgoing", 
            "wise", "non-committal", "blunt", "indiscriminate", "dogmatic"
        ],
        
        CAPRICORN: [
            "patient", "organised", "serious", "conservative", "controlled", "frugal", "ambitious", "strategic", 
            "guarded", "ungenerous", "ruthless", "calculating", "duty", "responsibility", "realistic", "careful"
        ],
        
        AQUARIUS: [
            "society-oriented", "independent", "rational", "detached", "unconventional", "humanitarian", "friendly", 
            "idealistic", "eccentric", "distant", "impersonal", "inflexible"
        ],
        
        PISCES: [
            "sensitive", "compassionate", "receptive", "imaginative", "sympathetic", "dreamy", "psychic", "passive", 
            "sentimental", "unfocused", "neurotic", "submissive"
        ]
    }

    signs_ = [aries_, taurus_, gemini_, cancer_, leo_, virgo_, libra_, 
              scorpio_, sagittarius_, capricorn_, aquarius_, pisces_]

    def get(self, s):
        aries = re.compile(r'ari', re.IGNORECASE)
        taurus = re.compile(r'tau', re.IGNORECASE)
        gemini = re.compile(r'gem', re.IGNORECASE)
        cancer = re.compile(r'can', re.IGNORECASE)
        leo = re.compile(r'leo', re.IGNORECASE)
        virgo = re.compile(r'vir', re.IGNORECASE)
        libra = re.compile(r'lib', re.IGNORECASE)
        scorpio = re.compile(r'sco', re.IGNORECASE)
        sagittarius = re.compile(r'sag', re.IGNORECASE)
        capricorn = re.compile(r'cap', re.IGNORECASE)
        aquarius = re.compile(r'aqu', re.IGNORECASE)
        pisces = re.compile(r'pis', re.IGNORECASE)

        if aries.search(s) != None:
            sign = self.aries_
        elif taurus.search(s) != None:
            sign = self.taurus_
        elif gemini.search(s) != None:
            sign = self.gemini_
        elif cancer.search(s) != None:
            sign = self.cancer_
        elif leo.search(s) != None:
            sign = self.leo_
        elif virgo.search(s) != None:
            sign = self.virgo_
        elif libra.search(s) != None:
            sign = self.libra_
        elif scorpio.search(s) != None:
            sign = self.scorpio_
        elif sagittarius.search(s) != None:
            sign = self.sagittarius_
        elif capricorn.search(s) != None:
            sign = self.capricorn_
        elif aquarius.search(s) != None:
            sign = self.aquarius_
        elif pisces.search(s) != None:
            sign = self.pisces_
        else:
            return -1
        return sign

    def print(self, sign):
        Sign.print(sign)

    def print_keywords(self, sign_name):
        print("\nKeyword list for sign " + sign_name.upper() + ":\n")
        for k in Signs.keywords_[sign_name]:
            print("\t- " + k)

    def print_arc(self, sign):
        print("Degrees\t\t\t:\t[", sign.degrees_, ",", sign.degrees_ + 30, ")\n")

    def print_signs_in_polarity(self, p):
        polarity = Polarities.get(Polarities, p)
        if polarity == -1:
            print("Invalid polarity!")
            return
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity.name_:
                list.append(s.name_)
        print(polarity.name_, "signs\t\t:\t", list)
        print("\n")

    def print_signs_in_mode(self, m):
        mode = Modes.get(Modes, m)
        if mode == -1:
            print("Invalid mode!")
            return
        list = []
        for s in self.signs_:
            if s.mode_ == mode.name_:
                list.append(s.name_)
        print(mode.name_, "signs\t\t:\t", list)
        print("\n")

    def print_signs_in_element(self, e):
        element = Elements.get(Elements, e)
        if element == -1:
            print("Invalid element!")
            return
        list = []
        for s in self.signs_:
            if s.element_ == element.name_:
                list.append(s.name_)
        print(element.name_, "signs\t\t:\t", list)
        print("\n")

    ###########################################################################
    # TODO: Integrate the following methods
    ###########################################################################

    def print_all(self):
        for s in self.signs_:
            Sign.print(s)

    def print_polarity_element(self, polarity, element):
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity and s.element_ == element:
                list.append(s.name_)
        print(polarity, "/", element, ": ", list)

    def print_polarity_mode(self, polarity, mode):
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity and s.mode_ == mode:
                list.append(s.name_)
        print(polarity, "/", mode, ": ", list)

    def print_element_mode(self, element, mode):
        list = []
        for s in self.signs_:
            if s.element_ == element and s.mode_ == mode:
                list.append(s.name_)
        print(element, "/", mode, ": ", list)

    def print_2_commons(self, sign):
        list = []
        for s in self.signs_:
            if s.sign_ == sign.sign_:
                pass
            elif s.element_ == sign.element_ and (s.mode_ == sign.mode_ or s.polarity_ == sign.polarity_):
                list.append(s.name_)
        print(sign.name_, "has 2 in common with", list)

