# instance methods:
# belong to or operate on specific objects
# class methods:
# operate on the entire class or on all objects of that class

import random


class Hat:
    # def __init__(self): -> not needed if we don't want to initialize objects
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variable, one shared copy for all objects

    @classmethod
    def sort(cls, name): # cls references to the class itself
        print(name, "is in", random.choice(cls.houses))


# hat = Hat() -> no need to instantiate an object anymore
Hat.sort("Harry") # using the class method