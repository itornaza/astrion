#
# planets
#

from planet import Planet

# Planets class
class Planets:

    # Define all planets
    sun_ = Planet("Sun")
    moon_ = Planet("Moon")
    mercury_ = Planet("Mercury")
    venus_ = Planet("Venus")
    mars_ = Planet("Mars")
    jupiter_ = Planet("Jupiter")
    saturn_ = Planet("Saturn")
    chiron_ = Planet("Chiron")
    uranus_ = Planet("uranus")
    neptune_ = Planet("Neptune")
    pluto_ = Planet("Pluto")

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
    
    def get(self, i):
        match(i):
            case "1" | "Sun" : 
                planet = self.sun_
            case "2" | "Moon" : 
                planet = self.moon_
            case "3" | "Mercury" : 
                planet = self.mercury_
            case "4" | "Venus" : 
                planet = self.venus_
            case "5" | "Mars" : 
                planet = self.mars_
            case "6" | "Jupiter" : 
                planet = self.jupiter_
            case "7" | "Saturn" : 
                planet = self.saturn_
            case "8" | "Chiron" : 
                planet = self.chiron_
            case "9" | "Uranus" : 
                planet = self.uranus_
            case "10" | "Neptune" : 
                planet = self.neptune_
            case "11" | "Pluto" : 
                planet = self.pluto_
            case _ :
                print()
        return planet

    def print(self, planet):
        Planet.print(planet)

    def print_keywords(self, planet_name):
        print("Keyword list for planet " + planet_name + ":")
        for k in Planets.keywords_[planet_name]:
            print("\t- " + k)
