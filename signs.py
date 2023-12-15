#
# signs
#

from sign import Sign
from elements import Elements
from constants import *

class Signs:
    
    aries_ = Sign(ARIES, 1, 0, POSITIVE, FIRE, CARDINAL, MARS, "Head", "I am")
    taurus_ = Sign(TAURUS, 2, 30, NEGATIVE, EARTH, FIXED, VENUS, "Neck and throat", "I possess")
    gemini_ = Sign(GEMINI, 3, 60, POSITIVE, AIR, MUTABLE, MERCURY, "Arms hands and lungs", "I think")
    cancer_ = Sign(CANCER, 4, 90, NEGATIVE, WATER, CARDINAL, MOON, "Breasts and stomach", "I feel")
    leo_ = Sign(LEO, 5, 120, POSITIVE, FIRE, FIXED, SUN, "Heart", "I will")
    virgo_ = Sign(VIRGO, 6, 150, NEGATIVE, EARTH, MUTABLE, MERCURY, "Digestive system and bowel", "I analyze")
    libra_ = Sign(LIBRA, 7, 180, POSITIVE, AIR, CARDINAL, VENUS, "Kidneys", "I balance")
    scorpio_ = Sign(SCORPIO, 8, 210, NEGATIVE, WATER, FIXED, [MARS, PLUTO], "Reproductive organs", "I desire")
    sagittarius_ = Sign(SAGITTARIUS, 9, 230, POSITIVE, FIRE, MUTABLE, JUPITER, "Hips and thighs", "I seek")
    capricorn_ = Sign(CAPRICORN, 10, 260, NEGATIVE, EARTH, CARDINAL, SATURN, "Knees", "I achieve")
    aquarius_ = Sign(AQUARIUS, 11, 290, POSITIVE, AIR, FIXED, [SATURN, URANUS],"Shins and ankles", "I know")
    pisces_ = Sign(PISCES, 12, 330, NEGATIVE, WATER, MUTABLE, [JUPITER, NEPTUNE], "Feet", "I believe")

    keywords_ = {
        ARIES: ["enthusiasm", "initiative", "drive", "action", "courageous", "energetic",
                  "sef-motivated", "decisive", "rash", "wilful", "selfish", "coarse", 
                  "locking horns", "battering ram", "zestful", "exuberant", "outgoing",
                  "work alone", "lead", "imppatient", "childlike behaviour", "spontaneous"],
        TAURUS: ["deliberate", "patient", "placid", "practical", "persistent", "grounded",
                   "acquisitive", "sensual", "stubborn", "unimaginative", "possessive", 
                   "self-indulgent", "simplistic", "comfort", "considered", 
                   "formidable temper", "red rug to a bull", "stability", "resistance to change"],
        GEMINI: ["versatile", "intellectual", "rational", "communicative", "sociable",
                   "adaptable", "diverse", "quick-witted", "flirtarious", "unpredictable",
                   "duplicitous", "shallow", "restless", "charming", "movement", "stimulation",
                   "emotional changeability"],
        CANCER: ["emotional", "receptive", "tenacious", "caring", "sensitive", "nurturing",
                   "imaginative", "supportive", "moody", "smothering", "neurotic", "domineering",
                   "mothering", "creative", "assertive in a covert way", "empathy"],
        LEO: ["grand", "playful", "loyal", "creative", "generous", "confident", "authoritative",
                "performer", "self-centered", "arrogant", "authoritarian", "attention-seeker"],
        VIRGO: ["discriminating", "analytical", "methodical", "practical", "fastidious",
                  "efficient", "compliant", "effective", "fussy", "perfectionist", "submissive",
                  "neurotic", "self-contained thinker"],
        LIBRA: ["loving", "balanced", "sociable", "relationship-oriented", "fair-minded", 
                  "gracious", "co-operative", "peace-loving", "indecisive", "gushing", 
                  "confrontational", "over-compromising", "diplomatic", "fair play", "charming",
                  "grace"],
        SCORPIO: ["resourceful", "intuitive", "insightful", "determined", "passionate", 
                    "private", "sensitive", "powerful", "jealous", "secretive", "unforgiving",
                    "overbearing", "powerful emotions", "intensity", "regeneration", "fighter"],
        SAGITTARIUS: ["οptimistic", "enthousiastic", "adventurous", "philosophical", 
                        "freedom-loving", "honest", "outgoing", "wise", "non-committal",
                        "blunt", "indiscriminate", "dogmatic"],
        CAPRICORN: ["patient", "organised", "serious", "conservative", "controlled",
                      "frugal", "ambitious", "strategic", "guarded", "ungenerous", "ruthless",
                      "calculating", "duty", "responsibility", "realistic", "careful"],
        AQUARIUS: ["society-oriented", "independent", "rational", "detached", "unconventional",
                     "humanitarian", "friendly", "idealistic", "eccentric", "distant",
                     "impersonal", "inflexible"],
        PISCES: ["sensitive", "compassionate", "receptive", "imaginative", "sympathetic",
                   "dreamy", "psychic", "passive", "sentimental", "unfocused", "neurotic",
                   "submissive"]
    }

    signs_ = [aries_, taurus_, gemini_, cancer_, leo_, virgo_, libra_, 
            scorpio_, sagittarius_, capricorn_, aquarius_, pisces_]

    def get(self, s):
        match(s):
            case "Aries" | "aries" : 
                sign = self.aries_
            case "Taurus" | "taurus" : 
                sign = self.taurus_
            case "Gemini" | "gemini" : 
                sign = self.gemini_
            case "Cancer" | "cancer" : 
                sign = self.cancer_
            case "Leo" | "leo" : 
                sign = self.leo_
            case "Virgo" | "virgo" : 
                sign = self.virgo_
            case "Libra" | "libra" : 
                sign = self.libra_
            case "Scorpio" | "scorpio" : 
                sign = self.scorpio_
            case "Sagittarius" | "sagittarius" : 
                sign = self.sagittarius_
            case "Capricorn" | "capricorn" : 
                sign = self.capricorn_
            case "Aquarius" | "aquarius" : 
                sign = self.aquarius_
            case "Pisces" | "pisces" : 
                sign = self.pisces_
            case _ :
                return -1
        return sign

    def get_polarity(self, p):
        match(p):
            case "Positive" | "positive" | "pos" | "p" | "+" :
                polarity = self.aries_.polarity_
            case "Negative" | "negative" | "neg" | "n" | "-" :
                polarity =  self.taurus_.polarity_
            case _ :
                return -1
        return polarity

    def get_mode(self, m):
        match(m):
            case "Cardinal" | "cardinal" :
                mode = self.aries_.mode_
            case "Fixed" | "fixed" :
                mode =  self.taurus_.mode_
            case "Mutable" | "mutable" :
                mode = self.gemini_.mode_
            case _ :
                return -1
        return mode

    def print(self, sign):
        Sign.print(sign)

    def print_keywords(self, sign_name):
        print("\nKeyword list for sign " + sign_name.upper() + ":\n")
        for k in Signs.keywords_[sign_name]:
            print("\t- " + k)

    def print_signs_in_polarity(self, p):
        polarity = self.get_polarity(self, p)
        if polarity == -1:
            print("Invalid polarity!")
            return
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity:
                list.append(s.name_)
        print("\n")
        print(polarity, "signs: ", list)
        print("\n")

    def print_signs_in_mode(self, m):
        mode = self.get_mode(self, m)
        if mode == -1:
            print("Invalid mode!")
            return
        list = []
        for s in self.signs_:
            if s.mode_ == mode:
                list.append(s.name_)
        print("\n")
        print(mode, "signs: ", list)
        print("\n")

    def print_signs_in_element(self, e):
        element = Elements.get(Elements, e)
        if element == -1:
            print("Invalid mode!")
            return
        list = []
        for s in self.signs_:
            if s.element_ == element.name_:
                list.append(s.name_)
        print("\n")
        print(element.name_, "signs : ", list)
        print("\n")

    def print_arc(self, sign):
        print("Degrees: [", sign.degrees_, ",", sign.degrees_ + 30, ")\n")

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

