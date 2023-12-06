#
# planets
#

from planet import Planet

# Planets class
class Planets:

    # Define all planets using the Planet class
    sun_ = Planet("Sun", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A",
                  "Leo", "Sunday", ["Bright majestic yellow", "Orange"], 
                  ["Heart", "Spine", "Eyes"])
    
    moon_ = Planet("Moon", "365.25 days", "27.3 around Earth", "29.5 days", "N/A", "N/A", "N/A",
                   "Cancer", "Monday", ["Silver", "Off-white"],
                    ["Stomach", "Breasts", "Lymphatic system", "Automatic nervous system",
                     "Milk and body fluids (except from blood)"])

    mercury_ = Planet("Mercury", "88 days", "58.65 days", "116 days", "176 days", "7˚ 0'", "28˚",
                      ["Gemini", "Virgo"], "Wednesday", "Multi-coloured", 
                      ["Nervous system", "Arms", "Hands"])
    
    venus_ = Planet("Venus", "225 days", "243 days", "584 days", "118 days", "3˚ 24'", "48˚", 
                    ["Taurus", "Libra"], "Friday", "Green", 
                    ["Kidneys", "Throat"])
    
    mars_ = Planet("Mars", "687 days", "24h 37m", "780 days", "N/A", "1˚ 51'", "N/A",
                   ["Aries", "Scorpio"], "Tuesday", "Red",
                   ["Immune system", "Blood", "Muscles", "Head", "Genitals", "Sexual functioning"])
    
    jupiter_ = Planet("Jupiter", "11.86 years", "9h 55m", "399 days", "N/A", "1˚ 18'", "N/A",
                      ["Sagittarius", "Pisces"], "Thursday", ["Purple", "Royal blue"],
                      ["Liver", "Thighs"])
    
    saturn_ = Planet("Saturn", "29.5 years", "10h 14m", "378 days", "N/A", "2˚ 29'", "N/A",
                     ["Capricorn", "Aquarius"], "Saturday", ["Black", "Brown", "Grey", "Bottle green"],
                     ["Skeleton", "Bones", "Skin", "Teeth"])
    
    chiron_ = Planet("Chiron", "50.7 years", "6h", "N/A", "N/A", "N/A", "N/A",
                     "N/A", "N/A", "N/A", "N/A")
    
    uranus_ = Planet("Uranus", "84 years", "17h 14m", "370 days", "N/A", "0˚ 46'", "N/A",
                     "Aquarius", "N/A", "Turquoise blue", "Ankles")
    
    neptune_ = Planet("Neptune", "164 years", "16h 7m", "368 days", "N/A", "1˚ 46'", "N/A",
                      "Pisces", "N/A", "Sea green", "Feet")
    
    pluto_ = Planet("Pluto", "248 days", "6d 9h", "367 days", "153h", "17˚ 10'", "N/A",
                    "Scorpio", "N/A", "Dark red", "Genitals")

    keywords_ = {
        "Sun": ["power", "vitality", "self-expression", "selfhood (ego-self)", "identity", 
                "purpose", "goal", "father", "leadership and authority", "creative impulse",
                "self awareness"],
        "Moon": ["safety and security", "instinctive responses", "the unconscious", 
                 "basic needs", "mother", "caretaking", "food and feeding", "rhythms", 
                 "tides", "fluctuation", "emotions", "nurturing", "memories", "the past",
                 "family", "instincts"],
        "Mercury": ["communication",  "learning", "language", "writing", "the mind", 
                    "the trickster", "youth", "transport", "connections", "siblings", 
                    "twins", "networking", "connecting", "thinking", "mental restlessness", 
                    "mentality", "movement"],
        "Venus": ["love", "relationship", "desire", "beauty", "peace", "harmony", 
                  "comparison", "art", "artistic expression", "personal values", "worth",
                  "relating to others", "giving and receiving love", "self expression", 
                  "appreciation"],
        "Mars": ["action", "daring", "courage", "drive", "will", "assertion or anger", 
                 "fighting and defending", "sexuality", "desire", "survival", "sharpness"],
        "Jupiter": ["authority", "opportunity", "vision", "philosophy", "expansion", 
                    "inflation", "abundance", "philanthropy", "adventure", "exploration",
                    "enthusiasm", "trust", "faith", "search for meaning", "growth"],
        "Saturn": ["authority", "realism", "intention", "structure", "organisation", 
                   "method", "ambition", "experience", "responsibility", "commitment", 
                   "formality", "convention", "tradition", "discipline", "limitations",
                   "practicality", "control"],
        "Chiron": ["vulnerability", "self-awareness", "unique talents", "maverick/outsider",
                   "integration", "contribution", "process of maturing", "wounded healer",
                   "teacher of wisdom"],
        "Uranus": ["innovation", "rebellion", "autonomy", "eccentricity", "independence",
                   "alienation", "mechanisation", "technology", "breakthrough", "revolution",
                   "awakening", "insight", "extremes"],
        "Neptune": ["the sea", "transcendence", "the sublime", "divine longing", 
                    "the intangible", "imagination", "enchantment and seduction", "dreams",
                    "ollusion and glamour", "fantasy, magic and myth", 
                    "yearning for perfection", "merging", "idealism and romance", 
                    "compassion", "intuition", "escapism"],
        "Pluto": ["the underworld", "darkness", "cycle of death and re-birth", 
                  "sexual attraction", "transformation", "catharsis", "survival", 
                  "strong determination", "power and control", "purging and elimination",
                  "profound change", "intensity", "buried secrets"]
    }
    
    planets_ = [sun_, moon_, mercury_, venus_, mars_, jupiter_, saturn_, chiron_, 
                uranus_, neptune_, pluto_]

    def get(self, i):
        match(i):
            case "Sun" | "sun" : 
                planet = self.sun_
            case "Moon" | "moon" : 
                planet = self.moon_
            case "Mercury" | "mercury" : 
                planet = self.mercury_
            case "Venus" | "venus" : 
                planet = self.venus_
            case "Mars" | "mars" : 
                planet = self.mars_
            case "Jupiter" | "jupiter" : 
                planet = self.jupiter_
            case "Saturn" | "saturn" : 
                planet = self.saturn_
            case "Chiron" | "chiron" : 
                planet = self.chiron_
            case "Uranus" | "uranus" : 
                planet = self.uranus_
            case "Neptune" | "neptune" : 
                planet = self.neptune_
            case "Pluto" | "pluto" : 
                planet = self.pluto_
            case _ :
                return -1
        return planet

    def print(self, planet):
        Planet.print(planet)

    def print_keywords(self, planet_name):
        print("\nKeyword list for planet " + planet_name.upper() + ":\n")
        for k in Planets.keywords_[planet_name]:
            print("\t- " + k)
