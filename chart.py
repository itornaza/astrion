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
        self.posit = posit

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
        self.neptune = ChartPlanet(Planets.neptune_, neptune_posit)
        self.pluto = ChartPlanet(Planets.pluto_, pluto_posit)
        self.chiron_ = ChartPlanet(Planets.chiron_, chiron_posit)

        # Nodes
        self.north_node_ = ChartLunarNode(LunarNodes.north_node_, north_node_posit)

        # TODO: Fix adding and subtracting scalar from Ecliptic!
        self.south_node_ = ChartLunarNode(LunarNodes.south_node_, 
                                          north_node_posit - to_ecliptic(Polar(180, 0)))

        # Equal house system angles
        self.asc_ = ChartAngle(Angles.asc_, asc_posit)
        self.dsc_ = ChartAngle(Angles.dsc_, asc_posit + to_ecliptic(Polar(180, 0)))
        self.mc_ = ChartAngle(Angles.ic_, mc_posit)
        self.ic_ = ChartAngle(Angles.mc_, mc_posit - to_ecliptic(Polar(180, 0)))

        # Equal house system cusps
        self.first_ = ChartHouse(Houses.first_, asc_posit)
        self.second_ = ChartHouse(Houses.second_, asc_posit + to_ecliptic(Polar(30, 0)))
        self.third_ = ChartHouse(Houses.third_, asc_posit + to_ecliptic(Polar(60, 0)))
        self.fourth_ = ChartHouse(Houses.fourth_, asc_posit + to_ecliptic(Polar(90, 0)))
        self.fifth_ = ChartHouse(Houses.fifth_, asc_posit + to_ecliptic(Polar(120, 0)))
        self.sixth_ = ChartHouse(Houses.sixth_, asc_posit + to_ecliptic(Polar(150, 0)))
        self.seventh_ = ChartHouse(Houses.seventh_, asc_posit + to_ecliptic(Polar(180, 0)))
        self.eight_ = ChartHouse(Houses.eight_, asc_posit + to_ecliptic(Polar(210, 0)))
        self.ninth_ = ChartHouse(Houses.ninth_, asc_posit + to_ecliptic(Polar(240, 0)))
        self.tenth_ = ChartHouse(Houses.tenth_, asc_posit + to_ecliptic(Polar(270, 0)))
        self.eleventh_ = ChartHouse(Houses.eleventh_, asc_posit + to_ecliptic(Polar(300, 0)))
        self.twelvth_ = ChartHouse(Houses.twelvth_, asc_posit + to_ecliptic(Polar(330, 0)))

    def get_aspects(self, aspect: Aspect):
        entities = list(self.__dict__.items())[:-12] # Exlude house cusps
        for entity_a in enumerate(entities):
            for entity_b in enumerate(entities):
                if entity_a == entity_b:
                    continue
                d: Polar = to_polar(entity_a.posit.diff(entity_b.posit))
                aspect = Aspects.get_aspect_from_angle(d.to_decimal())
                if aspect != None:
                    print(f"\n\t'{entity_a.name_} {aspect.name_} {entity_b.name_} = \
                          {d.deg_:.0f}° {d.min_:.0f}")

if __name__ == "__main__":

    eclipitc_format = " position in `dd sign mm`: "

    # TODO: Uncomment for production
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