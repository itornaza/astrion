#
# chart
#

import csv

from pangle import Ecliptic, Polar, get_ecliptic, to_polar, to_ecliptic
from planets import *
from angles import *
from houses import *
from lunar_nodes import *
from aspects import *
from signs import * # Used for testing data

class ChartPlanet:
    
    def __init__(self, planet: Planet, posit: Ecliptic):
        self.planet_ = planet
        self.posit_ = posit

    def __eq__(self, other):
        if isinstance(other, ChartPlanet):
            return self.planet_.name_ == other.planet_.name_
        return False

class ChartAngle:
    
    def __init__(self, angle: Angle, posit: Ecliptic):
        self.angle_ = angle
        self.posit_ = posit

    def __eq__(self, other):
        if isinstance(other, ChartAngle):
            return self.angle_.name_ == other.angle_.name_
        return False

class ChartLunarNode:

    def __init__(self, lunar_node: LunarNode, posit: Ecliptic):
        self.lunar_node_ = lunar_node
        self.posit_ = posit

    def __eq__(self, other):
        if isinstance(other, ChartLunarNode):
            return self.lunar_node_.name_ == other.lunar_node_.name_
        return False

class ChartHouse:
    
    def __init__(self, house: House, posit: Ecliptic):
        self.house_ = house
        self.posit_ = posit # This is the cusp position

