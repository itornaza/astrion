#
# lunar_nodes
#

import re
from constants import *
from keywords import Keywords

class LunarNode:

    def __init__(self, name):
        self.name_ = name

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), "\n")

# Only supports keywords and no extra information about the nodes
class LunarNodes:
    
    nodal_axis_ = LunarNode(NODAL_AXIS)
    north_node_ = LunarNode(NORTH_NODE)
    south_node_ = LunarNode(SOUTH_NODE)

    lunar_nodes_ = [nodal_axis_, north_node_, south_node_]

    def get(self, input):
        nodal_axis = re.compile(rf'^\s*{NODAL_AXIS}\s*$', re.IGNORECASE)
        north_node = re.compile(rf'^\s*{NORTH_NODE}\s*$', re.IGNORECASE)
        south_node = re.compile(rf'^\s*{SOUTH_NODE}\s*$', re.IGNORECASE)

        if nodal_axis.fullmatch(input):
            lunar_node = self.nodal_axis_
        elif north_node.fullmatch(input):
            lunar_node = self.north_node_
        elif south_node.fullmatch(input):
            lunar_node = self.south_node_
        else:
            return None
        return lunar_node
    
    def print(self, lunar_node):
        LunarNode.print(lunar_node)

    def print_keywords(self, keyword):
        print("\nKeyword list for lunar node " + keyword.upper() + ":\n")
        for k in Keywords.lunar_nodes_[keyword]:
            print("\n\t- " + k)
