#
# planet
#

class Planet:
   
    def __init__(self, name, orbit, rotation, synodic, solar_day, inclination, 
                 elongation, ruler, detriment, exaltation, fall, day, color, 
                 body_part):
        self.name_ = name
        self.orbit_ = orbit
        self.rotation_ = rotation
        self.synodic_ = synodic
        self.solar_day_ = solar_day
        self.inclination_ = inclination
        self.elongation_ = elongation
        self.ruler_ = ruler
        self.detriment_ = detriment
        self.exaltated_ = exaltation
        self.fall_ = fall
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
              "\nRuler\t\t\t:\t", self.ruler_,
              "\nDetriment\t\t:\t", self.detriment_,
              "\nExalted\t\t\t:\t", self.exaltated_,
              "\nFall\t\t\t:\t", self.fall_,
              "\nDay\t\t\t:\t", self.day_,
              "\nColor\t\t\t:\t", self.color_,
              "\nBody part\t\t:\t", self.body_part_, "\n")
        