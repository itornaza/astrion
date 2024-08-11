#
# lunar_nodes
#

import re
from constants import *
from keywords import Keywords

class LunarNodes:
    nodal_axis_ = NODAL_AXIS
    north_node_ = NORTH_NODE
    south_node_ = SOUTH_NODE

    def get(self, ln):
        nodal_axis = re.compile(rf'^\s*{NODAL_AXIS}\s*$', re.IGNORECASE)
        north_node = re.compile(rf'^\s*{NORTH_NODE}\s*$', re.IGNORECASE)
        south_node = re.compile(rf'^\s*{SOUTH_NODE}\s*$', re.IGNORECASE)

        if nodal_axis.fullmatch(ln):
            lunar_node = self.nodal_axis_
        elif north_node.fullmatch(ln):
            lunar_node = self.north_node_
        elif south_node.fullmatch(ln):
            lunar_node = self.south_node_
        else:
            return None
        return lunar_node
    
    def print_keywords(self, lunar_phase_name):
        print("\nKeyword list for lunar phase " + lunar_phase_name.upper() + ":\n")
        for k in Keywords.lunar_phases_[lunar_phase_name]:
            print("\n\t- " + k)



