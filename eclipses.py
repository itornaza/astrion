#
# eclipses
#

from pangle import Ecliptic

class Saros:
    def __init__(self, id: int, saros_type: str):
        self.id_ = id
        self.type_ = saros_type

class EclipseType:
    lunar_ = "Lunar"
    solar_ = "Solar"

class LunarEclipseCategory:
    partial = "Partial"
    total = "Total"

class SolarEclipseCategory(LunarEclipseCategory):
    """Only Solar eclipses can be annular, i.e. ring of fire"""
    annular = "Annular"

class Eclipse:
    def __init__(self, eclipse_type: EclipseType, saros: Saros, 
                 posit: Ecliptic):
        self.type_ = eclipse_type
        self.saros_ = saros
        self.posit_ = posit

class SolarEclipse(Eclipse):
    def __init__(self, saros: Saros, category: SolarEclipseCategory, 
                 posit: Ecliptic):
        super().__init__(EclipseType.solar_, posit, saros)
        self.categoty_: SolarEclipseCategory = category

class LunarEclipse(Eclipse):
    def __init__(self, saros: Saros, category: LunarEclipseCategory, 
                 posit: Ecliptic):
        super().__init__(EclipseType.lunar_, posit, saros)
        self.categoty_: SolarEclipseCategory = category

if __name__ == "__main__":
    pass    