#
# sign
#

# Sign class
class Sign:

    def __init__(self, sign, id, degrees, polarity ,element, mode, planet, body, moto):
        self.name_ = sign
        self.id_ = id
        self.degrees_ = degrees
        self.polarity_ = polarity
        self.element_ = element
        self.mode_ = mode
        self.planet_ = planet
        self.body_ = body
        self.moto_ = moto

    # Print the details of a sign
    def print(self):
        print("\nName:\t\t", self.name_, 
              "\nRank:\t\t", self.id_, 
              "\nPolarity:\t", self.polarity_, 
              "\nElement:\t", self.element_, 
              "\nMode:\t\t", self.mode_, 
              "\nPlanet:\t\t", self.planet_, 
              "\nBody part:\t", self.body_, 
              "\nMoto:\t\t", self.moto_, "\n")
