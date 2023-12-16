#
# element
#

class Element:

    def __init__(self, element, plato, alchemy, humor, psychology, tarot, 
                 function, predominance):
        self.name_ = element
        self.plato_ = plato
        self.alchemy_ = alchemy
        self.humor_ = humor
        self.psychology_ = psychology
        self.tarot_ = tarot
        self.function_ = function
        self.predominance_ = predominance
        
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(),
              "\nPlato\t\t\t:\t", self.plato_, 
              "\nAlchemy\t\t\t:\t", self.alchemy_, 
              "\nHumor\t\t\t:\t", self.humor_, 
              "\nPsychology\t\t:\t", self.psychology_, 
              "\nTarot\t\t\t:\t", self.tarot_,
              "\nFunction\t\t:\t", self.function_,
              "\nPredominance\t\t:\t", self.predominance_)
