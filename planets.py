#
# planets
#

from planet import Planet
from constants import *

class Planets:

    sun_ = Planet(SUN, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A",LEO, "Sunday", ["Bright majestic yellow", "Orange"], ["Heart", "Spine", "Eyes"])
    moon_ = Planet(MOON, "365.25 days", "27.3 around Earth", "29.5 days", "N/A", "N/A", "N/A", CANCER, "Monday", ["Silver", "Off-white"], ["Stomach", "Breasts", "Lymphatic system", "Automatic nervous system", "Milk and body fluids (except from blood)"])
    mercury_ = Planet(MERCURY, "88 days", "58.65 days", "116 days", "176 days", "7˚ 0'", "28˚", [GEMINI, VIRGO], "Wednesday", "Multi-coloured", ["Nervous system", "Arms", "Hands"])
    venus_ = Planet(VENUS, "225 days", "243 days", "584 days", "118 days", "3˚ 24'", "48˚", [TAURUS, LIBRA], "Friday", "Green", ["Kidneys", "Throat"])
    mars_ = Planet(MARS, "687 days", "24h 37m", "780 days", "N/A", "1˚ 51'", "N/A", [ARIES, SCORPIO], "Tuesday", "Red", ["Immune system", "Blood", "Muscles", "Head", "Genitals", "Sexual functioning"])
    jupiter_ = Planet(JUPITER, "11.86 years", "9h 55m", "399 days", "N/A", "1˚ 18'", "N/A", [SAGITTARIUS, PISCES], "Thursday", ["Purple", "Royal blue"], ["Liver", "Thighs"])
    saturn_ = Planet(SATURN, "29.5 years", "10h 14m", "378 days", "N/A", "2˚ 29'", "N/A", [CAPRICORN, AQUARIUS], "Saturday", ["Black", "Brown", "Grey", "Bottle green"], ["Skeleton", "Bones", "Skin", "Teeth"])
    chiron_ = Planet(CHIRON, "50.7 years", "6h", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
    uranus_ = Planet(URANUS, "84 years", "17h 14m", "370 days", "N/A", "0˚ 46'", "N/A", AQUARIUS, "N/A", "Turquoise blue", "Ankles")
    neptune_ = Planet(NEPTUNE, "164 years", "16h 7m", "368 days", "N/A", "1˚ 46'", "N/A", PISCES, "N/A", "Sea green", "Feet")
    pluto_ = Planet(PLUTO, "248 days", "6d 9h", "367 days", "153h", "17˚ 10'", "N/A", SCORPIO, "N/A", "Dark red", "Genitals")

    keywords_ = {
        SUN: ["power", "vitality", "self-expression", "selfhood (ego-self)", "identity", 
                "purpose", "goal", "father", "leadership and authority", "creative impulse",
                "self awareness"],
        MOON: ["safety and security", "instinctive responses", "the unconscious", 
                 "basic needs", "mother", "caretaking", "food and feeding", "rhythms", 
                 "tides", "fluctuation", "emotions", "nurturing", "memories", "the past",
                 "family", "instincts"],
        MERCURY: ["communication",  "learning", "language", "writing", "the mind", 
                    "the trickster", "youth", "transport", "connections", "siblings", 
                    "twins", "networking", "connecting", "thinking", "mental restlessness", 
                    "mentality", "movement"],
        VENUS: ["love", "relationship", "desire", "beauty", "peace", "harmony", 
                  "comparison", "art", "artistic expression", "personal values", "worth",
                  "relating to others", "giving and receiving love", "self expression", 
                  "appreciation"],
        MARS: ["action", "daring", "courage", "drive", "will", "assertion or anger", 
                 "fighting and defending", "sexuality", "desire", "survival", "sharpness"],
        JUPITER: ["authority", "opportunity", "vision", "philosophy", "expansion", 
                    "inflation", "abundance", "philanthropy", "adventure", "exploration",
                    "enthusiasm", "trust", "faith", "search for meaning", "growth"],
        SATURN: ["authority", "realism", "intention", "structure", "organisation", 
                   "method", "ambition", "experience", "responsibility", "commitment", 
                   "formality", "convention", "tradition", "discipline", "limitations",
                   "practicality", "control"],
        CHIRON: ["vulnerability", "self-awareness", "unique talents", "maverick/outsider",
                   "integration", "contribution", "process of maturing", "wounded healer",
                   "teacher of wisdom"],
        URANUS: ["innovation", "rebellion", "autonomy", "eccentricity", "independence",
                   "alienation", "mechanisation", "technology", "breakthrough", "revolution",
                   "awakening", "insight", "extremes"],
        NEPTUNE: ["the sea", "transcendence", "the sublime", "divine longing", 
                    "the intangible", "imagination", "enchantment and seduction", "dreams",
                    "ollusion and glamour", "fantasy, magic and myth", 
                    "yearning for perfection", "merging", "idealism and romance", 
                    "compassion", "intuition", "escapism"],
        PLUTO: ["the underworld", "darkness", "cycle of death and re-birth", 
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
