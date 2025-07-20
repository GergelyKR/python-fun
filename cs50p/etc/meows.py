# Constants = variables that are not meant to be changed
# They are defined in ALL CAPS, but they are not enforced by Python
# By convention they are defined at the top

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()