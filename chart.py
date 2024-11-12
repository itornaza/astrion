#
# chart
#

import csv
import os
import sys

from angles import *
from aspects import *
from houses import *
from ephimeris_handler import *
from lunar_nodes import *
from lunar_phases import *
from pangle import Ecliptic, Polar, to_polar, get_ecliptic
from planets import *
from signs import *

# Global location that all charts are stored
CHARTS = os.path.join(os.path.expanduser("~"), "Documents") + "/astrion-data/charts/"
REPORTS = os.path.join(os.path.expanduser("~"), "Documents") + "/astrion-data/reports/"

class ChartPlanet:
    def __init__(self, planet: Planet, posit: Ecliptic):
        self.planet_: Planet = planet
        self.posit_: Ecliptic = posit 
        self.house_: ChartHouse # ChartHouse: that the planet is
        self.ruled_houses_ = [] # int: ids of houses the planet rules

    def __eq__(self, other):
        if isinstance(other, ChartPlanet):
            return self.planet_.name_ == other.planet_.name_
        return False

class ChartAngle:
    def __init__(self, angle: Angle, posit: Ecliptic):
        self.angle_: Angle = angle
        self.posit_: Ecliptic = posit
        self.house_: ChartHouse

    def __eq__(self, other):
        if isinstance(other, ChartAngle):
            return self.angle_.name_ == other.angle_.name_
        return False

class ChartLunarNode:
    def __init__(self, lunar_node: LunarNode, posit: Ecliptic):
        self.lunar_node_: LunarNode = lunar_node
        self.posit_: Ecliptic = posit
        self.house_: ChartHouse

    def __eq__(self, other):
        if isinstance(other, ChartLunarNode):
            return self.lunar_node_.name_ == other.lunar_node_.name_
        return False

class ChartHouse:
    def __init__(self, house: House, posit: Ecliptic):
        self.house_ = house
        self.posit_ = posit # This is the cusp position

    def __eq__(self, other):
        if isinstance(other, ChartHouse):
            return self.house_.id_ == other.house_.id_
        return False

class ChartAspects(Aspects):
    """Extends the Aspects class so the aspects_ member now includes
    a custom aspect as well that is define through a user lucky number"""
    def __init__(self):
        super().__init__()
        
        # Inquire if user wants a custom aspect based on a random number
        option = input("Custom aspect? (Y/n): ")
        if option != 'Y': 
            print("Boring! Anyway continuing with the usual aspects only...")
            self.custom_: Aspect = None
            return
        
        # Get lucky numbner and orb from the user
        while True:
            lucky_number = input("Lucky number? ")
            orb = input("Orb? ")
            try:
                lucky_number = float(lucky_number) 
                orb = int(orb)
                angle = 360.0 / lucky_number
                break
            except ValueError:
                print("Not a number! Please try again")
            except ZeroDivisionError:
                print("Lucky number cannot be zero")
        
        # Add the custom aspect to the existing aspects list
        self.custom_ = Aspect(CUSTOM, angle, NA, NA, orb, NA, NA)

