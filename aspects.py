#
# aspects
#

from aspect import Aspect

# Aspects class
class Aspects:

    # Define all planets using the Planet class
    conjunction_ = Aspect("Conjunction", "0°", "1:1", 1, "8°", "Sign")
    
    opposition_ = Aspect("Opposition", "180°", "1:2", 2, "8°", "Polarity")

    trine_ = Aspect("Trine", "120°", "1:3", 3, "8°", "Element")

    square_ = Aspect("Square", "90°", "1:4", 2, "8°", "Mode")

    sextile_ = Aspect("Sextile", "60°", "1:6", [2, 3], "4°", ["Polarity", "Compatible element"])

    semisquare_ = Aspect("Semisquare", "45°", "1:8", 2, "2°", "N/A")

    sesquiquadrate_ = Aspect("Sesquiquadrate", "135°", "3:8", [2, 3], "2°", "N/A")

    semisextile_ = Aspect("Semisextile", "30°", "1:12", [2, 3], "2°", "Nothing")

    quincunx_ = Aspect("Quincunx", "150°", "5:12", [2, 3, 5], "2°", "Nothing")

    keywords_ = {
        "Conjunction": [
            "...... and ...... are at one with each other",
            "...... automatically combines with ......",
            "There is a synthesis between ...... and ......",
            "The expression of ...... is obscured by ......",
            "It is impossible to ...... without also ......",
            "The individual cannot differentiate between ...... and ...... ",
            "There is a natural affinity between ...... and ......",
            "There is a concentrated focus of ...... and ......"
        ],

        "Opposition": [
            "An inner conflict between ...... and ......", 
            "Swinging between ...... and ......",
            "Feeling split between ...... and ......",
            "Unable to decide whether to ...... or ......",
            "The ability to develop a healthy balance between ...... and ...... ",
            "Learning to recognise both ...... and ......"
        ],

        "Trine": [
            "He/she is easy and comfortable when it comes to ......", 
            "He/she enjoys and finds pleasure in ......",
            "He/she adopts the line of least resistance by ......", 
            "He/she takes it for granted that ......"
        ],

        "Square": [
            "He/she struggles to actively and effectively integrate ......",
            "He/she is confronted by the need to ......",
            "He/she finds themselves challenged to ......",
            "He/she seems to be frustrated and blocked by ......",
            "It is a big challenge for him/her to ......",
            "He/she gets a great deal of personal satisfaction when he/she achieves ......"            
        ],

        "Sextile": [
            "He/she is motivated to ......",
            "He/she can skilfully work towards ......",
            "He/she can ......",
            "He/she is able to combine ......"
        ],
        
        "Semisquare": [
            "He/she achieves productive and tangible results when he/she combines ......", 
            "He/she is determined to ......",
            "He/she finds it necessary to manifest ......",
            "He/she can produce ......",
            "He/she puts effort into ......",
            "He/she struggles or works hard to achieve ......"
        ],
        
        "Sesquiquadrate": [
            "He/she achieves productive and tangible results when he/she combines ......", 
            "He/she is determined to ......",
            "He/she finds it necessary to manifest ......",
            "He/she can produce ......",
            "He/she puts effort into ......",
            "He/she struggles or works hard to achieve ......"
        ],
        
        "Semisextile": [
            "He/she is constantly adjusting ......",
            "He/she feels uncomfortable with ......",
            "He/she is uneasy about ......",
            "He/she finds it difficult to see how ...... can work effectively together with ......",
            "He/she makes attempts to accommodate both ...... and ......"
        ],
        
        "Quincunx": [
            "He/she is constantly adjusting ......",
            "He/she feels uncomfortable with ......",
            "He/she is uneasy about ......",
            "He/she finds it difficult to see how ...... can work effectively together with ......",
            "He/she makes attempts to accommodate both ...... and ......"
        ]
    }
    
    planets_ = [conjunction_, opposition_, trine_, square_, sextile_, semisquare_, sesquiquadrate_,
                semisextile_, quincunx_]

    def get(self, i):
        match(i):
            case "1" | "Conjunction" : 
                aspect = self.conjunction_
            case "2" | "Opposition" : 
                aspect = self.opposition_
            case "3" | "Trine" : 
                aspect = self.trine_
            case "4" | "Square" : 
                aspect = self.square_
            case "5" | "Sextile" : 
                aspect = self.sextile_
            case "6" | "Semisquare" : 
                aspect = self.semisquare_
            case "7" | "Sesquiquadrate" : 
                aspect = self.sesquiquadrate_
            case "8" | "Semisextile" : 
                aspect = self.semisextile_
            case "9" | "Quincunx" : 
                aspect = self.quincunx_
            case _ :
                print("Invalid aspect input!")
                return -1
        return aspect

    def print(self, aspect):
        Aspect.print(aspect)

    def print_keywords(self, aspect_name):
        print("\nKeyword list for a " + aspect_name.upper() + " aspect:\n")
        for k in Aspects.keywords_[aspect_name]:
            print("\n\t- " + k)
