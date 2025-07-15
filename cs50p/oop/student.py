# tuple: Immutable list
# class: Allows inventing custom data types, a blueprint for creating objects
#        Custom containers with custom names for pieces of data
#        You can also define methods for the class
# object: Instance of a class
# method: Function inside a class
# property: Attribute of an object with more functionality
#  - decorator: A function that modifies another function

# int str and list for example are classes as well, calling init function
# they create objects on which we can use in-built methods

class Student:
    # ... -> works as a placeholder
    def __init__(self, name, house): # The function that is called to construct the object
        # self -> refers to the current object that was just created
        self.name = name # create new attribute / instance variable for the new empty object
        self.house = house

    def __str__(self): # accesses the defined object's attributes and returns a string representation of the object
        return f"{self.name} from {self.house}"
    
    # getter -> function for a class to get some attributes
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property # decorator for getter
    def house(self):
        return self._house # instance variable must have different name than the property    
    # setter -> function in a class that sets some values with error checking
    @house.setter # decorator for setter. it is called every time .house is accessed
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    # _{variable} means "private" or "don't touch this" to avoid breaking code
    # __{variable} means even more strictly not to touch the variable

def main():
    student = get_student()
    print(student)
    # student.house = "Number Four, Privet Drive" -> will raise an error due to the setter error-checking
    # print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return (name, house) -> using "," returns a tuple even without ()
#     return [name, house] # returns a list where values can be changed


def get_student():
    # student = Student() -> creates an object of the class
    # student.name = input"Name: ") -> adding attributes which can be accessed
    # student.house = input("House: ") -> also called instance variables
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    # you can use the class as a function
    # a constructor call to construct (instantiate) a student object
    # uses the student class as a template, it will always have a name and a house


if __name__ == "__main__":
    main()