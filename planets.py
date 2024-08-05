#
# planets
#

import re
from constants import *
from keywords import Keywords
from planet import Planet

class Planets:

    sun_ = Planet(SUN, NA, NA, NA, NA, NA, NA, LEO, AQUARIUS, ARIES, LIBRA, "Sunday", ["Bright majestic yellow", "Orange"], ["Heart", "Spine", "Eyes"])
    moon_ = Planet(MOON, "365.25 days", "27.3 around Earth", "29.5 days", NA, NA, NA, CANCER, CAPRICORN, TAURUS, SCORPIO, "Monday", ["Silver", "Off-white"], ["Stomach", "Breasts", "Lymphatic system", "Automatic nervous system", "Milk and body fluids (except from blood)"])
    mercury_ = Planet(MERCURY, "88 days", "58.65 days", "116 days", "176 days", "7˚ 0'", "28˚", [GEMINI, VIRGO], [SAGITTARIUS, PISCES], NA, NA, "Wednesday", "Multi-coloured", ["Nervous system", "Arms", "Hands"])
    venus_ = Planet(VENUS, "225 days", "243 days", "584 days", "118 days", "3˚ 24'", "48˚", [TAURUS, LIBRA], [ARIES, SCORPIO], PISCES, VIRGO, "Friday", "Green", ["Kidneys", "Throat"])
    mars_ = Planet(MARS, "687 days", "24h 37m", "780 days", NA, "1˚ 51'", NA, [ARIES, SCORPIO], [TAURUS, LIBRA], CAPRICORN, CANCER, "Tuesday", "Red", ["Immune system", "Blood", "Muscles", "Head", "Genitals", "Sexual functioning"])
    jupiter_ = Planet(JUPITER, "11.86 years", "9h 55m", "399 days", NA, "1˚ 18'", NA, [SAGITTARIUS, PISCES], [GEMINI, VIRGO], CANCER, CAPRICORN, "Thursday", ["Purple", "Royal blue"], ["Liver", "Thighs"])
    saturn_ = Planet(SATURN, "29.5 years", "10h 14m", "378 days", NA, "2˚ 29'", NA, [CAPRICORN, AQUARIUS], [CANCER, LEO], LIBRA, ARIES, "Saturday", ["Black", "Brown", "Grey", "Bottle green"], ["Skeleton", "Bones", "Skin", "Teeth"])
    chiron_ = Planet(CHIRON, "50.7 years", "6h", NA,  NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
    uranus_ = Planet(URANUS, "84 years", "17h 14m", "370 days", NA, "0˚ 46'", NA, AQUARIUS,  NA, NA, NA, NA, "Turquoise blue", "Ankles")
    neptune_ = Planet(NEPTUNE, "164 years", "16h 7m", "368 days", NA, "1˚ 46'", NA, PISCES,  NA, NA, NA, NA, "Sea green", "Feet")
    pluto_ = Planet(PLUTO, "248 days", "6d 9h", "367 days", "153h", "17˚ 10'", NA, SCORPIO,  NA, NA, NA, NA, "Dark red", "Genitals")
    planets_ = [sun_, moon_, mercury_, venus_, mars_, jupiter_, saturn_, 
                chiron_, uranus_, neptune_, pluto_]

    def get(self, p):
        sun = re.compile(rf'^\s*{SUN}\s*$', re.IGNORECASE)
        moon = re.compile(rf'^\s*{MOON}\s*$', re.IGNORECASE)
        mercury = re.compile(rf'^\s*{MERCURY}\s*$', re.IGNORECASE)
        venus = re.compile(rf'^\s*{VENUS}\s*$', re.IGNORECASE)
        mars = re.compile(rf'^\s*{MARS}\s*$', re.IGNORECASE)
        jupiter = re.compile(rf'^\s*{JUPITER}\s*$', re.IGNORECASE)
        saturn = re.compile(rf'^\s*{SATURN}\s*$', re.IGNORECASE)
        chiron = re.compile(rf'^\s*{CHIRON}\s*$', re.IGNORECASE)
        uranus = re.compile(rf'^\s*{URANUS}\s*$', re.IGNORECASE)
        neptune = re.compile(rf'^\s*{NEPTUNE}\s*$', re.IGNORECASE)
        pluto = re.compile(rf'^\s*{PLUTO}\s*$', re.IGNORECASE)

        if sun.fullmatch(p):
            planet = self.sun_
        elif moon.fullmatch(p):
            planet = self.moon_
        elif mercury.fullmatch(p):
            planet = self.mercury_
        elif venus.fullmatch(p):
            planet = self.venus_
        elif mars.fullmatch(p):
            planet = self.mars_
        elif jupiter.fullmatch(p):
            planet = self.jupiter_
        elif saturn.fullmatch(p):
            planet = self.saturn_
        elif chiron.fullmatch(p):
            planet = self.chiron_
        elif uranus.fullmatch(p):
            planet = self.uranus_
        elif neptune.fullmatch(p):
            planet = self.neptune_
        elif pluto.fullmatch(p):
            planet = self.pluto_
        else:
            return None
        return planet

    def print(self, planet):
        Planet.print(planet)

    def print_keywords(self, planet_name):
        print("\nKeyword list for planet " + planet_name.upper() + ":\n")
        for k in Keywords.planets_[planet_name]:
            print("\t- " + k)

    # TODO: Implement
    def print_all(self):
        for p in self.planets_:
            Planet.print(p)