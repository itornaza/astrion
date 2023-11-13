#
# signs
#

from sign import Sign

class Signs:
    
    # Define all twelve signs using the Sign class
    aries_ = Sign("Aries", 1, 0, "+", "Fire", "Cardinal", 
                "Mars", "Head", "I am")
    
    taurus_ = Sign("Taurus", 2, 30, "-", "Earth", "Fixed", 
                 "Venus", "Neck and throat", "I possess")
    
    gemini_ = Sign("Gemini", 3, 60, "+", "Air", "Mutable", 
                 "Mercury", "Arms hands and lungs", "I think")
    
    cancer_ = Sign("Cancer", 4, 90, "-", "Water", "Cardinal", 
                 "Moon", "Breasts and stomach", "I feel")
    
    leo_ = Sign("Leo", 5, 120, "+", "Fire", "Fixed", 
                 "Sun", "Heart", "I will")
    
    virgo_ = Sign("Virgo", 6, 150, "-", "Earth", "Mutable", 
                 "Mercury", "Digestive system and bowel", "I analyze")
    
    libra_ = Sign("Libra", 7, 180, "+", "Air", "Cardinal", 
                 "Venus", "Kidneys", "I balance")
    
    scorpio_ = Sign("Scorpio", 8, 210, "-", "Water", "Fixed", 
                   "Mars and Pluto", "Reproductive organs", "I desire")
    
    sagittarius_ = Sign("Sagittarius", 9, 230, "+", "Fire", "Mutable", 
                      "Jupiter", "Hips and thighs", "I seek")
    
    capricorn_ = Sign("Capricorn", 10, 260, "-", "Earth", "Cardinal", 
                     "Saturn", "Knees", "I achieve")
    
    aquarius_ = Sign("Aquarius", 11, 290, "+", "Air", "Fixed", 
                    "Saturn and Uranus", "Shins and ankles", "I know")
    
    pisces_ = Sign("Pisces", 12, 330, "-", "Water", "Mutable", 
                  "Jupiter and Neptune", "Feet", "I believe")

    keywords_ = {
        "Aries": ["enthusiasm", "initiative", "drive", "action", "courageous", "energetic",
                  "sef-motivated", "decisive", "rash", "wilful", "selfish", "coarse", 
                  "locking horns", "battering ram", "zestful", "exuberant", "outgoing",
                  "work alone", "lead", "imppatient", "childlike behaviour", "spontaneous"],
        "Taurus": ["deliberate", "patient", "placid", "practical", "persistent", "grounded",
                   "acquisitive", "sensual", "stubborn", "unimaginative", "possessive", 
                   "self-indulgent", "simplistic", "comfort", "considered", 
                   "formidable temper", "red rug to a bull", "stability", "resistance to change"],
        "Gemini": ["versatile", "intellectual", "rational", "communicative", "sociable",
                   "adaptable", "diverse", "quick-witted", "flirtarious", "unpredictable",
                   "duplicitous", "shallow", "restless", "charming", "movement", "stimulation",
                   "emotional changeability"],
        "Cancer": ["emotional", "receptive", "tenacious", "caring", "sensitive", "nurturing",
                   "imaginative", "supportive", "moody", "smothering", "neurotic", "domineering",
                   "mothering", "creative", "assertive in a covert way", "empathy"],
        "Leo": ["grand", "playful", "loyal", "creative", "generous", "confident", "authoritative",
                "performer", "self-centered", "arrogant", "authoritarian", "attention-seeker"],
        "Virgo": ["discriminating", "analytical", "methodical", "practical", "fastidious",
                  "efficient", "compliant", "effective", "fussy", "perfectionist", "submissive",
                  "neurotic", "self-contained thinker"],
        "Libra": ["loving", "balanced", "sociable", "relationship-oriented", "fair-minded", 
                  "gracious", "co-operative", "peace-loving", "indecisive", "gushing", 
                  "confrontational", "over-compromising", "diplomatic", "fair play", "charming",
                  "grace"],
        "Scorpio": ["resourceful", "intuitive", "insightful", "determined" "passionate", 
                    "private", "sensitive", "powerful", "jealous", "secretive", "unforgiving",
                    "overbearing", "powerful emotions", "intensity", "regeneration", "fighter"],
        "Sagittarius": ["οptimistic", "enthousiastic", "adventurous", "philosophical", 
                        "freedom-loving", "honest", "outgoing", "wise", "non-committal",
                        "blunt", "indiscriminate", "dogmatic"],
        "Capricorn": ["patient", "organised", "serious", "conservative", "controlled",
                      "frugal", "ambitious", "strategic", "guarded", "ungenerous", "ruthless",
                      "calculating", "duty", "responsibility", "realistic", "careful"],
        "Aquarius": ["society-oriented", "independent", "rational", "detached", "unconventional",
                     "humanitarian", "friendly", "idealistic", "eccentric", "distant",
                     "impersonal", "inflexible"],
        "Pisces": ["sensitive", "compassionate", "receptive", "imaginative", "sympathetic",
                   "dreamy", "psychic", "passive", "sentimental", "unfocused", "neurotic",
                   "submissive"]
    }

    signs_ = [aries_, taurus_, gemini_, cancer_, leo_, virgo_, libra_, 
            scorpio_, sagittarius_, capricorn_, aquarius_, pisces_]

    def get(self, s):
        match(s):
            case "Aries" | "1" : 
                sign = self.aries_
            case "Taurus" | "2" : 
                sign = self.taurus_
            case "Gemini" | "3" : 
                sign = self.gemini_
            case "Cancer" | "4" : 
                sign = self.cancer_
            case "Leo" | "5" : 
                sign = self.leo_
            case "Virgo" | "6" : 
                sign = self.virgo_
            case "Libra" | "7" : 
                sign = self.libra_
            case "Scorpio" | "8" : 
                sign = self.scorpio_
            case "Sagittarius" | "9" : 
                sign = self.sagittarius_
            case "Capricorn" | "10" : 
                sign = self.capricorn_
            case "Aquarius" | "11" : 
                sign = self.aquarius_
            case "Pisces" | "12" : 
                sign = self.pisces_
            case _ :
                print("Invalid sign input!")
                return -1
        return sign

    def print_all(self):
        for s in self.signs_:
            Sign.print(s)

    # Wrapper for the Sign.print method
    def print(self, sign):
        Sign.print(sign)

    def print_keywords(self, sign_name):
        print("\nKeyword list for sign " + sign_name.upper() + ":\n")
        for k in Signs.keywords_[sign_name]:
            print("\t- " + k)

    # Print the signs that match the given mode
    def print_mode(self, mode):
        list = []
        for s in self.signs_:
            if s.mode_ == mode:
                list.append(s.name_)
        print(mode, ": ", list)

    # Print the signs that match the given polarity
    def print_polarity(self, polarity):
        list = []
        for s in self.signs_:
            if s.polarity_ == polarity:
                list.append(s.name_)
        print(polarity, ": ", list)

    # Print the signs that match the given element
    def print_element(self, element):
        list = []
        for s in self.signs_:
            if s.element_ == element:
                list.append(s.name_)
        print(element, ": ", list)

    def print_arc(self, sign):
        for s in self.signs_:
            if s.name_ == sign:
                print("[", s.degrees_, s.degrees_ + 30, ")")

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

