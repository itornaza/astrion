#
# house
#

# Planet class
class Planet:

    keywords = {
        "sun": ["power", "vitality", "self-expression", "selfhood (ego-self)", "identity", 
                "purpose", "goal", "father", "leadership and authority", "creative impulse",
                "self awareness"],
        "moon": ["safety and security", "instinctive responses", "the unconscious", 
                 "basic needs", "mother", "caretaking", "food and feeding", "rhythms", 
                 "tides", "fluctuation", "emotions", "nurturing", "memories", "the past",
                 "family", "instincts"],
        "mercury": ["communication",  "learning", "language", "writing", "the mind", 
                    "the trickster", "youth", "transport", "connections", "siblings", 
                    "twins", "networking", "connecting", "thinking", "mental restlessness", 
                    "mentality", "movement"],
        "venus": ["love", "relationship", "desire", "beauty", "peace", "harmony", 
                  "comparison", "art", "artistic expression", "personal values", "worth",
                  "relating to others", "giving and receiving love", "self expression", 
                  "appreciation"],
        "mars": ["action", "daring", "courage", "drive", "will", "assertion or anger", 
                 "fighting and defending", "sexuality", "desire", "survival", "sharpness"],
        "jupiter": ["authority", "opportunity", "vision", "philosophy", "expansion", 
                    "inflation", "abundance", "philanthropy", "adventure", "exploration",
                    "enthusiasm", "trust", "faith", "search for meaning", "growth"],
        "saturn": ["authority", "realism", "intention", "structure", "organisation", 
                   "method", "ambition", "experience", "responsibility", "commitment", 
                   "formality", "convention", "tradition", "discipline", "limitations",
                   "practicality", "control"],
        "chiron": ["vulnerability", "self-awareness", "unique talents", "maverick/outsider",
                   "integration", "contribution", "process of maturing", "wounded healer",
                   "teacher of wisdom"],
        "uranus": ["innovation", "rebellion", "autonomy", "eccentricity", "independence",
                   "alienation", "mechanisation", "technology", "breakthrough", "revolution",
                   "awakening", "insight", "extremes"],
        "neptune": ["the sea", "transcendence", "the sublime", "divine longing", 
                    "the intangible", "imagination", "enchantment and seduction", "dreams",
                    "ollusion and glamour", "fantasy, magic and myth", 
                    "yearning for perfection", "merging", "idealism and romance", 
                    "compassion", "intuition", "escapism"],
        "pluto": ["the underworld", "darkness", "cycle of death and re-birth", 
                  "sexual attraction", "transformation", "catharsis", "survival", 
                  "strong determination", "power and control", "purging and elimination",
                  "profound change", "intensity", "buried secrets"]
    }
    
    def print_keywords(self, planet):
        print("Keyword list for planet " + planet + ":")
        print(Planet.keywords[planet])

### test Planet class
Planet.print_keywords(Planet, "pluto")
pass