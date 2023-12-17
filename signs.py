#
# signs
#

import re
from constants import *
from sign import Sign
from elements import Elements
from polarities import Polarities
from modes import Modes
from aspects import Aspects

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

    def find_common_planet(self, sign_a, sign_b):
        planet = -1
        planet_a_is_list = False
        planet_b_is_list = False

        if isinstance(sign_a.planet_, list):
            planet_a_is_list = True
        if isinstance(sign_b.planet_, list):
            planet_b_is_list = True

        if (planet_a_is_list == True) and (planet_b_is_list == True):
            for i in range(0, 1):
                for j in range(0, 1):
                    if sign_a.planet_[i] == sign_b.planet_[j]:
                        planet = sign_a.planet_[i]
        elif (planet_a_is_list == True) and (planet_b_is_list == False):
            for i in range(0, 1):
                if sign_b.planet_ == sign_a.planet_[i]:
                    planet = sign_b.planet_
        elif (planet_a_is_list == False) and (planet_b_is_list == True):
            for i in range(0, 1):
                if sign_a.planet_ == sign_b.planet_[i]:
                    planet = sign_a.planet_
        else:
            if sign_a.planet_ == sign_b.planet_:
                planet = sign_a.planet_

        return planet

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
            if planet != -1:
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
        aspect = Aspects.get_aspect_from_aspect_angle(aspect_angle)
        if aspect != -1:
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
        if planet != -1:
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

    def print_all(self):
        for s in self.signs_:
            Sign.print(s)
            print("+--------------------------------------------------+")