class Chart:

    # All planets + Asc + MC + NN
    def __init__(self, sun_posit: Ecliptic, moon_posit: Ecliptic, mercury_posit: Ecliptic, 
                 venus_posit: Ecliptic, mars_posit: Ecliptic, jupiter_posit: Ecliptic, 
                 saturn_posit: Ecliptic, uranus_posit: Ecliptic, neptune_posit: Ecliptic, 
                 pluto_posit: Ecliptic, chiron_posit: Ecliptic, 
                 asc_posit: Ecliptic, mc_posit: Ecliptic, north_node_posit: Ecliptic):
        
        self.sun_ = ChartPlanet(Planets.sun_, sun_posit)
        self.moon_ = ChartPlanet(Planets.moon_, moon_posit)
        self.mercury_ = ChartPlanet(Planets.mercury_, mercury_posit)
        self.venus_ = ChartPlanet(Planets.venus_, venus_posit)
        self.mars_ = ChartPlanet(Planets.mars_, mars_posit)
        self.jupiter_ = ChartPlanet(Planets.jupiter_, jupiter_posit)
        self.saturn_ = ChartPlanet(Planets.saturn_, saturn_posit)
        self.uranus_ = ChartPlanet(Planets.uranus_, uranus_posit)
        self.neptune_ = ChartPlanet(Planets.neptune_, neptune_posit)
        self.pluto_ = ChartPlanet(Planets.pluto_, pluto_posit)
        self.chiron_ = ChartPlanet(Planets.chiron_, chiron_posit)
        self.north_node_ = ChartLunarNode(LunarNodes.north_node_, north_node_posit)
        self.asc_ = ChartAngle(Angles.asc_, asc_posit)
        self.mc_ = ChartAngle(Angles.mc_, mc_posit)
        self.calc_rest_chart()

    def load(self, path):

        # TODO: If no path specified, provide a default chart or prompt to enter a chart
        # from the command line

        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)
            sun = ChartPlanet(Planets.get(Planets, str(lines[0][0])), Ecliptic(int(lines[0][1]), Signs.get(Signs, lines[0][2]) ,int(lines[0][3])))
            moon = ChartPlanet(Planets.get(Planets, str(lines[1][0])), Ecliptic(int(lines[1][1]), Signs.get(Signs, lines[1][2]) ,int(lines[1][3])))
            mercury = ChartPlanet(Planets.get(Planets, str(lines[2][0])), Ecliptic(int(lines[2][1]), Signs.get(Signs, lines[2][2]) ,int(lines[2][3])))
            venus = ChartPlanet(Planets.get(Planets, str(lines[3][0])), Ecliptic(int(lines[3][1]), Signs.get(Signs, lines[3][2]) ,int(lines[3][3])))
            mars = ChartPlanet(Planets.get(Planets, str(lines[4][0])), Ecliptic(int(lines[4][1]), Signs.get(Signs, lines[4][2]) ,int(lines[4][3])))
            jupiter = ChartPlanet(Planets.get(Planets, str(lines[5][0])), Ecliptic(int(lines[5][1]), Signs.get(Signs, lines[5][2]) ,int(lines[5][3])))
            saturn =  ChartPlanet(Planets.get(Planets, str(lines[6][0])), Ecliptic(int(lines[6][1]), Signs.get(Signs, lines[6][2]) ,int(lines[6][3])))
            uranus = ChartPlanet(Planets.get(Planets, str(lines[7][0])), Ecliptic(int(lines[7][1]), Signs.get(Signs, lines[7][2]) ,int(lines[7][3])))
            neptune = ChartPlanet(Planets.get(Planets, str(lines[8][0])), Ecliptic(int(lines[8][1]), Signs.get(Signs, lines[8][2]) ,int(lines[8][3])))
            pluto = ChartPlanet(Planets.get(Planets, str(lines[9][0])), Ecliptic(int(lines[9][1]), Signs.get(Signs, lines[9][2]) ,int(lines[9][3])))
            chiron = ChartPlanet(Planets.get(Planets, str(lines[10][0])), Ecliptic(int(lines[10][1]), Signs.get(Signs, lines[10][2]) ,int(lines[10][3])))
            asc = ChartAngle(Angles.get(Angles, str(lines[11][0])), Ecliptic(int(lines[11][1]), Signs.get(Signs, lines[11][2]) ,int(lines[11][3])))
            mc = ChartAngle(Angles.get(Angles, str(lines[12][0])), Ecliptic(int(lines[12][1]), Signs.get(Signs, lines[12][2]) ,int(lines[12][3])))
            north_node = ChartLunarNode(LunarNodes.get(LunarNodes, str(lines[13][0])), Ecliptic(int(lines[13][1]), Signs.get(Signs, lines[13][2]) ,int(lines[13][3])))

            # Call the default constructor with the data loaded from the csv
            self.__init__(sun.posit_, moon.posit_, mercury.posit_, venus.posit_, 
                  mars.posit_, jupiter.posit_, saturn.posit_, uranus.posit_, 
                  neptune.posit_, pluto.posit_, chiron.posit_, 
                  asc.posit_, mc.posit_, north_node.posit_)

    def calc_rest_chart(self):
        self.south_node_ = ChartLunarNode(LunarNodes.south_node_, self.north_node_.posit_ + 180)
        self.dsc_ = ChartAngle(Angles.dsc_, self.asc_.posit_ + 180)
        self.ic_ = ChartAngle(Angles.ic_, self.mc_.posit_ - 180)

        # Equal house system cusps
        self.first_ = ChartHouse(Houses.first_, self.asc_.posit_)
        self.second_ = ChartHouse(Houses.second_, self.asc_.posit_ + 30)
        self.third_ = ChartHouse(Houses.third_, self.asc_.posit_ + 60)
        self.fourth_ = ChartHouse(Houses.fourth_, self.asc_.posit_ + 90)
        self.fifth_ = ChartHouse(Houses.fifth_, self.asc_.posit_ + 120)
        self.sixth_ = ChartHouse(Houses.sixth_, self.asc_.posit_ + 150)
        self.seventh_ = ChartHouse(Houses.seventh_, self.asc_.posit_ + 180)
        self.eight_ = ChartHouse(Houses.eight_, self.asc_.posit_ + 210)
        self.ninth_ = ChartHouse(Houses.ninth_, self.asc_.posit_ + 240)
        self.tenth_ = ChartHouse(Houses.tenth_, self.asc_.posit_ + 270)
        self.eleventh_ = ChartHouse(Houses.eleventh_, self.asc_.posit_ + 300)
        self.twelvth_ = ChartHouse(Houses.twelvth_, self.asc_.posit_ + 330)

    def traditional_asc_mc(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.asc_, self.mc_]

    def all_planets(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_, self.chiron_]

    def all_planets_asc_mc_nn(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_, self.chiron_, self.asc_, self.mc_, self.north_node_]

    def get_aspects(self, aspect: Aspect):
        entities = list(self.__dict__.items())[:-12] # Exlude house cusps
        
        print("\n*****************")
        print("* ASPECTS TABLE *")
        print("*****************\n")

        # For each entity compared to all other entities
        for _, (_, value_a) in enumerate(entities):
            for _, (_, value_b) in enumerate(entities):
                if value_a == value_b:
                    continue
                
                delta: Polar = to_polar(value_a.posit_.diff(value_b.posit_))
                aspect = Aspects.get_aspect_from_angle(delta.to_decimal())
                if aspect != None:

                    # Entity
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
        entities = self.traditional_asc_mc()
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
        entities = self.traditional_asc_mc()
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
        entities = self.traditional_asc_mc()
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
            if entity.posit_.sign_ in [Signs.gemini_, Signs.virgo_, Signs.pisces_]:
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
        entities = self.all_planets()
        
        # North/South hemispheres division
        northern_list = []
        southern_list = []
        shift: Ecliptic = self.asc_.posit_
        for entity in entities:
            if self.first_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.seventh_.posit_ - shift:
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
            if self.fourth_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.tenth_.posit_ - shift:
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
        entities = self.all_planets()
        personal_list = []
        social_list = []
        universal_list = []
        for entity in entities:
            # Personal
            shift: Polar = self.asc_.posit_
            if self.first_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.fifth_.posit_ - shift:
                personal_list.append(entity.planet_.name_)
                continue
            
            # Social
            shift = self.fifth_.posit_
            if self.fifth_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.ninth_.posit_ - shift:
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
        entities = self.all_planets()
        development_list = []
        expression_list = []
        expansion_list = []
        transcendence_list = []
        for entity in entities:
            # Self development
            shift: Polar = self.asc_.posit_
            if self.first_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.fourth_.posit_ - shift:
                development_list.append(entity.planet_.name_)
                continue
            
            # Self expression
            shift = self.fourth_.posit_
            if self.fourth_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.seventh_.posit_ - shift:
                expression_list.append(entity.planet_.name_)
                continue
            
            # Self expansion
            shift = self.seventh_.posit_
            if self.seventh_.posit_ - shift <= entity.posit_ - shift and entity.posit_ - shift < self.tenth_.posit_ - shift:
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

