#!/usr/bin/python3

class RSPCA:
    def __init__(self, animals_saved=[]):
        self.animals_saved = animals_saved

    @property
    def animals_saved(self):
        return self.__animals_saved

    @animals_saved.setter
    def animals_saved(self, value):
        self.__animals_saved = value

    def save_animals(self, animals):
        print("/////////////////////")
        print("We are saving:")
        for index, animal in enumerate(animals):
            print(f"Animal #{index}: {animal}")
        print("/////////////////////")
        self.animals_saved = animals
        


rspca = RSPCA()

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

    def __del__(self):
        try:
            if type(rspca) is not RSPCA:
                print("Bye Bye Animals!")
            else:
                rspca.save_animals(self.animals)
        except NameError:
            print("Bye Bye Animals!")
        

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

class Neighbourhood:

    __COUNT = 0
    
    def __init__(self, daycare):
        if Neighbourhood.__COUNT >= 1:
            raise OSError("Bendigo doesn't accept 2 neighbourhoods!")

        Neighbourhood.__COUNT += 1
        self.daycare = daycare

    def __del__(self):
        print("Neighbourhood destroyed")
        Neighbourhood.__COUNT -= 1
        for d in self.daycare:
            del d
        
    @property
    def daycare(self):
        return self.__daycare

    @daycare.setter
    def daycare(self, value):
        self.__daycare = value
    
if __name__ == "__main__":
    dog = Animal("Snoopy", "dog")
    cat = Animal("Garfield", "cat")
    bird = Animal("Big Bird", "bird")
    daycare = Daycare([dog, cat, bird])
    n1 = Neighbourhood([daycare])
    del n1
    
