#
# house
#

# House class
class House:

    def __init__(self, house, id, sign_affinity, moto):
        self.house = house
        self.id = id
        self.sign_affinity = sign_affinity
        self.moto = moto

    # Print the details of a house
    def print(self):
        print("|", self.house, "|", self.id, "|", self.sign_affinity, "|", self.moto, "|")
