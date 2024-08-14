#
# quadrants
#

import re
from constants import *
from keywords import Keywords

class Quadrant:

    def __init__(self, name):
        self.name_ = name

    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(), "\n")

# Only supports keywords and no extra information about the quadrants
class Quadrants:
    
    self_development_ = Quadrant(SELF_DEVELOPMENT)
    self_expression_ = Quadrant(SELF_EXPRESSION)
    self_expansion_ = Quadrant(SELF_EXPANSION)
    self_transcendence_ = Quadrant(SELF_TRANSENDENCE)

    quadrants_ = [self_development_, self_expression_, 
                   self_expression_, self_transcendence_]

    def get(self, input):
        self_development = re.compile(rf'^\s*({SELF_DEVELOPMENT}|{"Q1"})\s*$', re.IGNORECASE)
        self_expression = re.compile(rf'^\s*({SELF_EXPRESSION}|{"Q2"})\s*$', re.IGNORECASE)
        self_expansion = re.compile(rf'^\s*({SELF_EXPANSION}|{"Q3"})\s*$', re.IGNORECASE)
        self_transcendence = re.compile(rf'^\s*({SELF_TRANSENDENCE}|{"Q4"})\s*$', re.IGNORECASE)

        if self_development.fullmatch(input):
            quadrant = self.self_development_
        elif self_expression.fullmatch(input):
            quadrant = self.self_expression_
        elif self_expansion.fullmatch(input):
            quadrant = self.self_expansion_
        elif self_transcendence.fullmatch(input):
            quadrant = self.self_transcendence_
        else:
            return None
        return quadrant
    
    def print(self, quadrant):
        Quadrant.print(quadrant)

    def print_keywords(self, keyword):
        print("\nKeyword list for quadrant " + keyword.upper() + ":\n")
        for k in Keywords.quadrants_[keyword]:
            print("\n\t- " + k)
