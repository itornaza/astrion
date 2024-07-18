from constants import *

class Keywords:

    planets_ = {
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

    signs_ = {
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
    
    houses_ = {
        FIRST: [
            "personal vitality", "birth", "self and self-development", "the body", "appearance", "gait or carriage", 
            "physical energy", "approach to life", "beginnings", "capacity and desire for self-development", 
            "early experiences", "personal identification", "outer appearances-approach"
        ],
        
        SECOND: [
            "personal resources", "personal finances", "possessions", "income", "money", "moveable property", "values",
            "material world", "our relationship to the physical world", "security", "worth", "desires", "tastes"
        ],
        
        THIRD: [
            "the early environment", "siblings", "neighbours", "school", "learning and language", "the mind", 
            "development of speech and language", "learning", "education (early schooling and school environment)", 
            "our immediate surroundings and neighbourhood", "short journeys", "communication", "facts", "environs"
        ],
        
        FOURTH: [
            "foundations and roots", "home", "family", "ancestry", "parents", "the past", "security", 
            "where one lives", "domestic life", "ancestry", "father", "personal history", 
            "place of safety and security", "private place of retreat", "endings and completion", "mines", 
            "lands/non-moveable property", "storage/protective space", "heritage", "inner base", "private life", 
            "foundations"
        ],
        
        FIFTH: [
            "creativity and joyful pursuits", "children", "pregnancy", "love affairs", "games", "sports", 
            "offspring/children", "creative projects", "procreation", "recreation", "games", "sports", "leisure", 
            "pastimes", "having fun", "love affairs", "things that affirm our creativity and joyfulness", 
            "what we play at", "gambling", "speculation", "pleasure", "romance", "self-expression"
        ],
        
        SIXTH: [
            "the routines of the physical world", "duty", "work", "health", "service", "attitude to work", 
            "bodily functions", "servants/practical caretakers", "daily functioning", "rituals", 
            "employment – earning our daily bread", "work colleagues", "employees", "those who serve us", "pets", 
            "everyday life", "craft"
        ],
        
        SEVENTH: [
            "Open relationships to the other", "marriage", "contractual relationships", "projections", "partnership", 
            "one-to-one relationships", "projection onto others","legal contracts", "litigation/law suits", 
            "open enemies", "attractions"
        ],

        EIGHT: [
            "hidden relationships to the other", "emotional bonds", "joint finances or money belonging to others", 
            "taxes", "loans", "debts", "death", "crisis", "death", "regeneration", "shared resources", "wills", 
            "legacies", "deeper level of relationship", "sexual partnership", "the occult and the hidden", 
            "fear and crisis", "primal patterns", "the mysterious", "inheritance", "sex"
        ],
        
        NINTH: [
            "exploration of unfamiliar territory", "higher learning", "religion", "philosophy", 
                  "travel and foreign countries", "further education", "philosophy", "religion", "law", "moral code", 
                  "travel", "long journeys", "exploration", "research", "foreign lands and people", "publishing", 
                  "quest for meaning", "beliefs", "teaching"
        ],
        
        TENTH: [
            "worldly position and responsibility", "job", "career", "public image", "authority figures", "parents", 
            "relationship to bosses", "public image and standing in the world", "rulers", "kings", "employers", 
            "ambitions", "aspirations", "honour", "prestige", "vocation", "status", "society", "wider world", "mother"
        ],
        
        ELEVENTH: [
            "relationship to groups and to the collective", "friendship", "hopes and wishes", "ideals and ideology", 
            "shared aims", "friends", "clubs", "groups", "social contacts", "organisations/committees", "social duties", 
            "political stance", "humanitarian enterprises", "hopes and wishes", "community", "projects", 
            "social reform", "allies"
        ],
        
        TWELVTH: [
            "the desire to retreat or escape", "institutions", "hospitals", "monasteries", "sorrow", "self-undoing", 
            "prisons", "asylums", "retreats/escapes", "places that are removed from the world", "hidden enemies", 
            "self-undoing", "mysticism", "secrets", "loss", "sacrifice", "martyrdom", "renunciation, surrender", 
            "dissolution", "the unconscious", "higher service"
        ]
    }

    aspects_ = {
        CONJUNCTION: [
            "...... and ...... are at one with each other",
            "...... automatically combines with ......",
            "There is a synthesis between ...... and ......",
            "The expression of ...... is obscured by ......",
            "It is impossible to ...... without also ......",
            "The individual cannot differentiate between ...... and ...... ",
            "There is a natural affinity between ...... and ......",
            "There is a concentrated focus of ...... and ......"
        ],

        OPPOSITION: [
            "An inner conflict between ...... and ......", 
            "Swinging between ...... and ......",
            "Feeling split between ...... and ......",
            "Unable to decide whether to ...... or ......",
            "The ability to develop a healthy balance between ...... and ...... ",
            "Learning to recognise both ...... and ......"
        ],

        TRINE: [
            "He/she is easy and comfortable when it comes to ......", 
            "He/she enjoys and finds pleasure in ......",
            "He/she adopts the line of least resistance by ......", 
            "He/she takes it for granted that ......"
        ],

        SQUARE: [
            "He/she struggles to actively and effectively integrate ......",
            "He/she is confronted by the need to ......",
            "He/she finds themselves challenged to ......",
            "He/she seems to be frustrated and blocked by ......",
            "It is a big challenge for him/her to ......",
            "He/she gets a great deal of personal satisfaction when he/she achieves ......"            
        ],

        SEXTILE: [
            "He/she is motivated to ......",
            "He/she can skilfully work towards ......",
            "He/she can ......",
            "He/she is able to combine ......"
        ],
        
        SEMISQUARE: [
            "He/she achieves productive and tangible results when he/she combines ......", 
            "He/she is determined to ......",
            "He/she finds it necessary to manifest ......",
            "He/she can produce ......",
            "He/she puts effort into ......",
            "He/she struggles or works hard to achieve ......"
        ],
        
        SESQUIQUADRATE: [
            "He/she achieves productive and tangible results when he/she combines ......", 
            "He/she is determined to ......",
            "He/she finds it necessary to manifest ......",
            "He/she can produce ......",
            "He/she puts effort into ......",
            "He/she struggles or works hard to achieve ......"
        ],
        
        SEMISEXTILE: [
            "He/she is constantly adjusting ......",
            "He/she feels uncomfortable with ......",
            "He/she is uneasy about ......",
            "He/she finds it difficult to see how ...... can work effectively together with ......",
            "He/she makes attempts to accommodate both ...... and ......"
        ],
        
        QUINCUNX: [
            "He/she is constantly adjusting ......",
            "He/she feels uncomfortable with ......",
            "He/she is uneasy about ......",
            "He/she finds it difficult to see how ...... can work effectively together with ......",
            "He/she makes attempts to accommodate both ...... and ......"
        ]
    }

    patterns_ = {
        # TODO
    }

    angles_ = {
        ASC: [
            "The place of the rising sun and our birth and entry into the world",
            "How we approach the world and how the world sees us",
            "Beginnings – our birth moment",
            "Our momentum into life",
            "Our approach to initiation and how we start things Our body and appearance",
            "Our identity and journey of self discovery",
            "Liminal space – the great threshold"
        ],

        DSC: [
            "The journey through relationships What relationship means to us",
            "The experience we meet in relationship", 
            "How we approach relationships Qualities we admire in others", 
            "Attractions and what is attractive to us",
            "Our projections"
        ],

        MC: [
            "The middle of the heavens",
            "Our vocation, our calling",
            "Our career and the work we do",
            "Our place in the world and what we have to offer the world – our journey into this", 
            "Our achievement and attainment in the world",
            "Ambition which drives our achievement",
            "Our relationship with authority and with power",
            "The parental axis – mother/father",
            "How the world sees us – and what we project onto the world"
        ],

        IC: [
            "The bottom of the sky",
            "Our roots and foundations - anchorage",
            "Our home and experience of belonging",
            "Family life, early experience of home, and security",
            "Parental axis – father/mother – parental roots",
            "The past",
            "Private space",
            "Inner life, inner world, place of reflection and being, of mystery Place of the soul and soul-making",
            "The end of the matter",
            "... and may be unconscious"
        ]
    }      

    polarities_ = {
        POSITIVE: ["outward-moving", "doing", "yang", "extravert", "assertive"],
        NEGATIVE: ["inward-moving", "being", "yin", "introvert", "self-reflective"],
    }

    modes_ = {
        CARDINAL: [
            "instigating", "initiating", "initiate and generate energy", "doing", "motion", "pioneering", 
            "start things up", "accept challenges", "goal oriented", "centrifugal radiating energy"
        ],

        FIXED: ["steadfast", "stable", "concentrate energy and sustain it", "consolidate", "put down roots", 
                "preservation and continuation", "stamina", "loyalty", "persistence", "perseverence", "constant", 
                "patience", "self-control", "endurance"
        ],
        
        MUTABLE: ["adaptable", "flexible", "disperse, distribute and transform energy", "state of flux", "restless", 
                  "changeable", "going with the flow", "changing direction", "resolve stalemates", "versatile", 
                  "restless"
        ]
    }

    elements_ = {
        FIRE: ["enthusiastic", "optimistic", "confident", "dramatic", "warm"],
        EARTH: ["practical", "sensible", "sensual", "realistic", "reliable", "down to earth"],
        AIR: ["civilised", "detaches", "objective", "impersonal", "rational", "verbal"],
        WATER: ["sympathetic", "receptive", "imaginative", "emotional", "intuitive"]
    }

