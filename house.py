#
# house
#

class House:

    def __init__(self, house, id, sign_affinity, moto):
        self.name_ = house
        self.id_ = id
        self.sign_affinity_ = sign_affinity
        self.moto_ = moto

    def print(self):
        print("\nName:\t\t", self.name_, 
              "\nRank:\t\t", self.id_, 
              "\nSign:\t\t", self.sign_affinity_, 
              "\nMoto:\t\t", self.moto_, "\n")
