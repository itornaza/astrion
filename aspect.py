#
# aspect
#

class Aspect:
   
    def __init__(self, name, angle, fraction, root_numbers, orb, same):
        self.name_ = name
        self.angle_ = angle
        self.fraction_ = fraction
        self.root_numbers_ = root_numbers
        self.orb_ = orb
        self.same_ = same
    
    def print(self):
        print("\nName:\t\t", self.name_,
              "\nAngle:\t\t", self.angle_,
              "\nFraction:\t", self.fraction_,
              "\nRoot numbers:\t", self.root_numbers_,
              "\nOrb:\t\t", self.orb_,
              "\nSame:\t\t", self.same_, "\n")
        