class Chart:
    ###########################################################################
    #                             INITIALIZATION                              #
    ###########################################################################

    # TODO: Consider getting all the Client initialization here so we can 
    # improve the report with the Clients name etc. This will make it like 
    # a chart based compared to client based system.

    def __init__(self, path: str = "", placidus: bool = True):
        """placidus: True for Placidus and False for Equal house systems"""
        self.placidus = placidus

        # Get and branch on choice to select either _input, _load, _calc
        if path == "":
            self._input(self.placidus)
        elif path == "ephimeris":
            self._calc()
        else:
            self._load(path, self.placidus)
        
        # Calculate entities relationships 
        self.aspects = ChartAspects()
        self._entities_in_houses()
        self._rulerships()

    def _input(self, placidus: bool):
        """Get the chart data from the user via the cli"""

        # Get the Name of the client in case we want to save the file later
        client_id = Identity.set_identity(Identity)

        # User input for any house system
        eclipitc_format = " position in `dd sign mm`: "
        sun_posit: Ecliptic = get_ecliptic(Planets.sun_.name_ + eclipitc_format)
        moon_posit: Ecliptic = get_ecliptic(Planets.moon_.name_ + eclipitc_format)
        mercury_posit: Ecliptic= get_ecliptic(Planets.mercury_.name_ + eclipitc_format)
        venus_posit: Ecliptic = get_ecliptic(Planets.venus_.name_ + eclipitc_format)
        mars_posit: Ecliptic = get_ecliptic(Planets.mars_.name_ + eclipitc_format)
        jupiter_posit: Ecliptic = get_ecliptic(Planets.jupiter_.name_ + eclipitc_format)
        saturn_posit: Ecliptic = get_ecliptic(Planets.saturn_.name_ + eclipitc_format)
        uranus_posit: Ecliptic = get_ecliptic(Planets.uranus_.name_ + eclipitc_format)
        neptune_posit: Ecliptic = get_ecliptic(Planets.neptune_.name_ + eclipitc_format)
        pluto_posit: Ecliptic = get_ecliptic(Planets.pluto_.name_ + eclipitc_format)
        chiron_posit: Ecliptic = get_ecliptic(Planets.chiron_.name_ + eclipitc_format)
        asc_posit: Ecliptic = get_ecliptic(Angles.asc_.name_ + eclipitc_format)
        mc_posit: Ecliptic = get_ecliptic(Angles.mc_.name_ + eclipitc_format)
        north_node_posit: Ecliptic = get_ecliptic(LunarNodes.north_node_.name_ + eclipitc_format)

        # Extra steps for placidus
        if placidus:
            # Get the remaining cusps required for the user's house system
            second_posit: Ecliptic = get_ecliptic(Houses.second_.name_ + eclipitc_format)
            third_posit: Ecliptic = get_ecliptic(Houses.third_.name_ + eclipitc_format)
            fifth_posit: Ecliptic = get_ecliptic(Houses.fifth_.name_ + eclipitc_format)
            sixth_posit: Ecliptic = get_ecliptic(Houses.sixth_.name_ + eclipitc_format)

        # Member variable declarations
        self.sun_ = ChartPlanet(Planets.sun_, sun_posit)
        self.moon_ = ChartPlanet(Planets.moon_, moon_posit)
        self.mercury_ = ChartPlanet(Planets.mercury_, mercury_posit)
        self.venus_ = ChartPlanet(Planets.venus_, venus_posit)
        self.mars_ = ChartPlanet(Planets.mars_, mars_posit)
        self.jupiter_ = ChartPlanet(Planets.jupiter_, jupiter_posit)
        self.saturn_= ChartPlanet(Planets.saturn_, saturn_posit)
        self.uranus_ = ChartPlanet(Planets.uranus_, uranus_posit)
        self.neptune_ = ChartPlanet(Planets.neptune_, neptune_posit)
        self.pluto_ = ChartPlanet(Planets.pluto_, pluto_posit)
        self.chiron_ = ChartPlanet(Planets.chiron_, chiron_posit)
        self.asc_ = ChartAngle(Angles.asc_, asc_posit)
        self.mc_ = ChartAngle(Angles.mc_, mc_posit)
        self.north_node_ = ChartLunarNode(LunarNodes.north_node_, north_node_posit)

        # Extra steps for placidus
        if placidus:
            # Member variable declarations  for placidus cusps calculations
            self.second_ = ChartHouse(Houses.second_, second_posit)
            self.third_ = ChartHouse(Houses.third_, third_posit)
            self.fifth_ = ChartHouse(Houses.fifth_, fifth_posit)
            self.sixth_ = ChartHouse(Houses.sixth_, sixth_posit)

        # For any house system, calculate all other cusps
        self._calc_rest_chart(placidus)

        # Optionally, export chart data to custom file in default location
        self._export(client_id, placidus)

    def _load(self, filename: str, placidus: bool):
        """Get the chart data data from a file specified from the user"""
        with open(CHARTS + filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header row
            lines = list(reader)
            # TODO: Make the error user friendly and return control to user
            assert len(lines) >= 14, "Chart data for equal houses not present in the file"

            # TODO: Apply checks on the file data to report if the file is corrupted
            # or not in the correct format

            # Entities needed for all house systems
            self.sun_ = ChartPlanet(Planets.get(Planets, str(lines[0][0])), 
                    Ecliptic(int(lines[0][1]), Signs.get(Signs, lines[0][2]),
                    int(lines[0][3])))
            self.moon_ = ChartPlanet(Planets.get(Planets, str(lines[1][0])), 
                    Ecliptic(int(lines[1][1]), Signs.get(Signs, lines[1][2]),
                    int(lines[1][3])))
            self.mercury_ = ChartPlanet(Planets.get(Planets, str(lines[2][0])), 
                    Ecliptic(int(lines[2][1]), Signs.get(Signs, lines[2][2]),
                    int(lines[2][3])))
            self.venus_ = ChartPlanet(Planets.get(Planets, str(lines[3][0])), 
                    Ecliptic(int(lines[3][1]), Signs.get(Signs, lines[3][2]),
                    int(lines[3][3])))
            self.mars_ = ChartPlanet(Planets.get(Planets, str(lines[4][0])), 
                    Ecliptic(int(lines[4][1]), Signs.get(Signs, lines[4][2]),
                    int(lines[4][3])))
            self.jupiter_ = ChartPlanet(Planets.get(Planets, str(lines[5][0])), 
                    Ecliptic(int(lines[5][1]), Signs.get(Signs, lines[5][2]),
                    int(lines[5][3])))
            self.saturn_ =  ChartPlanet(Planets.get(Planets, str(lines[6][0])), 
                    Ecliptic(int(lines[6][1]), Signs.get(Signs, lines[6][2]),
                    int(lines[6][3])))
            self.uranus_ = ChartPlanet(Planets.get(Planets, str(lines[7][0])), 
                    Ecliptic(int(lines[7][1]), Signs.get(Signs, lines[7][2]),
                    int(lines[7][3])))
            self.neptune_ = ChartPlanet(Planets.get(Planets, str(lines[8][0])), 
                    Ecliptic(int(lines[8][1]), Signs.get(Signs, lines[8][2]),
                    int(lines[8][3])))
            self.pluto_ = ChartPlanet(Planets.get(Planets, str(lines[9][0])), 
                    Ecliptic(int(lines[9][1]), Signs.get(Signs, lines[9][2]),
                    int(lines[9][3])))
            self.chiron_ = ChartPlanet(Planets.get(Planets, str(lines[10][0])), 
                    Ecliptic(int(lines[10][1]), Signs.get(Signs, lines[10][2]),
                    int(lines[10][3])))
            self.asc_ = ChartAngle(Angles.get(Angles, str(lines[11][0])), 
                    Ecliptic(int(lines[11][1]), Signs.get(Signs, lines[11][2]),
                    int(lines[11][3])))
            self.mc_ = ChartAngle(Angles.get(Angles, str(lines[12][0])), 
                    Ecliptic(int(lines[12][1]), Signs.get(Signs, lines[12][2]),
                    int(lines[12][3])))
            self.north_node_ = ChartLunarNode(LunarNodes.get(LunarNodes, str(lines[13][0])), 
                    Ecliptic(int(lines[13][1]), Signs.get(Signs, lines[13][2]),
                    int(lines[13][3])))

            # Get the cusps required for the placidus calculations
            if placidus:
                # TODO: Make the error user friendly and return control to user
                assert len(lines) >= 18 , "Chart data for placidus are not present in the file" 
                self.second_ = ChartHouse(Houses.get(Houses, str(lines[14][0])), 
                    Ecliptic(int(lines[14][1]), Signs.get(Signs, lines[14][2]),
                    int(lines[14][3])))
                self.third_ = ChartHouse(Houses.get(Houses, str(lines[15][0])), 
                    Ecliptic(int(lines[15][1]), Signs.get(Signs, lines[15][2]),
                    int(lines[15][3])))
                self.fifth_ = ChartHouse(Houses.get(Houses, str(lines[16][0])), 
                    Ecliptic(int(lines[16][1]), Signs.get(Signs, lines[16][2]),
                    int(lines[16][3])))
                self.sixth_ = ChartHouse(Houses.get(Houses, str(lines[17][0])), 
                    Ecliptic(int(lines[17][1]), Signs.get(Signs, lines[17][2]),
                    int(lines[17][3])))

            # For any house system, calculate all other cusps
            self._calc_rest_chart(placidus)

    def _calc(self):
        # Note: cusp index is actual house number - 1
        eph = EphimerisHandler()

        # Set all planets except Chiron
        self.sun_ = ChartPlanet(Planets.sun_, eph.all_planets_except_chiron_.sun_)
        self.moon_ = ChartPlanet(Planets.moon_, eph.all_planets_except_chiron_.moon_)
        self.mercury_ = ChartPlanet(Planets.mercury_, eph.all_planets_except_chiron_.mercury_)
        self.venus_ = ChartPlanet(Planets.venus_, eph.all_planets_except_chiron_.venus_)
        self.mars_ = ChartPlanet(Planets.mars_, eph.all_planets_except_chiron_.mars_)
        self.saturn_ = ChartPlanet(Planets.saturn_, eph.all_planets_except_chiron_.jupiter_)
        self.jupiter_ = ChartPlanet(Planets.jupiter_, eph.all_planets_except_chiron_.saturn_)
        self.uranus_ = ChartPlanet(Planets.uranus_, eph.all_planets_except_chiron_.uranus_)
        self.neptune_ = ChartPlanet(Planets.neptune_, eph.all_planets_except_chiron_.neptune_)
        self.pluto_ = ChartPlanet(Planets.pluto_, eph.all_planets_except_chiron_.pluto_)
        
        # Set Chiron
        self.chiron_ = ChartPlanet(Planets.chiron_, eph.chiron_.chiron_)

        # Set the Houses
        self.first_ = ChartHouse(Houses.first_, eph.houses_and_nodes_.cusps_[0])
        self.second_ = ChartHouse(Houses.second_, eph.houses_and_nodes_.cusps_[1])
        self.third_ = ChartHouse(Houses.third_, eph.houses_and_nodes_.cusps_[2])
        self.fourth_ = ChartHouse(Houses.fourth_, eph.houses_and_nodes_.cusps_[3])
        self.fifth_ = ChartHouse(Houses.fifth_, eph.houses_and_nodes_.cusps_[4])
        self.sixth_ = ChartHouse(Houses.sixth_, eph.houses_and_nodes_.cusps_[5])
        self.seventh_ = ChartHouse(Houses.seventh_, eph.houses_and_nodes_.cusps_[6])
        self.eight_ = ChartHouse(Houses.eight_, eph.houses_and_nodes_.cusps_[7])
        self.ninth_ = ChartHouse(Houses.ninth_, eph.houses_and_nodes_.cusps_[8])
        self.tenth_ = ChartHouse(Houses.tenth_, eph.houses_and_nodes_.cusps_[9])
        self.eleventh_ = ChartHouse(Houses.eleventh_, eph.houses_and_nodes_.cusps_[10])
        self.twelvth_ = ChartHouse(Houses.twelvth_, eph.houses_and_nodes_.cusps_[11])

        # Set the Angles
        self.asc_ = ChartAngle(Angles.asc_, eph.houses_and_nodes_.cusps_[0])
        self.ic_ = ChartAngle(Angles.asc_, eph.houses_and_nodes_.cusps_[3])
        self.dsc_ = ChartAngle(Angles.asc_, eph.houses_and_nodes_.cusps_[6])
        self.mc_ = ChartAngle(Angles.asc_, eph.houses_and_nodes_.cusps_[9])

        # Set the Lunar Nodes
        self.north_node_ = ChartLunarNode(LunarNodes.north_node_, eph.houses_and_nodes_.nodes_[0])
        self.south_node_ = ChartLunarNode(LunarNodes.south_node_, eph.houses_and_nodes_.nodes_[1])

        # Optional Export with the patients name as filename, True for Placidus
        client_id = eph.client_.id_
        self._export(client_id, True) 

    def _calc_rest_chart(self, placidus: bool):
        """Given the basic chart data, calculates the rest of the house cusps
        and angles for the chart"""
        # Remember that Asc, MC, NN are given, so get the rest of the angles
        # and the South node
        self.south_node_ = ChartLunarNode(LunarNodes.south_node_, self.north_node_.posit_ + 180)
        self.dsc_ = ChartAngle(Angles.dsc_, self.asc_.posit_ + 180)
        self.ic_ = ChartAngle(Angles.ic_, self.mc_.posit_ - 180)

        if placidus:
            self.first_ = ChartHouse(Houses.first_, self.asc_.posit_)
            # 2 and 3 are already defined by the user
            self.fourth_ = ChartHouse(Houses.fourth_, self.ic_.posit_)
            # 5 and 6 are already defined by the user
            self.seventh_ = ChartHouse(Houses.seventh_, self.dsc_.posit_)
            self.eight_ = ChartHouse(Houses.eight_, self.second_.posit_ + 180)
            self.ninth_ = ChartHouse(Houses.ninth_, self.third_.posit_ + 180)
            self.tenth_ = ChartHouse(Houses.tenth_, self.mc_.posit_)
            self.eleventh_ = ChartHouse(Houses.eleventh_, self.fifth_.posit_ + 180)
            self.twelvth_ = ChartHouse(Houses.twelvth_, self.sixth_.posit_ + 180)
        else: 
            # Equal house system cusps
            self.first_ = ChartHouse(Houses.first_, self.asc_.posit_)
            self.second_ = ChartHouse(Houses.second_, self.first_.posit_ + 30)
            self.third_ = ChartHouse(Houses.third_, self.first_.posit_ + 60)
            self.fourth_ = ChartHouse(Houses.fourth_, self.first_.posit_ + 90)
            self.fifth_ = ChartHouse(Houses.fifth_, self.first_.posit_ + 120)
            self.sixth_ = ChartHouse(Houses.sixth_, self.first_.posit_ + 150)
            self.seventh_ = ChartHouse(Houses.seventh_, self.first_.posit_ + 180)
            self.eight_ = ChartHouse(Houses.eight_, self.first_.posit_ + 210)
            self.ninth_ = ChartHouse(Houses.ninth_, self.first_.posit_ + 240)
            self.tenth_ = ChartHouse(Houses.tenth_, self.first_.posit_ + 270)
            self.eleventh_ = ChartHouse(Houses.eleventh_, self.first_.posit_ + 300)
            self.twelvth_ = ChartHouse(Houses.twelvth_, self.first_.posit_ + 330)

    def _entities_in_houses(self):
        """Finds the houses that each of the entities is placed into"""
        for entity in self._all_entities():
            shift: Polar = self.first_.posit_
            if self.first_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.second_.posit_ - shift:
                entity.house_ = self.first_
            shift = self.second_.posit_
            if self.second_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.third_.posit_ - shift:
                entity.house_ = self.second_
            shift = self.third_.posit_
            if self.third_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.fourth_.posit_ - shift:
                entity.house_ = self.third_
            shift = self.fourth_.posit_
            if self.fourth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.fifth_.posit_ - shift:
                entity.house_ = self.fourth_
            shift = self.fifth_.posit_
            if self.fifth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.sixth_.posit_ - shift:
                entity.house_ = self.fifth_
            shift = self.sixth_.posit_
            if self.sixth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.seventh_.posit_ - shift:
                entity.house_ = self.sixth_
            shift = self.seventh_.posit_
            if self.seventh_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.eight_.posit_ - shift:
                entity.house_ = self.seventh_
            shift = self.eight_.posit_
            if self.eight_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.ninth_.posit_ - shift:
                entity.house_ = self.eight_
            shift = self.ninth_.posit_
            if self.ninth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.tenth_.posit_ - shift:
                entity.house_ = self.ninth_
            shift = self.tenth_.posit_
            if self.tenth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.eleventh_.posit_ - shift:
                entity.house_ = self.tenth_
            shift = self.eleventh_.posit_
            if self.eleventh_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.twelvth_.posit_ - shift:
                entity.house_ = self.eleventh_
            shift = self.twelvth_.posit_
            if self.twelvth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.first_.posit_ - shift:
                entity.house_ = self.twelvth_

    def _rulerships(self):
        """Finds and assigns to each planet the house or houses each of them rule"""
        for planet in self._all_planets_except_chiron():
            for house in self._all_houses():
                if planet.planet_.name_ == house.posit_.sign_.ruler_:
                    planet.ruled_houses_.append(house.house_.id_)
                elif planet.planet_.name_ in house.posit_.sign_.ruler_:
                    planet.ruled_houses_.append(house.house_.id_)

    ###########################################################################
    #                                   API                                   #
    ###########################################################################

    def get_filename():
        print("astrion-data at: " + CHARTS)
        filename = input("Enter a file without extension: ")
        filename = filename + '.csv'
        while not os.path.exists(CHARTS + filename):
            print("File " + "\"" + filename + "\"" + " does not exist.", end= " ")
            filename = input("Try again: ")
            filename = filename + '.csv'
        return filename

    def get_house_system():
        option = input("Placidus? (Y/n): ")
        return (True if option == 'Y' else  False)

    def get_chart_ruler(self):
        print("\n* \033[1;32mCHART RULER\033[0m *")
        print(self.asc_.posit_.sign_.ruler_)

    def get_house_cusps(self):
        if self.placidus:
            print("\n* \033[1;32mPLACIDUS HOUSE CUSPS\033[0m *")
        else:
            print("\n* \033[1;32mEQUAL HOUSE CUSPS\033[0m *")
        for house in self._all_houses():
            print("Cusp", house.house_.id_, ": ", end=" "); 
            house.posit_.print()
        print()        

    def get_entities_in_signs_and_houses(self):
        print("* \033[1;32mENTITIES IN SIGNS & HOUSES\033[0m *")
        for entity in self._all_entities():
            if isinstance(entity, ChartPlanet):
                print(entity.planet_.name_ + " in " + entity.posit_.sign_.name_ + 
                      " in " + str(entity.house_.house_.id_), end="   @")
                entity.posit_.print()
            elif isinstance(entity, ChartAngle):
                print(entity.angle_.name_ + " in " + entity.posit_.sign_.name_ +
                      " in " + str(entity.house_.house_.id_), end="   @")
                entity.posit_.print()
            elif isinstance(entity, ChartLunarNode):
                print(entity.lunar_node_.name_ + " in " + entity.posit_.sign_.name_ + 
                      " in " + str(entity.house_.house_.id_), end="   @")
                entity.posit_.print()
        print() # Each entry in a separate line

    # TODO: Get unique aspects on another function. Not dublicated as in here.
    # Check in get_mutual_receptions() for a similar implementation

    # TODO: Get rid of aspects between axis entities like NN-SS oppositions...
    def get_aspects(self):
        print("* \033[1;32mASPECTS TABLE\033[0m *")
        entities = self._all_entities()
        for value_a in entities:
            for value_b in entities:
                if value_a == value_b: 
                    continue
                delta: Polar = to_polar(value_a.posit_.diff(value_b.posit_))
                aspect = Aspects.get_aspect_from_angle(delta.to_decimal())

                # First check against the custom aspect cause it will override other
                # aspects in conflicting arcs
                if self.aspects.custom_ != None:
                    angle = delta.to_decimal()
                    if  angle <= self.aspects.custom_.angle_ + self.aspects.custom_.orb_ and \
                        angle >= self.aspects.custom_.angle_ - self.aspects.custom_.orb_:
                        aspect = self.aspects.custom_

                # Now check against the standard aspects
                if aspect != None:
                    # Entity A
                    if isinstance(value_a, ChartPlanet): 
                        print(f"{value_a.planet_.name_}", end=" ")
                    elif isinstance(value_a, ChartAngle): 
                        print(f"{value_a.angle_.name_}", end=" ")
                    elif isinstance(value_a, ChartLunarNode): 
                        print(f"{value_a.lunar_node_.name_}", end=" ")
                        
                    # Aspect
                    if aspect.name_ in [SQUARE, OPPOSITION, CONJUNCTION]:
                        print(f"\033[1m\033[31m{aspect.name_}\033[0m", end=" ")
                    elif aspect.name_ in [SEXTILE, TRINE]:
                        print(f"\033[1m\033[34m{aspect.name_}\033[0m", end=" ")
                    elif aspect.name_ == CUSTOM:
                        print(f"\033[1m\033[33m{aspect.name_}\033[0m", end=" ")
                    else:
                        print(aspect.name_, end=" ")

                    # Entity B
                    if isinstance(value_b, ChartPlanet): 
                        print(f"{value_b.planet_.name_}", end=" ")
                    elif isinstance(value_b, ChartAngle): 
                        print(f"{value_b.angle_.name_}", end=" ")
                    elif isinstance(value_b, ChartLunarNode): 
                        print(f"{value_b.lunar_node_.name_}", end=" ")
                        
                    # Orb
                    aspect_polar: Polar = Polar(aspect.angle_, 0)
                    orb = aspect_polar.diff(delta)
                    print(f"({orb.deg_:.0f}° {orb.min_:.0f}')", end=" ")
                    
                    # Tight
                    if orb <= Polar(1, 0):
                        print("\033[1mTight\033[0m", end=" ")
                    
                    # Angular, rising, culminating
                    if (isinstance(value_a, ChartAngle) and isinstance(value_b, ChartPlanet)) or \
                        (isinstance(value_a, ChartPlanet) and isinstance(value_b, ChartAngle)): 
                        if aspect.name_ == CONJUNCTION:
                            print("\033[1mAngular\033[0m", end=" ")
                            if isinstance(value_a, ChartAngle):
                                if value_a.angle_.name_ == MC:
                                    print("\033[1mCulminating\033[0m", end=" ")
                                elif value_a.angle_.name_ == ASC:
                                    print("\033[1mRising\033[0m", end=" ")
                            elif isinstance(value_b, ChartAngle):
                                if value_b.angle_.name_ == MC:
                                    print("\033[1mCulminating\033[0m", end=" ")
                                elif value_b.angle_.name_ == ASC:
                                    print("\033[1mRising\033[0m", end=" ")
                    print() # Add the missing end line
            print() # Separate combinations with a new line

    def get_polarity(self):
        entities = self._traditional_asc_mc()
        positive_list = []
        negative_list = []
        for entity in entities:
            # Positive
            if entity.posit_.sign_ in [Signs.aries_, Signs.leo_, Signs.sagittarius_, 
                                       Signs.gemini_, Signs.libra_, Signs.aquarius_]:
                if isinstance(entity, ChartPlanet): 
                    positive_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    positive_list.append(entity.angle_.name_)

            # Negative
            elif entity.posit_.sign_ in [Signs.taurus_, Signs.virgo_, Signs.capricorn_,
                                       Signs.cancer_, Signs.scorpio_, Signs.pisces_]:
                if isinstance(entity, ChartPlanet): 
                    negative_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    negative_list.append(entity.angle_.name_)

        print("* \033[1;32mPOLARITY\033[0m *")
        print("Positive: ", end=" ")
        for positive in positive_list:
            print(f"\033[1m\033[31m{positive}\033[0m", end = " ")
        print()
        print("Negative: ", end=" ")
        for negative in negative_list:
            print(f"\033[1m\033[34m{negative}\033[0m", end = " ")
        print()
        print(f"==> \033[1m\033[31mPositive = {len(positive_list)}\033[0m", end=" ")
        print(f"\033[1m\033[34mNegative = {len(negative_list)}\033[0m\n")  

        assert len(positive_list) + len(negative_list) == 9

    def get_elements(self):
        # In Elements we count the 7 traditional planets plus the ascendant and mc
        entities = self._traditional_asc_mc()
        fire_list= []
        earth_list = []
        air_list = []
        water_list = []
        for entity in entities:
            # Fire
            if entity.posit_.sign_ in [Signs.aries_, Signs.leo_, Signs.sagittarius_]:
                if isinstance(entity, ChartPlanet): 
                    fire_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    fire_list.append(entity.angle_.name_)
            
            # Earth
            elif entity.posit_.sign_ in [Signs.taurus_, Signs.virgo_, Signs.capricorn_]:
                if isinstance(entity, ChartPlanet): 
                    earth_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    earth_list.append(entity.angle_.name_)
            
            # Air
            elif entity.posit_.sign_ in [Signs.gemini_, Signs.libra_, Signs.aquarius_]:
                if isinstance(entity, ChartPlanet): 
                    air_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    air_list.append(entity.angle_.name_)
            
            # Water
            elif entity.posit_.sign_ in [Signs.cancer_, Signs.scorpio_, Signs.pisces_]:
                if isinstance(entity, ChartPlanet): 
                    water_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    water_list.append(entity.angle_.name_)

        print("* \033[1;32mELEMENTS\033[0m *")
        print("Fire: ", end=" ")
        for fire in fire_list:
            print(f"\033[1m\033[31m{fire}\033[0m", end = " ")
        print()
        print("Earth: ", end=" ")
        for earth in earth_list:
            print(f"\033[1m\033[33m{earth}\033[0m", end = " ")
        print()
        print("Air: ", end=" ")
        for air in air_list:
            print(f"\033[1m\033[36m{air}\033[0m", end = " ")
        print()
        print("Water: ", end=" ")
        for water in water_list:
            print(f"\033[1m\033[34m{water}\033[0m", end = " ")
        print()
        print(f"==> \033[1m\033[31mFire = {len(fire_list)}\033[0m", end=" ")
        print(f"\033[1m\033[33mEarth = {len(earth_list)}\033[0m", end=" ")
        print(f"\033[1m\033[36mAir = {len(air_list)}\033[0m", end=" ")
        print(f"\033[1m\033[34mWater = {len(water_list)}\033[0m\n")

        assert len(fire_list) + len(earth_list) + len(air_list) + len(water_list) == 9

    def get_modes(self):
        entities = self._traditional_asc_mc()
        cardinal_list = []
        fixed_list = []
        mutable_list = []
        for entity in entities:
            # Cardinals
            if entity.posit_.sign_ in [Signs.aries_, Signs.cancer_, Signs.libra_, Signs.capricorn_]:
                if isinstance(entity, ChartPlanet): 
                    cardinal_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    cardinal_list.append(entity.angle_.name_)
            
            # Fixed
            if entity.posit_.sign_ in [Signs.taurus_, Signs.leo_, Signs.scorpio_, Signs.aquarius_]:
                if isinstance(entity, ChartPlanet): 
                    fixed_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    fixed_list.append(entity.angle_.name_)
            
            # Mutable
            if entity.posit_.sign_ in [Signs.gemini_, Signs.virgo_, Signs.sagittarius_, Signs.pisces_]:
                if isinstance(entity, ChartPlanet): 
                    mutable_list.append(entity.planet_.name_)
                elif isinstance(entity, ChartAngle): 
                    mutable_list.append(entity.angle_.name_)

        print("* \033[1;32mMODES\033[0m *")
        print("Cardinal: ", end=" ")
        for cardinal in cardinal_list:
            print(f"\033[1m\033[31m{cardinal}\033[0m", end = " ")
        print()
        print("Fixed: ", end=" ")
        for fixed in fixed_list:
            print(f"\033[1m\033[33m{fixed}\033[0m", end = " ")
        print()
        print("Mutable: ", end=" ")
        for mutable in mutable_list:
            print(f"\033[1m\033[36m{mutable}\033[0m", end = " ")
        print()
        print(f"==> \033[1m\033[31mCardinal = {len(cardinal_list)}\033[0m", end=" ")
        print(f"\033[1m\033[33mFixed = {len(fixed_list)}\033[0m", end=" ")
        print(f"\033[1m\033[36mMutable = {len(mutable_list)}\033[0m\n")

        assert len(cardinal_list) + len(fixed_list) + len(mutable_list) == 9

    def get_hemispheres(self):
        entities = self._all_planets()
        print("* \033[1;32mHEMISPHERES\033[0m *")
        
        # North/South hemispheres division
        northern_list = []
        southern_list = []
        shift: Ecliptic = self.asc_.posit_
        for entity in entities:
            if self.first_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.seventh_.posit_ - shift:
                northern_list.append(entity.planet_.name_)
            else:
                southern_list.append(entity.planet_.name_)

        # East/West hemispheres division
        western_list = []
        eastern_list = []
        shift = self.fourth_.posit_
        for entity in entities:
            if self.fourth_.posit_ - shift <= entity.posit_ - shift \
                and entity.posit_ - shift < self.tenth_.posit_ - shift:
                
                western_list.append(entity.planet_.name_)
            else:
                eastern_list.append(entity.planet_.name_)

        print("Northern: ", end=" ")
        for planet in northern_list:
            print(f"\033[1m\033[31m{planet}\033[0m", end = " ")
        print()
        print("Southern: ", end=" ")
        for planet in southern_list:
            print(f"\033[1m\033[33m{planet}\033[0m", end= " ")
        print()
        print(f"==> \033[1m\033[31mNorthern = {len(northern_list)}\033[0m", end=" ")
        print(f"\033[1m\033[33mSouthern = {len(southern_list)}\033[0m\n")
        print("Eastern: ", end=" ")
        for planet in eastern_list:
            print(f"\033[1m\033[34m{planet}\033[0m", end= " ")
        print()
        print("Western: ", end=" ")
        for planet in western_list:
            print(f"\033[1m\033[36m{planet}\033[0m", end = " ")
        print()
        print(f"==> \033[1m\033[34mEastern = {len(eastern_list)}\033[0m", end=" ")
        print(f"\033[1m\033[36mWestern = {len(western_list)}\033[0m\n")
        
        assert len(southern_list) + len(northern_list) == 11
        assert len(eastern_list) + len(western_list) == 11        

    def get_triple_division(self):
        entities = self._all_planets()
        personal_list = []
        social_list = []
        universal_list = []
        for entity in entities:
            # Personal
            shift: Polar = self.asc_.posit_
            if self.first_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.fifth_.posit_ - shift:
                personal_list.append(entity.planet_.name_)
                continue
            
            # Social
            shift = self.fifth_.posit_
            if self.fifth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.ninth_.posit_ - shift:
                social_list.append(entity.planet_.name_)
                continue
            
            # Universal
            universal_list.append(entity.planet_.name_)
        
        print("* \033[1;32mTRIPLICITIES\033[0m *")
        print("Personal: ", end=" ")
        for personal in personal_list:
            print(f"\033[1m\033[31m{personal}\033[0m", end = " ")
        print()
        print("Social: ", end=" ")
        for social in social_list:
            print(f"\033[1m\033[33m{social}\033[0m", end = " ")
        print()
        print("Universal: ", end=" ")
        for universal in universal_list:
            print(f"\033[1m\033[36m{universal}\033[0m", end = " ")
        print()
        print(f"==> \033[1m\033[31mPersonal = {len(personal_list)}\033[0m", end=" ")
        print(f"\033[1m\033[33mSocial = {len(social_list)}\033[0m", end=" ")
        print(f"\033[1m\033[36mUniversal = {len(universal_list)}\033[0m\n")
        assert len(personal_list) + len(social_list) + len(universal_list) == 11
    
    def get_quadrant_division(self):
        entities = self._all_planets()
        development_list = []
        expression_list = []
        expansion_list = []
        transcendence_list = []
        for entity in entities:
            # Self development
            shift: Polar = self.asc_.posit_
            if self.first_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.fourth_.posit_ - shift:
                development_list.append(entity.planet_.name_)
                continue
            
            # Self expression
            shift = self.fourth_.posit_
            if self.fourth_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.seventh_.posit_ - shift:
                expression_list.append(entity.planet_.name_)
                continue
            
            # Self expansion
            shift = self.seventh_.posit_
            if self.seventh_.posit_ - shift <= entity.posit_ - shift and \
                entity.posit_ - shift < self.tenth_.posit_ - shift:
                expansion_list.append(entity.planet_.name_)
                continue

            # Self transcendence
            transcendence_list.append(entity.planet_.name_)

        print("* \033[1;32mQUADRANTS\033[0m *")
        print("Self development: ", end=" ")
        for development in development_list:
            print(f"\033[1m\033[31m{development}\033[0m", end = " ")
        print()
        print("Self expression: ", end=" ")
        for expression in expression_list:
            print(f"\033[1m\033[33m{expression}\033[0m", end = " ")
        print()
        print("Expansion: ", end=" ")
        for expansion in expansion_list:
            print(f"\033[1m\033[36m{expansion}\033[0m", end = " ")
        print()
        print("Transcendence: ", end=" ")
        for transcendence in transcendence_list:
            print(f"\033[1m\033[34m{transcendence}\033[0m", end = " ")
        print()
        print(f"==> \033[1m\033[31mSelf development = {len(development_list)}\033[0m", end=" ")
        print(f"\033[1m\033[33mSelf expression = {len(expression_list)}\033[0m", end=" ")
        print(f"\033[1m\033[36mSelf expansion = {len(expansion_list)}\033[0m", end= " ")
        print(f"\033[1m\033[34mSelf trsnscendence = {len(transcendence_list)}\033[0m\n")

        assert len(development_list) + len(expression_list) + \
            len(expansion_list) + len(transcendence_list) == 11

    def get_lunar_phase(self):
        delta: Polar = to_polar(self.moon_.posit_ - self.sun_.posit_)
        lunar_phase  = LunarPhases.get_from_angle(LunarPhases, delta.deg_)
        print("* \033[1;32mLUNAR PHASE\033[0m *")
        print(lunar_phase.name_ + ":", end=" ")
        delta.print()
        print()

    def get_dignities_debilities(self):
        print("* \033[1;32mDIGNITIES & DEBILITIES\033[0m *")
        for planet in self._all_planets():
            if planet.posit_.sign_.name_ in planet.planet_.ruler_:
                print(planet.planet_.name_, f"in \033[1m\033[36mrulership\033[0m")
            elif planet.posit_.sign_.name_ in planet.planet_.exaltated_:
                print(planet.planet_.name_, f"in \033[1m\033[36mexaltation\033[0m")
            elif planet.posit_.sign_.name_ in planet.planet_.detriment_:
                print(planet.planet_.name_, f"in \033[1m\033[31mdetriment\033[0m")
            elif planet.posit_.sign_.name_ in planet.planet_.fall_:
                print(planet.planet_.name_, f"in \033[1m\033[31mfall\033[0m")
        print()

    def get_rulerships(self):
        print("* \033[1;32mRULERSHIPS\033[0m *")
        for planet in self._all_planets_except_chiron():
            print(planet.planet_.name_, "rules:", end= " ")
            if planet.ruled_houses_ == []:
                print("None")
            else:
                for house_id in planet.ruled_houses_:
                    print(house_id, end = " ")
                print()
        print() # Each planet in a separate line

    def get_mutual_receptions(self):
        """Finds and reports all mutual receptions"""
        print("* \033[1;32mMUTUAL RECEPTIONS\033[0m *")
        mutual_receptions: bool = False
        unvisited_planets = self._all_planets_except_chiron()
        for planet in self._all_planets_except_chiron():
            # Only test planet with next ones in order to avoid duplicates
            unvisited_planets = unvisited_planets[1:]
            for other_house in planet.ruled_houses_:
                for other_planet in unvisited_planets:
                    if other_planet.house_.house_.id_ == other_house:
                        for other_planet_ruled_house in other_planet.ruled_houses_:
                            if other_planet_ruled_house == planet.house_.house_.id_:
                                mutual_receptions = True
                                print(planet.planet_.name_, "in", 
                                    planet.posit_.sign_.name_, "in", 
                                    planet.house_.house_.id_, "and", 
                                    other_planet.planet_.name_, "in", 
                                    other_planet.posit_.sign_.name_, "in", 
                                    other_planet.house_.house_.id_)
        if mutual_receptions == False:
            print("None")
        print()

    # TODO: Add a function to calculate all dispositor chains and check if
    # all of them end up in the same one
    def get_dispositors(self):
        # For all planets get the sign and then the ruler until self ruled?
        for planet in self._all_planets_except_chiron():
            print(planet.posit_.sign_.ruler_)

    def report(self):
        """Write all of the information we computed to a file"""
        with open(f"{REPORTS}/report.txt", "w") as report_txt: 
            stdout = sys.stdout
            sys.stdout = report_txt
            
            try:
                # 3.
                self.get_chart_ruler()
                # 4.
                self.get_house_cusps()
                # 5.
                self.get_entities_in_signs_and_houses()
                # 6.
                self.get_aspects()
                # 7.
                self.get_polarity()
                # 8.
                self.get_elements()
                # 9.
                self.get_modes()
                # 10.
                self.get_hemispheres()
                # 11.
                self.get_triple_division()
                # 12.
                self.get_quadrant_division()
                # 13.
                self.get_lunar_phase()
                # 14.
                self.get_dignities_debilities()
                # 15.
                self.get_rulerships()
                # 16.
                self.get_mutual_receptions()
            finally:
                sys.stdout = stdout
        
        self._clean_file(f"{REPORTS}/report.txt")

    ###########################################################################
    #                                HELPERS                                  #
    ###########################################################################

    def _all_houses(self):
        return [self.first_, self.second_, self.third_, self.fourth_, self.fifth_,
                self.sixth_, self.seventh_, self.eight_, self.ninth_, self.tenth_,
                self.eleventh_, self.twelvth_]

    def _traditional_asc_mc(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.asc_, self.mc_]

    def _all_planets(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_, self.chiron_]

    def _all_planets_except_chiron(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_]

    def _all_planets_asc_mc_nn(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_, self.chiron_, self.asc_, self.mc_, self.north_node_]
    
    def _all_entities(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_, self.chiron_, self.asc_, self.dsc_, self.mc_, self.ic_,
                self.north_node_, self.south_node_]
    
    # TODO: Generalize to use both from _input and _calc
    def _export(self, client_id: Identity, placidus: bool):
        """Optionally exports the csv file containing the planets and house cusps 
        positions"""
        option = input("Would you like to save the data? (Y/n): ")
        if option == 'Y':

            # Prepare data to export into the file
            entities = self._all_planets_asc_mc_nn()
            data = []
            for entity in entities:
                if isinstance(entity, ChartPlanet):
                    data.append([entity.planet_.name_, entity.posit_.deg_, 
                                entity.posit_.sign_.name_, entity.posit_.min_])
                elif isinstance(entity, ChartAngle):
                    data.append([entity.angle_.name_, entity.posit_.deg_, 
                                entity.posit_.sign_.name_, entity.posit_.min_])
                elif isinstance(entity, ChartLunarNode):
                    data.append([entity.lunar_node_.name_, entity.posit_.deg_, 
                             entity.posit_.sign_.name_, entity.posit_.min_])
                
            # Export the extra information needed for placidus
            if placidus:
                # Add the cusps to the data that will be added to the new file
                for cusp in [self.second_, self.third_, self.fifth_, self.sixth_]:
                    data.append([cusp.house_.name_, cusp.posit_.deg_, 
                                cusp.posit_.sign_.name_, cusp.posit_.min_])


            filename = client_id.name_ + "-" + client_id.lastname_
            header = ['Planet', 'Degrees', 'Sign', 'Minutes']
            with open(CHARTS + filename + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header) # Write the header first
                writer.writerows(data)
                print("Saved at: " + CHARTS + filename + ".csv")

    def _remove_ansi_escape_sequences(self, text):
        ansi_escape = re.compile(r'\033.*?m')
        return ansi_escape.sub('', text)

    def _clean_file(self, file_path):
        """Clean the content of a file by removing ANSI sequences"""
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            cleaned_content = self._remove_ansi_escape_sequences(content)
            with open(file_path, 'w') as file:
                file.write(cleaned_content)
        except Exception as e:
            print(f"Error: {e}")
