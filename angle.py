#
# angle
#

class Angle:

    def __init__(self, angle, full_name, direction):
        self.name_ = angle
        self.full_name_ = full_name
        self.direction_ = direction
        
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nFull name\t\t:\t", self.full_name_,
              "\nDirection\t\t:\t", self.direction_, "\n")

