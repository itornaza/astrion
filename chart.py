#
# chart
#

import csv
import os

from pangle import Ecliptic, Polar, to_polar, get_ecliptic
from planets import *
from angles import *
from houses import *
from lunar_nodes import *
from lunar_phases import *
from aspects import *
from signs import *

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

class Chart:

    DOCUMENTS = os.path.join(os.path.expanduser("~"), "Documents") + "/Astrion/charts/"

    ###########################################################################
    #                             INITIALIZATION                              #
    ###########################################################################

    def __init__(self, path: str = "", placidus: bool = True):
        """placidus: True for Placidus and False for Equal house systems"""
        self._input(placidus) if (path == "") else self._load(path, placidus)
        self._entities_in_houses()
        self._rulerships()

    def _input(self, placidus: bool):
        """Get the chart data from the user via the cli"""

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
                data.append(cusp.house_.name_, cusp.posit_.deg_, 
                            cusp.posit_.sign_.name_, cusp.posit_.min_)

        # Export chart data to custom file found in the 
        # ~/Documents/Astrion/charts' directory
        filename = input("Enter the file name (without extension): ")
        print("The file will be saved in: " + self.DOCUMENTS + ".csv")
        with open(self.DOCUMENTS + filename + '.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

    def _load(self, filename: str, placidus: bool):
        """Get the chart data data from a file specified from the user"""

        with open(self.DOCUMENTS + filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)
            assert len(lines) >= 14, "Chart data for equal houses not present in the file"

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

        if placidus:
            print("\n* PLACIDUS HOUSE CUSPS *")
        else:
            print("\n* EQUAL HOUSE CUSPS *")
        for house in self._all_houses():
            print("Cusp", house.house_.id_, ": ", end=" "); 
            house.posit_.print()
        print()

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

        print("* ENTITIES IN SIGNS & HOUSES *")
        for entity in self._all_entities():
            if isinstance(entity, ChartPlanet):
                print(entity.planet_.name_ + " in " + entity.posit_.sign_.name_ +
                      " in " + str(entity.house_.house_.id_))
            elif isinstance(entity, ChartAngle):
                print(entity.angle_.name_ + " in " + entity.posit_.sign_.name_ +
                      " in " + str(entity.house_.house_.id_))
            elif isinstance(entity, ChartLunarNode):
                print(entity.lunar_node_.name_ + " in " + entity.posit_.sign_.name_ + 
                      " in " + str(entity.house_.house_.id_))
        print()

    def _rulerships(self):
        """Finds and assigns to each planet the house or houses each of them rule"""
        for planet in self._all_planets_except_chiron():
            for house in self._all_houses():
                if planet.planet_.name_ == house.posit_.sign_.ruler_:
                    planet.ruled_houses_.append(house.house_.id_)
                elif planet.planet_.name_ in house.posit_.sign_.ruler_:
                    planet.ruled_houses_.append(house.house_.id_)

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

    ###########################################################################
    #                                   API                                   #
    ###########################################################################

    def get_aspects(self):
        entities = self._all_entities()
        print("* ASPECTS TABLE *\n")

        # For each entity compared to all other entities
        for value_a in entities:
            for value_b in entities:
                if value_a == value_b:
                    continue
                
                delta: Polar = to_polar(value_a.posit_.diff(value_b.posit_))
                aspect = Aspects.get_aspect_from_angle(delta.to_decimal())
                if aspect != None:

                    # Entity a
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
                    else:
                        print(aspect.name_, end=" ")

                    # Entity b
                    if isinstance(value_b, ChartPlanet): 
                        print(f"{value_b.planet_.name_}", end=" ")
                    elif isinstance(value_b, ChartAngle): 
                        print(f"{value_b.angle_.name_}", end=" ")
                    elif isinstance(value_b, ChartLunarNode): 
                        print(f"{value_b.lunar_node_.name_}", end=" ")
                        
                    # Aspect details
                    aspect_polar: Polar = Polar(aspect.angle_, 0)
                    orb = aspect_polar.diff(delta)

                    print(f"({orb.deg_:.0f}° {orb.min_:.0f}')", end=" ")
                    if orb <= Polar(1, 0):
                        print("\033[1mTight\033[0m")
                    else:
                        print() # Add the missing end line

                    # TODO: Add angular, rising and culminating tags!

            print() # Separate entities with a new line

    def get_polarity(self):
        print("* POLARITY *")

        # In Polarities we count the 7 traditional planets plus the ascendant and mc
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
        print("* ELEMENTS *")

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
        print("* MODES *")

        # In modes we count the 7 traditional planets plus the ascendant and mc
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
        print("* HEMISPHERES *")

        # In hemispheres we count all 10 planets plus Chiron
        entities = self._all_planets()
        
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
        assert len(southern_list) + len(northern_list) == 11

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
        assert len(eastern_list) + len(western_list) == 11        

    def get_triple_division(self):
        print("* TRIPLICITIES *")

        # In hemispheres we count all 10 planets plus Chiron
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
        print("* QUADRANTS *")

        # In Quadrants we count all 10 planets plus Chiron
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
        print("* LUNAR PHASE *")
        print(lunar_phase.name_ + ":", end=" ")
        delta.print()
        print()

    def get_dignities_debilities(self):
        print("* DIGNITIES & DEBILITIES *")
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
        print("/* RULERSHIPS */")
        for planet in self._all_planets_except_chiron():
            print(planet.planet_.name_, "rules:", end= " ")
            if planet.ruled_houses_ == []:
                print("None")
            else:
                for house_id in planet.ruled_houses_:
                    print(house_id, end = " ")
                print()
        print()

    def get_mutual_receptions(self):
        """Finds and reports all mutual receptions"""
        print("* MUTUAL RECEPTIONS *")
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

if __name__ == "__main__":
   
    # TODO: Before integrating get filename or direct imput from the user
    # Charts are placed by default in ~/Documents/Astrion/charts
    
    # Load a chart from file: True for Placidus, False for Equal
    chart = Chart("taylor.csv", False)
    
    # Load a chart manually and save it to file
    # chart = Chart(True)

    # Call all functions of the API
    chart.get_aspects()
    chart.get_polarity()
    chart.get_elements()
    chart.get_modes()
    chart.get_hemispheres()
    chart.get_triple_division()
    chart.get_quadrant_division()
    chart.get_lunar_phase()
    chart.get_dignities_debilities()
    chart.get_rulerships()
    chart.get_mutual_receptions()