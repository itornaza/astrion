#
# pattern
#
class Pattern:
   
    def __init__(self, name, type, aspects, categories):
        self.name_ = name
        self.type_ = type
        self.aspects_ = aspects
        self.categories_ = categories
    
    def print(self):
        print("\nName\t\t\t:\t", self.name_.upper(),
              "\nType\t\t\t:\t", self.type_,
              "\nAspects\t\t\t:\t", self.aspects_, 
              "\nCategories\t\t:\t", self.categories_, "\n")
        