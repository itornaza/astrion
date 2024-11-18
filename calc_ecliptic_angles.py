# 
# calc_ecliptic_angles.py
#

from aspects import *
from pangle import Ecliptic, Polar, to_polar, get_ecliptic
from signs import *

__all__ = ['calculate_aspect_from_angle']

def calculate_aspect_from_angle():
    """Calculates the aspect formed between two ecliptic angles"""
    
    e1 = get_ecliptic("Enter first angle `dd sign mm`: ")
    e2 = get_ecliptic("Enter second angle `dd sign mm`: ")
    
    d: Polar = to_polar(e1.diff(e2))    
    aspect = Aspects.get_aspect_from_angle(d.to_decimal())
    if aspect != None:
        print(f"\n\t{d.deg_:.0f}° {d.min_:.0f}' -- {aspect.name_}")
    else:
        print(f"\n\t{d.deg_:.0f}° {d.min_:.0f}' -- Unaspected")

if __name__ == "__main__":
    calculate_aspect_from_angle()
    