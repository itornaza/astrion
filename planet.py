#
# planet
#

class Planet:
   
    def __init__(self, name, orbit, rotation, synodic, solar_day, inclination, 
                 elongation, sign_ruler, day, color, body_part):
        self.name_ = name
        self.orbit_ = orbit
        self.rotation_ = rotation
        self.synodic_ = synodic
        self.solar_day_ = solar_day
        self.inclination_ = inclination
        self.elongation_ = elongation
        self.sign_ruler_ = sign_ruler
        self.day_ = day
        self.color_ = color
        self.body_part_ = body_part
    
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(),
              "\nOrbit\t\t\t:\t", self.orbit_,
              "\nRotation\t\t:\t", self.rotation_,
              "\nSynodic\t\t\t:\t", self.synodic_,
              "\nSolar day\t\t:\t", self.solar_day_,
              "\nInclination\t\t:\t", self.inclination_,
              "\nMax elongation\t\t:\t", self.elongation_,
              "\nSign ruler\t\t:\t", self.sign_ruler_,
              "\nDay\t\t\t:\t", self.day_,
              "\nColor\t\t\t:\t", self.color_,
              "\nBody part\t\t:\t", self.body_part_, "\n")
        