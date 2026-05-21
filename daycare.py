#!/usr/bin/python3

class Animal:
    
    __VALID_SPECIES = ("dog", "cat", "bird")
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        if self.species == "dog":
            sound = "Woof Woof"
        if self.species == "cat":
            sound = "Meow Meow"
        if self.species == "bird":
            sound = "Tweet Tweet"

        return sound + ": My name is " + self.name
    
    def __add__(self, other):
        return Daycare()

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        if not isinstance(value, str):
            raise TypeError("This is not a string. Be better.")
        if value == "":
            raise ValueError("This name is empty. Do better.")
        self.__name = value
        
    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value not in self.__VALID_SPECIES:
            raise TypeError("Not a valid species. You suck!")
        self.__species = value

class Daycare:

    def __init__(self, animals):
        self.animals = animals

    def __str__(self):
        border = "========================="
        row = "Animal #{}: {}\n"
        string = border + '\n'
        for i, v in enumerate(self.animals):
            string += row.format(i, v)
        string += border
        return string
        
    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, animals):
        if not isinstance(animals, list):
            raise TypeError("Not a list of animals")
        if not animals:
            raise TypeError("This is an empty list you fuckhead.")
        if not all(type(animal) is Animal for animal in animals):
            raise TypeError("Not an animal")

        self.__animals = animals
        
if __name__ == "__main__":
    dog = Animal("Snoopy", "dog")
    cat = Animal("Garfield", "cat")
    bird = Animal("Big Bird", "bird")
    daycare = Daycare([dog, cat, bird])
    print(f"Name: {dog.name} Species: {dog.species}")
    print(f"Name: {cat.name} Species: {cat.species}")
    print(f"{daycare}")
