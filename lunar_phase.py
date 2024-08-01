#
# lunar_phase
#

class LunarPhase:

    def __init__(self, name, phase, arc_ahead_of_sun, days_ahead_of_sun, aspects):
        self.name_ = name
        self.phase_ = phase
        self.arc_ahead_of_sun_ = arc_ahead_of_sun # From-to angles ahead
        self.days_ahead_of_sun_ = days_ahead_of_sun # From-to days ahead
        self.aspects_ = aspects 

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), 
              "\nPhase\t\t\t:\t", self.phase_, 
              "\nArc ahead\t\t:\t", self.arc_ahead_of_sun_, 
              "\nDays ahead\t\t:\t", self.days_ahead_of_sun_, 
              "\nAspects\t\t\t:\t", self.aspects_, "\n")
        