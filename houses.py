#
# house
#

from house import House

class Houses:

    # Define all houses
    first_ = House("first", 1, "Aries", "I am")
    second_ = House("second", 2, "Taurus", "I possess")
    third_ = House("third", 3, "Gemini", "I think")
    forth_ = House("fourth", 4, "Cancer", "I belong")
    fifth_ = House("fifth", 5, "Leo", "I generate")
    sixth_ = House("sixth", 6, "Virgo", "I attend to")
    seventh_ = House("seventh", 7, "Libra", "I relate")
    eight_ = House("eight", 8, "Scorpio", "I deepen")
    ninth_ = House("ninth", 9, "Sagittarius", "I beleive")
    tenth_ = House("tenth", 10, "Capricorn", "I aspire")
    eleventh_ = House("eleventh", 11, "Aquarius", "I participate")
    twelvth_ = House("twelvth", 12, "Pisces", "I release")

    keywords_ = {
        "first": ["personal vitality", "birth", "self and self-development", "the body", 
                  "appearance", "gait or carriage", "physical energy", "approach to life", 
                  "beginnings", "capacity and desire for self-development", 
                  "early experiences", "personal identification", "outer appearances-approach"],
        "second": ["personal resources", "personal finances", "possessions", "income", "money", 
                   "moveable property", "values", "material world", 
                   "our relationship to the physical world", "security", "worth", "desires", "tastes"],
        "third": ["the early environment", "siblings", "neighbours", "school", "learning and language",
                  "the mind", "development of speech and language", "learning", 
                  "education (early schooling and school environment)", "our immediate surroundings and neighbourhood",
                  "short journeys", "communication", "facts", "environs"],
        "fourth": ["foundations and roots", "home", "family", "ancestry", "parents", "the past", 
                   "security", "where one lives", "domestic life", "ancestry", "father", 
                   "personal history", "place of safety and security", "private place of retreat", 
                   "endings and completion", "mines", "lands/non-moveable property", 
                   "storage/protective space", "heritage", "inner base", "private life", 
                   "foundations"],
        "fifth": ["creativity and joyful pursuits", "children", "pregnancy", "love affairs", "games", 
                  "sports", "offspring/children", "creative projects", "procreation", "recreation", 
                  "games", "sports", "leisure", "pastimes", "having fun", "love affairs", 
                  "things that affirm our creativity and joyfulness", "what we play at", 
                  "gambling", "speculation", "pleasure", "romance", "self-expression"],
        "sixth": ["the routines of the physical world", "duty", "work", "health", "service", 
                  "attitude to work", "bodily functions", "servants/practical caretakers", 
                  "daily functioning", "rituals", "employment – earning our daily bread", 
                  "work colleagues", "employees", "those who serve us", "pets", "everyday life", 
                  "craft"],
        "seventh": ["Open relationships to the other", "marriage", "contractual relationships", 
                    "projections", "partnership", "one-to-one relationships", "projection onto others",
                    "legal contracts", "litigation/law suits", "open enemies", "attractions"],
        "eight": ["hidden relationships to the other", "emotional bonds", 
                  "joint finances or money belonging to others", "taxes", "loans", "debts", "death", 
                  "crisis", "death", "regeneration", "shared resources", "wills", "legacies", 
                  "deeper level of relationship", "sexual partnership", "the occult and the hidden", 
                  "fear and crisis", "primal patterns", "the mysterious", "inheritance", "sex"],
        "ninth": ["exploration of unfamiliar territory", "higher learning", "religion", "philosophy", 
                  "travel and foreign countries", "further education", "philosophy", "religion", "law", 
                  "moral code", "travel", "long journeys", "exploration", "research", 
                  "foreign lands and people", "publishing", "quest for meaning", "beliefs", "teaching"],
        "tenth": ["worldly position and responsibility", "job", "career", "public image", 
                  "authority figures", "parents", "relationship to bosses", 
                  "public image and standing in the world", "rulers", "kings", "employers", "ambitions", 
                  "aspirations", "honour", "prestige", "vocation", "status", "society", "wider world", 
                  "mother"],
        "eleventh": ["relationship to groups and to the collective", "friendship", "hopes and wishes", 
                     "ideals and ideology", "shared aims", "friends", "clubs", "groups", 
                     "social contacts", "organisations/committees", "social duties", "political stance", 
                     "humanitarian enterprises", "hopes and wishes", "community", "projects", 
                     "social reform", "allies"],
        "twelvth": ["the desire to retreat or escape", "institutions", "hospitals", "monasteries", 
                    "sorrow", "self-undoing", "prisons", "asylums", "retreats/escapes", 
                    "places that are removed from the world", "hidden enemies", "self-undoing", 
                    "mysticism", "secrets", "loss", "sacrifice", "martyrdom", "renunciation, surrender", 
                    "dissolution", "the unconscious", "higher service"]
    }

    def get(self, i):
        match(i):
            case "1" | "first" : 
                house = self.first_
            case "2" | "second" : 
                house = self.second_
            case "3" | "third" : 
                house = self.third_
            case "4" | "fourth" : 
                house = self.forth_
            case "5" | "fifth" : 
                house = self.fifth_
            case "6" | "sixth" : 
                house = self.sixth_
            case "7" | "seventh" : 
                house = self.seventh_
            case "8" | "eigth" : 
                house = self.eight_
            case "9" | "ninth" : 
                house = self.ninth_
            case "10" | "tenth" : 
                house = self.tenth_
            case "11" | "eleventh" : 
                house = self.eleventh_
            case "12" | "twelvth" : 
                house = self.twelvth_
            case _ :
                print("Invalid house input!")
                return -1
        return house
    
    def print(self, house):
        House.print(house)

    def print_keywords(self, house_name):
        print("\nKeyword list for the " + house_name + " house:")
        for k in Houses.keywords_[house_name]:
            print("\t- " + k)
