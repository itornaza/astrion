# 
# zodiac.py
#

from sign import Sign

# Zodiac class
class Zodiac():
    aries = Sign("Aries", 1, 0, "+", "Fire", "Cardinal", "Mars", "Head", "I am")
    taurus = Sign("Taurus", 2, 30, "-", "Earth", "Fixed", "Venus", "Neck and throat", "I possess")
    gemini = Sign("Gemini", 3, 60, "+", "Air", "Mutable", "Mercury", "Arms hands and lungs", "I think")
    cancer = Sign("Cancer", 4, 90, "-", "Water", "Cardinal", "Moon", "Breasts and stomach", "I feel")
    leo = Sign("Leo", 5, 120, "+", "Fire", "Fixed", "Sun", "Heart", "I will")
    virgo = Sign("Virgo", 6, 150, "-", "Earth", "Mutable", "Mercury", "Digestive system and bowel", "I analyze")
    libra = Sign("Libra", 7, 180, "+", "Air", "Cardinal", "Venus", "Kidneys", "I balance")
    scorpio = Sign("Scorpio", 8, 210, "-", "Water", "Fixed", "Mars and Pluto", "Reproductive organs", "I desire")
    sagitarius = Sign("Sagitarius", 9, 230, "+", "Fire", "Mutable", "Jupiter", "Hips and thighs", "I seek")
    capricorn = Sign("Capricorn", 10, 260, "-", "Earth", "Cardinal", "Saturn", "Knees", "I achieve")
    aquarius = Sign("Aquarius", 11, 290, "+", "Air", "Fixed", "Saturn and Uranus", "Shins and ankles", "I know")
    pisces = Sign("Pisces", 12, 330, "-", "Water", "Mutable", "Jupiter and Neptune", "Feet", "I believe")

    signs = [aries, taurus, gemini, cancer, leo, virgo, libra, 
             scorpio, sagitarius, capricorn, aquarius, pisces]
    
    def get_sign(self, s):
        match(s):
            case "Aries" : 
                sign = self.aries
            case "Taurus" : 
                sign = self.taurus
            case "Gemini" : 
                sign = self.gemini
            case "Cancer" : 
                sign = self.cancer
            case "Leo" : 
                sign = self.leo
            case "Virgo" : 
                sign = self.virgo
            case "Libra" : 
                sign = self.libra
            case "Scorpio" : 
                sign = self.scorpio
            case "Sagitarius" : 
                sign = self.sagitarius
            case "Capricorn" : 
                sign = self.capricorn
            case "Aquarius" : 
                sign = self.aquarius
            case "Pisces" : 
                sign = self.pisces
            case _ :
                print()
        return sign

    def print_all(self):
        for s in self.signs:
            Sign.print(s)

    # Print the signs that match the given mode
    def print_mode(self, mode):
        list = []
        for s in self.signs:
            if s.mode == mode:
                list.append(s.sign)
        print(mode, ": ", list)

    # Print the signs that match the given polarity
    def print_polarity(self, polarity):
        list = []
        for s in self.signs:
            if s.polarity == polarity:
                list.append(s.sign)
        print(polarity, ": ", list)

    # Print the signs that match the given element
    def print_element(self, element):
        list = []
        for s in self.signs:
            if s.element == element:
                list.append(s.sign)
        print(element, ": ", list)

    def print_arc(self, sign):
        for s in self.signs:
            if s.sign == sign:
                print("[", s.degrees, s.degrees + 30, ")")

    def print_polarity_element(self, polarity, element):
        list = []
        for s in self.signs:
            if s.polarity == polarity and s.element == element:
                list.append(s.sign)
        print(polarity, "/", element, ": ", list)

    def print_polarity_mode(self, polarity, mode):
        list = []
        for s in self.signs:
            if s.polarity == polarity and s.mode == mode:
                list.append(s.sign)
        print(polarity, "/", mode, ": ", list)

    def print_element_mode(self, element, mode):
        list = []
        for s in self.signs:
            if s.element == element and s.mode == mode:
                list.append(s.sign)
        print(element, "/", mode, ": ", list)

    def print_2_commons(self, sign):
        list = []
        for s in self.signs:
            if s.sign == sign.sign:
                pass
            elif s.element == sign.element and (s.mode == sign.mode or s.polarity == sign.polarity):
                list.append(s.sign)
        print(sign.sign, "has 2 in common with", list)
