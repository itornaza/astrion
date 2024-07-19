#
# pattern
#
class Pattern:
   
    def __init__(self, name, type, aspects):
        self.name_ = name
        self.type_ = type
        self.aspects_ = aspects
    
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(),
              "\nType\t\t\t:\t", self.type_,
              "\nAspects\t\t:\t", self.aspects_, "\n")
        