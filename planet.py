#
# planet
#

# Planet class
class Planet:
   
    def __init__(self, planet):
        self.name_ = planet
    
    # Print the details of a planet
    def print(self):
        print("\nName:\t\t", self.name_)