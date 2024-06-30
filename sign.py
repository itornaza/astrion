#
# sign
#

class Sign:

    def __init__(self, sign, id, degrees, polarity, element, mode, ruler, 
                 detriment, exalted, fall, body, moto):
        self.name_ = sign
        self.id_ = id
        self.degrees_ = degrees
        self.polarity_ = polarity
        self.element_ = element
        self.mode_ = mode
        self.ruler_ = ruler
        self.detriment_ = detriment
        self.exalted_ = exalted
        self.fall_ = fall
        self.body_ = body
        self.moto_ = moto

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nRank\t\t\t:\t", self.id_, 
              "\nStarts at\t\t:\t", self.degrees_, "degrees",
              "\nPolarity\t\t:\t", self.polarity_, 
              "\nElement\t\t\t:\t", self.element_, 
              "\nMode\t\t\t:\t", self.mode_, 
              "\nRuler\t\t\t:\t", self.ruler_,
              "\nDetriment\t\t:\t", self.detriment_,
              "\nExalted\t\t\t:\t", self.exalted_,
              "\nFall\t\t\t:\t", self.fall_, 
              "\nBody part\t\t:\t", self.body_, 
              "\nMoto\t\t\t:\t", self.moto_)
