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

    patterns_ = {
        T_SQUARE: ["Inner tension and drive for active integration and manifestation",
                   "The principle of the apex planet may seem to highlight the differences between the opposing "
                   "planets and to exacerbate the tension and conflicts between them",
                   "The apex may experienced as an obstacle which stands in the way of reconciliation and balance "
                   "between those planets in the opposition",
                   "The apex planet may be the unlikely mediator or catalyst between the opposing principles",
                   "Cardinal: demand to be actively integrated and resolved",
                   "Fixed: particularly difficult to integrate, tremendous internal pressure and capacity for "
                   "creativity", 
                   "Mutable: least resistant to integration, restless motion to move forward but difficulty in "
                   "following through"
        ],

        GRAND_CROSS: ["Describes a person that is driven and fiercely self-sufficient, who may have to learn the "
                      "hard way but who is also capable of remarkable achievements",
                      "A great deal of striving and effort to overcome challenges",
                      "By no means indicative of an easy life",
                      "May experience life as a great challenge",
                      "May see other people and the matterial world as obstacles to their progress"
        ],

        FINGER_OF_WORLD: ["The active challenge of the sesquiquadrates will tend to drive the individual to integrate "
                          "and resolve through the focal point",
                          "The inherent conflict of the square is further aggrevated by the more minor frictions and "
                          "obstacles indicated by both the sesquiquadrates",
                          "Although the subject may never feel close to achieving their aims, they are likely to "
                          "remain driven",
                          "The purpose of life may lie in the struggle itself rather than in the end result"
        ],

        HARD_RECTANGLE: ["As in the T-square, the conflicts and strengths of the oppositions are likely to be "
                         "intensified by the additional strain of the semisquares and sesquiquadrates"                 
        ],

        GRAND_TRINE: ["The emphasis on 3-ness indicates a high degree of harmony, enjoyment and contentment",
                      "Natural talent that enables a hugh degree of achievement with relative low effort",
                      "The person might become lazy or complacent",
                      "There is not Apex which resists the kind of action or dynamic instability present in "
                      "T-square or grand cross",
                      "Fire: The individual will have an innate and instinctive faith and optimism. Warmth and "
                      "generosity of spirit, center stage",
                      "Earth: The individual will be instinctively well grounded, capable and practical",
                      "Air: The individual will be able to draw on their natural ability to detach and assess "
                      "a situation, balancing and weighting up options, natural skills in communicating and "
                      "socializing",
                      "Water: The individual will have a deep reservoir of comfort and emotional support from "
                      "which to draw, natural reservoir of empathetic feeling, attuned to the emotional "
                      "undercurrents of a situation"
        ],

        MINOR_GRAND_TRINE: ["The principle of focal planet forming the sextiles, brings extra opportunity for "
                            "an active realization of the potential ease and enjoyment constrained with the "
                            "trine",
                            "It can represent significant creative impulse",
                            "The reservoir of natural skill and easy integration of the planets in trine can be "
                            "funneled through the apex, fueled by easy activeness of the sextile energy"
        ],

        KITE: ["Combines the ease, comfort and natural talent of the grand rine with the activity of the two "
               "sextiles and the dynamic tension of the opposition",
               "The apex planet forming the two sextiles will be in different element from the planets in the "
               "grand trine and provides an outlet for the expression of the potential shown by the overall "
               "configuration",
               "More effort may be exerted in the pursuit of rewards promised by the easy integration of "
               "planetary principles in the grand trine"
        ],

        YOD: ["The focal point stabilizes and drives this configuration",
              "It may be difficult at first to see how this can be done",
              "Fate may intervene in this respect throwing the person into situation where he must develop...",
              "The principle of the focal point is engaged in a struggle to become more whole by embracing "
              "the relatively alien principles of the other two planets",
              "The sextile aspect may indicate an opportunity for the above proposition to be accomplished "
              "with relatively less effort than might be usually be the case with the quincunx aspects",
              "Not until the apex planet is engaged with actively and continuously, and the irritations of "
              "the quincunxes faced, that the potential of the yod trully come alive",
              "A kind of fatedness is associated with yod"
        ],

        MYSTIC_RECTANGLE: ["The two trines and two sextiles enable the inner tensions of the oppositions to "
                           "be resolved",
                           "The individual has exceptional innate talents and gifts which demand to be "
                           "harvested and actively expressed in the world",
                           "There seems to be an element of responsibility. The individual is responsible "
                           "for using rather than ignoring their considerable gifts",
                           "The person will be good at finding creative solutions to difficult dilemmas",
                           "Their life may contain many paradoxes and situations which might on the surface "
                           "seem irreconciable, but there seems to be a facility for working creatively "
                           "with such situations"
        ],

        GRAND_SEXTILE: ["This very rear pattern indicates a markedly versatile character who with little "
                        "effort may be especially able to create or discover opportunities to utilise the "
                        "full range of their considerable resources",
        ],

        STELLIUM: ["Caution: 3 or more planets in the same sign and house in conjunction by association",
                   "The person will often be single minded, self-contained and self-driven"
        ]
    }

    lunar_phases_ = {
        NEW_MOON: ["Involved at the beginnings of things", 
                   "May meet many new situations",
                   "Impulsive and operating on instinct and spontaneity",
                   "Sowers of seeds",
                   "Enthusiastic", 
                   "Impulsive",
                   "Spontaneous",
                   "Subjective",
                   "Energy levels likely to fluctuate",
                   "Inner life may be more real than their external experiences",
                   "Perceive situations in symbolic terms making a network of ocnnections instinctively"
        ],
        
        CRESCENT: ["Searching for a dream",
                   "Breaking new ground",
                   "Working hard to gain a foothold yet their pioneering spirit is somehow dashed against "
                   "the rocks of destiny",
                   "Ahead of their time",
                   "Heighly motivated and succesful if they can persist in the face of resistance",
                   "May feel as if life is frequently two steps forward and one step back"
        ],
        
        FIRST_QUARTER: ["Builders or activists of one sort or another",
                        "Strong willed",
                        "Energetic",
                        "Have more than their fair share of challenges in life",
                        "Adventurous",
                        "Willing to explore new ground",
                        "Hold theirselves back through overreflection or inner uncertainties",
                        "Trine or No aspect type: Are willing to embrace new potentials but less forcefull "
                        "on the dissmantling of the old",
                        "Square or cuspal Sesquiquadrate type: Burning bridges behind them as they thrive "
                        "by tearing down the outmoded structures"
        ],
        
        GIBBOUS: ["Idealistic",
                  "Seeking for personal meaning",
                  "Are on a some quest to reach their current goal",
                  "Devote themselves to a cause",
                  "Seeking insight or understanding through pulling different threads together",
                  "May choose to work for a joint venture",
                  "May act as an inspiration to others as well",
                  "Tendency to perfectionism and self questioning",
                  "Aim height at tasks they have set themselves",
                  "If it is worth doing, it is worth doing well"
        ],
        
        FULL_MOON: ["Capacity for visionary thought",
                    "Taking the objective stance",
                    "Having a clear sense of themselves or a conscious sense of purpose",
                    "Vital importance of personal relationships",
                    "Relationships might be important in their lives or rejected altogether",
                    "Pattern of life experiences rising to a peak folowed by a crisis",
                    "Illumination or revelation through psychic insight for some",
                    "Know the joy of fullfilment, reconciliation and achievement or the pull or stalking opposing "
                    "circumstances especially for opposition types",
                    "Perceive ways to rise above difficulties",
                    "Move forward and transform themselves and possibly other people",
                    "The gift of seeking to find the next step beyond the present"
        ],
        
        DISSEMINATING: ["Teachers",
                        "Communicators",
                        "The crusadres of the lunation cycle",
                        "Passionate desire to share experiences that make impression on them",
                        "Want to demonstrate their acquired knowledge",
                        "Awareness of participating on a greater whole",
                        "Owned inspired visions",
                        "Sweep others along with them with the fire of their emotions",
                        "Uplifted by a cause, movement, religion or philosophy",
                        "Capacity to translate vision to action",
                        "Difficulties if emotional climate rises too fast or too height",
                        "Tempering of passion with dissernment is neccessary for lasting achievement",
                        "May become lost within their own cause or loose touch with personal responsibility "
                        "creating a sense of pwerlessness"
        ],
        
        LAST_QUARTER: ["Thoughtfull",
                       "Philosophical",
                       "Want to consolidate and actualize their ideologies",
                       "Important to conserve a personal or social principle that they fight to maintain if neccessary",
                       "Inflexible and defensive in the face of criticism",
                       "Can perceive a seed future arising from the ashes of the past",
                       "Pioneering spirit obehind future systems of thought or concrete manifestations that may "
                       "outlast them individually",
                       "Reformers attuned to the nature of progress setting up some lasting legacy",
                       "Ironic sense of humour"
        ],
        
        BALSAMIC: ["Need for space, quite and solitude",
                   "Capable of immense sacrifice surrendering even this need if occasion calls for it",
                   "Feeling like a melting pot in which something grester than themselves is being gestated",
                   "Creative inspiration",
                   "Prophetic vision",
                   "May simply feel confused, lost or overstretched",
                   "Desire to revolutionize and transform intensly felt sometimes to the extreme",
                   "Reaches out to the future and outgrows the past in a conscious manner",
                   "Bridge between past and future",
                   "Aware both of the endings inherent in the beginnings and the beginnings inherent in endings",
                   "Applying conjunction types: Feeling as if the past is sweeping them towards a new and better "
                   "future"
        ]
    }

    lunar_nodes_ = {
        NODAL_AXIS: ["TODO: Nodal axis"],
        NORTH_NODE: ["TODO: North node"],
        SOUTH_NODE: ["TODO: South node"]
    }
    