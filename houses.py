#
# house
#

from house import House
from constants import *

class Houses:

    first_ = House(FIRST, 1, ARIES, "I am")
    second_ = House(SECOND, 2, TAURUS, "I possess")
    third_ = House(THIRD, 3, GEMINI, "I think")
    forth_ = House(FOURTH, 4, CANCER, "I belong")
    fifth_ = House(FIFTH, 5, LEO, "I generate")
    sixth_ = House(SIXTH, 6, VIRGO, "I attend to")
    seventh_ = House(SEVENTH, 7, LIBRA, "I relate")
    eight_ = House(EIGHT, 8, SCORPIO, "I deepen")
    ninth_ = House(NINTH, 9, SAGITTARIUS, "I beleive")
    tenth_ = House(TENTH, 10, CAPRICORN, "I aspire")
    eleventh_ = House(ELEVENTH, 11, AQUARIUS, "I participate")
    twelvth_ = House(TWELVTH, 12, PISCES, "I release")

    keywords_ = {
        FIRST: ["personal vitality", "birth", "self and self-development", "the body", 
                  "appearance", "gait or carriage", "physical energy", "approach to life", 
                  "beginnings", "capacity and desire for self-development", 
                  "early experiences", "personal identification", "outer appearances-approach"],
        SECOND: ["personal resources", "personal finances", "possessions", "income", "money", 
                   "moveable property", "values", "material world", 
                   "our relationship to the physical world", "security", "worth", "desires", "tastes"],
        THIRD: ["the early environment", "siblings", "neighbours", "school", "learning and language",
                  "the mind", "development of speech and language", "learning", 
                  "education (early schooling and school environment)", "our immediate surroundings and neighbourhood",
                  "short journeys", "communication", "facts", "environs"],
        FOURTH: ["foundations and roots", "home", "family", "ancestry", "parents", "the past", 
                   "security", "where one lives", "domestic life", "ancestry", "father", 
                   "personal history", "place of safety and security", "private place of retreat", 
                   "endings and completion", "mines", "lands/non-moveable property", 
                   "storage/protective space", "heritage", "inner base", "private life", 
                   "foundations"],
        FIFTH: ["creativity and joyful pursuits", "children", "pregnancy", "love affairs", "games", 
                  "sports", "offspring/children", "creative projects", "procreation", "recreation", 
                  "games", "sports", "leisure", "pastimes", "having fun", "love affairs", 
                  "things that affirm our creativity and joyfulness", "what we play at", 
                  "gambling", "speculation", "pleasure", "romance", "self-expression"],
        SIXTH: ["the routines of the physical world", "duty", "work", "health", "service", 
                  "attitude to work", "bodily functions", "servants/practical caretakers", 
                  "daily functioning", "rituals", "employment – earning our daily bread", 
                  "work colleagues", "employees", "those who serve us", "pets", "everyday life", 
                  "craft"],
        SEVENTH: ["Open relationships to the other", "marriage", "contractual relationships", 
                    "projections", "partnership", "one-to-one relationships", "projection onto others",
                    "legal contracts", "litigation/law suits", "open enemies", "attractions"],
        EIGHT: ["hidden relationships to the other", "emotional bonds", 
                  "joint finances or money belonging to others", "taxes", "loans", "debts", "death", 
                  "crisis", "death", "regeneration", "shared resources", "wills", "legacies", 
                  "deeper level of relationship", "sexual partnership", "the occult and the hidden", 
                  "fear and crisis", "primal patterns", "the mysterious", "inheritance", "sex"],
        NINTH: ["exploration of unfamiliar territory", "higher learning", "religion", "philosophy", 
                  "travel and foreign countries", "further education", "philosophy", "religion", "law", 
                  "moral code", "travel", "long journeys", "exploration", "research", 
                  "foreign lands and people", "publishing", "quest for meaning", "beliefs", "teaching"],
        TENTH: ["worldly position and responsibility", "job", "career", "public image", 
                  "authority figures", "parents", "relationship to bosses", 
                  "public image and standing in the world", "rulers", "kings", "employers", "ambitions", 
                  "aspirations", "honour", "prestige", "vocation", "status", "society", "wider world", 
                  "mother"],
        ELEVENTH: ["relationship to groups and to the collective", "friendship", "hopes and wishes", 
                     "ideals and ideology", "shared aims", "friends", "clubs", "groups", 
                     "social contacts", "organisations/committees", "social duties", "political stance", 
                     "humanitarian enterprises", "hopes and wishes", "community", "projects", 
                     "social reform", "allies"],
        TWELVTH: ["the desire to retreat or escape", "institutions", "hospitals", "monasteries", 
                    "sorrow", "self-undoing", "prisons", "asylums", "retreats/escapes", 
                    "places that are removed from the world", "hidden enemies", "self-undoing", 
                    "mysticism", "secrets", "loss", "sacrifice", "martyrdom", "renunciation, surrender", 
                    "dissolution", "the unconscious", "higher service"]
    }

    def get(self, i):
        match(i):
            case "1" | "First" | "first" : 
                house = self.first_
            case "2" | "Second" | "second" : 
                house = self.second_
            case "3" | "Third" | "third" : 
                house = self.third_
            case "4" | "Fourth" | "fourth" : 
                house = self.forth_
            case "5" | "Fifth" | "fifth" : 
                house = self.fifth_
            case "6" | "Sixth" | "sixth" : 
                house = self.sixth_
            case "7" | "Seventh" | "seventh" : 
                house = self.seventh_
            case "8" | "Eigth" | "eigth" : 
                house = self.eight_
            case "9" | "Ninth" | "ninth" : 
                house = self.ninth_
            case "10" | "Tenth" | "tenth" : 
                house = self.tenth_
            case "11" | "Eleventh" | "eleventh" : 
                house = self.eleventh_
            case "12" | "Twelvth" | "twelvth" : 
                house = self.twelvth_
            case _ :
                return -1
        return house
    
    def print(self, house):
        House.print(house)

    def print_keywords(self, house_name):
        print("\nKeyword list for the " + house_name.upper() + " house:\n")
        for k in Houses.keywords_[house_name]:
            print("\t- " + k)
