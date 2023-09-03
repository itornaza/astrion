#
# sign
#

# Sign class
class Sign:

    def __init__(self, sign, id, degrees, polarity ,element, mode, planet, body, moto):
        self.sign = sign
        self.id = id
        self.degrees = degrees
        self.polarity = polarity
        self.element = element
        self.mode = mode
        self.planet = planet
        self.body = body
        self.moto = moto

    # Print the details of a sign
    def print(self):
        print("|", self.sign, "|", self.id, "|", self.polarity, "|", self.element, 
              "|", self.mode, "|", self.planet, "|", self.body, "|", self.moto, "|")
