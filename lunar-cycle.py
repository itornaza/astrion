#
# lunar-cycle
#

class LunarCycle:

    def __init__(self, name, phase, angle_ahead_of_sun, days_ahead_of_sun, aspects):
        self.name_ = name
        self.phase_ = phase
        self.angle_ahead_of_sun_ = angle_ahead_of_sun
        self.days_ahead_of_sun_ = days_ahead_of_sun
        self.aspects_ = aspects

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nPhase\t\t\t:\t", self.phase_, 
              "\nAngle ahead\t\t:\t", self.angle_ahead_of_sun_, 
              "\nDays ahead\t\t:\t", self.days_ahead_of_sun_, 
              "\nAspects\t\t\t:\t", self.name_, "\n")