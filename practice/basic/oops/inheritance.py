class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def ani(self):
        print(f"the name of the dog is {self.name} and the species is {self.species}")
class Cat(Animal):
    def __init__(self,name,specie):
        self.name = name
        self.specie = specie
    def catan(self):
        print(f"the name of cat is  {self.name}and the species is {self.specie}")
a1 = Animal("max","labradour")
a1.ani()
a2 = Cat("maxi","perisan")
a2.catan()