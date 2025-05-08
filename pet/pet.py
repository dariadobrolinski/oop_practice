class Pet:
    def __init__(self, name, species, age, weight):
        self._name = name
        self._species = species
        self._age = age
        self._weight = weight

    def getName(self):
        return self._name
    
    def getSpecies(self):
        return self._species
    
    def getAge(self):
        return self._age
    
    def getWeight(self):
        return self._weight
    
    def isAdoptable(self):
        return self._age < 10 and self._weight < 100
    
    def __eq__(self, other):
        return self._name == other._name and self._species == other._species
    
    def __lt__(self, other):
        return self._weight < other._weight
    
    def __str__(self):
        return f"Name: {self._name}, Species: {self._species}, Age: {self._age}, Weight: {self._weight} lbs"