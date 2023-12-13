#
# element
#

class Element:

    def __init__(self, element, plato, alchemy, humor, psychology, tarot, function, predominance):
        self.name_ = element
        self.plato_ = plato
        self.alchemy_ = alchemy
        self.humor_ = humor
        self.psychology_ = psychology
        self.tarot_ = tarot
        self.function_ = function
        self.predominance_ = predominance
        
    def print(self):
        print("\nName:\t\t", self.name_,
              "\nPlato:\t\t", self.plato_, 
              "\nAlchemy:\t", self.alchemy_, 
              "\nHumor:\t\t", self.humor_, 
              "\nPsychology:\t", self.psychology_, 
              "\nTarot:\t\t", self.tarot_,
              "\nFunction:\t", self.function_,
              "\nPredominance:\t", self.predominance_, "\n")

