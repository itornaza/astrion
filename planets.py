#
# planets
#

import re
from constants import *
from planet import Planet

class Planets:

    sun_ = Planet(SUN, NA, NA, NA, NA, NA, NA,LEO, "Sunday", ["Bright majestic yellow", "Orange"], ["Heart", "Spine", "Eyes"])
    moon_ = Planet(MOON, "365.25 days", "27.3 around Earth", "29.5 days", NA, NA, NA, CANCER, "Monday", ["Silver", "Off-white"], ["Stomach", "Breasts", "Lymphatic system", "Automatic nervous system", "Milk and body fluids (except from blood)"])
    mercury_ = Planet(MERCURY, "88 days", "58.65 days", "116 days", "176 days", "7˚ 0'", "28˚", [GEMINI, VIRGO], "Wednesday", "Multi-coloured", ["Nervous system", "Arms", "Hands"])
    venus_ = Planet(VENUS, "225 days", "243 days", "584 days", "118 days", "3˚ 24'", "48˚", [TAURUS, LIBRA], "Friday", "Green", ["Kidneys", "Throat"])
    mars_ = Planet(MARS, "687 days", "24h 37m", "780 days", NA, "1˚ 51'", NA, [ARIES, SCORPIO], "Tuesday", "Red", ["Immune system", "Blood", "Muscles", "Head", "Genitals", "Sexual functioning"])
    jupiter_ = Planet(JUPITER, "11.86 years", "9h 55m", "399 days", NA, "1˚ 18'", NA, [SAGITTARIUS, PISCES], "Thursday", ["Purple", "Royal blue"], ["Liver", "Thighs"])
    saturn_ = Planet(SATURN, "29.5 years", "10h 14m", "378 days", NA, "2˚ 29'", NA, [CAPRICORN, AQUARIUS], "Saturday", ["Black", "Brown", "Grey", "Bottle green"], ["Skeleton", "Bones", "Skin", "Teeth"])
    chiron_ = Planet(CHIRON, "50.7 years", "6h", NA, NA, NA, NA, NA, NA, NA, NA)
    uranus_ = Planet(URANUS, "84 years", "17h 14m", "370 days", NA, "0˚ 46'", NA, AQUARIUS, NA, "Turquoise blue", "Ankles")
    neptune_ = Planet(NEPTUNE, "164 years", "16h 7m", "368 days", NA, "1˚ 46'", NA, PISCES, NA, "Sea green", "Feet")
    pluto_ = Planet(PLUTO, "248 days", "6d 9h", "367 days", "153h", "17˚ 10'", NA, SCORPIO, NA, "Dark red", "Genitals")

    keywords_ = {
        SUN: [
            "power", "vitality", "self-expression", "selfhood (ego-self)", "identity", "purpose", "goal", "father", 
            "leadership and authority", "creative impulse","self awareness"
        ],
        
        MOON: [
            "safety and security", "instinctive responses", "the unconscious", "basic needs", "mother", "caretaking", 
            "food and feeding", "rhythms", "tides", "fluctuation", "emotions", "nurturing", "memories", "the past",
            "family", "instincts"
        ],
        
        MERCURY: [
            "communication",  "learning", "language", "writing", "the mind", "the trickster", "youth", "transport", 
            "connections", "siblings", "twins", "networking", "connecting", "thinking", "mental restlessness", 
            "mentality", "movement"
        ],

        VENUS: [
            "love", "relationship", "desire", "beauty", "peace", "harmony", "comparison", "art", "artistic expression", 
            "personal values", "worth","relating to others", "giving and receiving love", "self expression", 
            "appreciation"
        ],
        
        MARS: [
            "action", "daring", "courage", "drive", "will", "assertion or anger", "fighting and defending", 
            "sexuality", "desire", "survival", "sharpness"
        ],
        
        JUPITER: [
            "authority", "opportunity", "vision", "philosophy", "expansion", "inflation", "abundance", "philanthropy", 
            "adventure", "exploration", "enthusiasm", "trust", "faith", "search for meaning", "growth"
        ],
        
        SATURN: [
            "authority", "realism", "intention", "structure", "organisation", "method", "ambition", "experience", 
            "responsibility", "commitment", "formality", "convention", "tradition", "discipline", "limitations",
            "practicality", "control"
        ],
        
        CHIRON: [
            "vulnerability", "self-awareness", "unique talents", "maverick/outsider","integration", "contribution", 
            "process of maturing", "wounded healer", "teacher of wisdom"
        ],
        
        URANUS: [
            "innovation", "rebellion", "autonomy", "eccentricity", "independence", "alienation", "mechanisation", 
            "technology", "breakthrough", "revolution", "awakening", "insight", "extremes"
        ],
        
        NEPTUNE: [
            "the sea", "transcendence", "the sublime", "divine longing", "the intangible", "imagination", 
            "enchantment and seduction", "dreams", "illusion and glamour", "fantasy, magic and myth", 
            "yearning for perfection", "merging", "idealism and romance", "compassion", "intuition", "escapism"
        ],
        
        PLUTO: [
            "the underworld", "darkness", "cycle of death and re-birth", "sexual attraction", "transformation", 
            "catharsis", "survival", "strong determination", "power and control", "purging and elimination",
            "profound change", "intensity", "buried secrets"
        ]
    }
    
    planets_ = [sun_, moon_, mercury_, venus_, mars_, jupiter_, saturn_, 
                chiron_, uranus_, neptune_, pluto_]

    def get(self, p):
        sun = re.compile(r'sun', re.IGNORECASE)
        moon = re.compile(r'moo', re.IGNORECASE)
        mercury = re.compile(r'mer', re.IGNORECASE)
        venus = re.compile(r'ven', re.IGNORECASE)
        mars = re.compile(r'mar', re.IGNORECASE)
        jupiter = re.compile(r'jup', re.IGNORECASE)
        saturn = re.compile(r'sat', re.IGNORECASE)
        chiron = re.compile(r'chi', re.IGNORECASE)
        uranus = re.compile(r'ura', re.IGNORECASE)
        neptune = re.compile(r'nep', re.IGNORECASE)
        pluto = re.compile(r'plu', re.IGNORECASE)

        if sun.search(p) != None:
            planet = self.sun_
        elif moon.search(p) != None:
            planet = self.moon_
        elif mercury.search(p) != None:
            planet = self.mercury_
        elif venus.search(p) != None:
            planet = self.venus_
        elif mars.search(p) != None:
            planet = self.mars_
        elif jupiter.search(p) != None:
            planet = self.jupiter_
        elif saturn.search(p) != None:
            planet = self.saturn_
        elif chiron.search(p) != None:
            planet = self.chiron_
        elif uranus.search(p) != None:
            planet = self.uranus_
        elif neptune.search(p) != None:
            planet = self.neptune_
        elif pluto.search(p) != None:
            planet = self.pluto_
        else:
            return -1
        return planet

    def print(self, planet):
        Planet.print(planet)

    def print_keywords(self, planet_name):
        print("\nKeyword list for planet " + planet_name.upper() + ":\n")
        for k in Planets.keywords_[planet_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.planets_:
            Planet.print(p)