#
# chart
#

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
        
        # Planets
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

        # Nodes
        self.north_node_ = ChartLunarNode(LunarNodes.north_node_, north_node_posit)
        self.south_node_ = ChartLunarNode(LunarNodes.south_node_, north_node_posit + 180)

        # Equal house system angles
        self.asc_ = ChartAngle(Angles.asc_, asc_posit)
        self.dsc_ = ChartAngle(Angles.dsc_, asc_posit + 180)
        self.mc_ = ChartAngle(Angles.mc_, mc_posit)
        self.ic_ = ChartAngle(Angles.ic_, mc_posit - 180)

        # Equal house system cusps
        self.first_ = ChartHouse(Houses.first_, asc_posit)
        self.second_ = ChartHouse(Houses.second_, asc_posit + 30)
        self.third_ = ChartHouse(Houses.third_, asc_posit + 60)
        self.fourth_ = ChartHouse(Houses.fourth_, asc_posit + 90)
        self.fifth_ = ChartHouse(Houses.fifth_, asc_posit + 120)
        self.sixth_ = ChartHouse(Houses.sixth_, asc_posit + 150)
        self.seventh_ = ChartHouse(Houses.seventh_, asc_posit + 180)
        self.eight_ = ChartHouse(Houses.eight_, asc_posit + 210)
        self.ninth_ = ChartHouse(Houses.ninth_, asc_posit + 240)
        self.tenth_ = ChartHouse(Houses.tenth_, asc_posit + 270)
        self.eleventh_ = ChartHouse(Houses.eleventh_, asc_posit + 300)
        self.twelvth_ = ChartHouse(Houses.twelvth_, asc_posit + 330)

    def traditional_asc_mc(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.asc_, self.mc_]

    def all_planets(self):
        return [self.sun_, self.moon_, self.mercury_, self.venus_, self.mars_, 
                self.jupiter_, self.saturn_, self.uranus_, self.neptune_,
                self.pluto_, self.chiron_]

    def get_aspects(self, aspect: Aspect):
        entities = list(self.__dict__.items())[:-12] # Exlude house cusps
        
        print()
        print("*****************")
        print("* ASPECTS TABLE *")
        print("*****************")
        print()

        # For each entity compared to all other entities
        for _, (_, value_a) in enumerate(entities):
            for _, (_, value_b) in enumerate(entities):
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
            
            print() # Separate entities with a new line

    def get_polarity(self):
        entities = self.traditional_asc_mc()
        positive: int = 0
        negative: int = 0

        for entity in entities:
            if entity.posit_.sign_ in [Signs.aries_, Signs.leo_, Signs.sagittarius_, 
                                       Signs.gemini_, Signs.libra_, Signs.aquarius_]:
                positive = positive + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[31m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[31m{entity.angle_.name_}\033[0m")

            if entity.posit_.sign_ in [Signs.taurus_, Signs.virgo_, Signs.capricorn_,
                                       Signs.cancer_, Signs.scorpio_, Signs.pisces_]:
                negative = negative + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[34m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[34m{entity.angle_.name_}\033[0m")

        print()
        print(f"\033[1m\033[31mPositive = {positive}\033[0m", end=" ")
        print(f"\033[1m\033[34mNegative = {negative}\033[0m")
        print()
        
        assert positive + negative == 9

    def get_elements(self):
        entities = self.traditional_asc_mc()
        fire: int = 0
        earth: int = 0
        air: int = 0
        water: int = 0

        for entity in entities:
            if entity.posit_.sign_ in [Signs.aries_, Signs.leo_, Signs.sagittarius_]:
                fire = fire + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[31m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[31m{entity.angle_.name_}\033[0m")

            if entity.posit_.sign_ in [Signs.taurus_, Signs.virgo_, Signs.capricorn_]:
                earth = earth + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[33m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[33m{entity.angle_.name_}\033[0m")

            if entity.posit_.sign_ in [Signs.gemini_, Signs.libra_, Signs.aquarius_]:
                air = air + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[36m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[36m{entity.angle_.name_}\033[0m")

            if entity.posit_.sign_ in [Signs.cancer_, Signs.scorpio_, Signs.pisces_]:
                water = water + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[34m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[34m{entity.angle_.name_}\033[0m")

        print()
        print(f"\033[1m\033[31mFire = {fire}\033[0m", end=" ")
        print(f"\033[1m\033[33mEarth = {earth}\033[0m", end=" ")
        print(f"\033[1m\033[36mAir = {air}\033[0m", end=" ")
        print(f"\033[1m\033[34mWater = {water}\033[0m")
        print()

        assert fire + earth + air + water == 9

    def get_modes(self):
        entities = self.traditional_asc_mc()
        cardinal: int = 0
        fixed: int = 0
        mutable: int = 0

        for entity in entities:
            if entity.posit_.sign_ in [Signs.aries_, Signs.cancer_, Signs.libra_, Signs.capricorn_]:
                cardinal = cardinal + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[31m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[31m{entity.angle_.name_}\033[0m")

            if entity.posit_.sign_ in [Signs.taurus_, Signs.leo_, Signs.scorpio_, Signs.aquarius_]:
                fixed = fixed + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[33m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[33m{entity.angle_.name_}\033[0m")

            if entity.posit_.sign_ in [Signs.gemini_, Signs.virgo_, Signs.pisces_]:
                mutable = mutable + 1
                if isinstance(entity, ChartPlanet): 
                    print(f"\033[1m\033[36m{entity.planet_.name_}\033[0m")
                elif isinstance(entity, ChartAngle): 
                    print(f"\033[1m\033[36m{entity.angle_.name_}\033[0m")

        print()
        print(f"\033[1m\033[31mFire = {cardinal}\033[0m", end=" ")
        print(f"\033[1m\033[33mEarth = {fixed}\033[0m", end=" ")
        print(f"\033[1m\033[36mAir = {mutable}\033[0m", end=" ")
        print()
        
        assert cardinal + fixed + mutable == 9

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

    # TODO: Override with test data -> move to tests
    sun_posit = Ecliptic(21, Signs.taurus_, 2)
    moon_posit = Ecliptic(27, Signs.taurus_, 31)
    mercury_posit = Ecliptic(8, Signs.taurus_, 6)
    venus_posit = Ecliptic(18, Signs.aries_, 23)
    mars_posit = Ecliptic(15, Signs.capricorn_, 47)
    jupiter_posit = Ecliptic(9, Signs.cancer_, 0)
    saturn_posit = Ecliptic(24, Signs.pisces_, 48)
    uranus_posit = Ecliptic(12, Signs.capricorn_, 27)
    neptune_posit = Ecliptic(10, Signs.cancer_, 33)
    pluto_posit = Ecliptic(22, Signs.gemini_, 29)
    chiron_posit = Ecliptic(18, Signs.aquarius_, 10)
    asc_posit = Ecliptic(7, Signs.scorpio_, 57)
    mc_posit = Ecliptic(16, Signs.leo_, 9)
    north_node_posit = Ecliptic(26, Signs.cancer_, 48)

    # Set up the chart
    chart = Chart(sun_posit, moon_posit, mercury_posit, venus_posit, 
                  mars_posit, jupiter_posit, saturn_posit, uranus_posit, 
                  neptune_posit, pluto_posit, chiron_posit, 
                  asc_posit, mc_posit, north_node_posit)
    
    chart.get_aspects(Aspects.conjunction_)
    chart.get_polarity()
    chart.get_elements()
    chart.get_modes()