if __name__ == "__main__":

    eclipitc_format = " position in `dd sign mm`: "

    # TODO: Uncomment for production, from Catherine's chart
    # Set up chart parameters 
    # sun_posit = get_ecliptic(Planets.sun_.name_ + eclipitc_format)
    # moon_posit = get_ecliptic(Planets.moon_.name_ + eclipitc_format)
    # mercury_posit = get_ecliptic(Planets.mercury_.name_ + eclipitc_format)
    # venus_posit = get_ecliptic(Planets.venus_.name_ + eclipitc_format)
    # mars_posit = get_ecliptic(Planets.mars_.name_ + eclipitc_format)
    # jupiter_posit = get_ecliptic(Planets.jupiter_.name_ + eclipitc_format)
    # saturn_posit = get_ecliptic(Planets.saturn_.name_ + eclipitc_format)
    # uranus_posit = get_ecliptic(Planets.uranus_.name_ + eclipitc_format)
    # neptune_posit = get_ecliptic(Planets.neptune_.name_ + eclipitc_format)
    # pluto_posit = get_ecliptic(Planets.pluto_.name_ + eclipitc_format)
    # chiron_posit = get_ecliptic(Planets.chiron_.name_ + eclipitc_format)
    # asc_posit = get_ecliptic(Angles.asc_.name_ + eclipitc_format)
    # mc_posit = get_ecliptic(Angles.mc_.name_ + eclipitc_format)
    # north_node_posit = get_ecliptic(LunarNodes.north_node_.name_ + eclipitc_format)

    # TODO: Move to debug code
    # print(f"{sun.planet_.name_}: ", end=" "); sun.posit_.print()
    # print(f"{moon.planet_.name_}: ", end=" "); moon.posit_.print()
    # print(f"{mercury.planet_.name_}: ", end=" "); mercury.posit_.print()
    # print(f"{venus.planet_.name_}: ", end=" "); venus.posit_.print()
    # print(f"{mars.planet_.name_}: ", end=" "); mars.posit_.print()
    # print(f"{jupiter.planet_.name_}: ", end=" "); jupiter.posit_.print()
    # print(f"{saturn.planet_.name_}: ", end=" "); saturn.posit_.print()
    # print(f"{uranus.planet_.name_}: ", end=" "); uranus.posit_.print()
    # print(f"{neptune.planet_.name_}: ", end=" "); neptune.posit_.print()
    # print(f"{pluto.planet_.name_}: ", end=" "); pluto.posit_.print()
    # print(f"{chiron.planet_.name_}: ", end=" "); chiron.posit_.print()
    # print(f"{asc.angle_.name_}: ", end=" "); asc.posit_.print()
    # print(f"{mc.angle_.name_}: ", end=" "); mc.posit_.print()
    # print(f"{north_node.lunar_node_.name_}: ", end=" "); north_node.posit_.print()

    # TODO: Override with test data -> move to tests (Γιώτα)
    sun_posit = Ecliptic(15, Signs.libra_, 5)
    moon_posit = Ecliptic(0, Signs.pisces_, 37)
    mercury_posit = Ecliptic(7, Signs.scorpio_, 44)
    venus_posit = Ecliptic(29, Signs.scorpio_, 4)
    mars_posit = Ecliptic(6, Signs.taurus_, 46)
    jupiter_posit = Ecliptic(2, Signs.aquarius_, 27)
    saturn_posit = Ecliptic(4, Signs.cancer_, 41)
    uranus_posit = Ecliptic(22, Signs.libra_, 54)
    neptune_posit = Ecliptic(5, Signs.sagittarius_, 24)
    pluto_posit = Ecliptic(4, Signs.libra_, 42)
    chiron_posit = Ecliptic(18, Signs.aries_, 46)
    asc_posit = Ecliptic(0, Signs.aquarius_, 45)
    mc_posit = Ecliptic(21, Signs.scorpio_, 53)
    north_node_posit = Ecliptic(2, Signs.capricorn_, 6)

    # Set up the chart from user input
    chart = Chart(sun_posit, moon_posit, mercury_posit, venus_posit, 
                  mars_posit, jupiter_posit, saturn_posit, uranus_posit, 
                  neptune_posit, pluto_posit, chiron_posit, 
                  asc_posit, mc_posit, north_node_posit)

    # Override with a chart from the archives
    chart.load("./charts/giota.csv")
    
    chart.get_aspects(Aspects.conjunction_)
    chart.get_polarity()
    chart.get_elements()
    chart.get_modes()
    chart.get_hemispheres()
    chart.get_triple_division()
    chart.get_quadrant_division()
