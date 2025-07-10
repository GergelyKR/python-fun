# tuple: Immutable list
# class: Allows inventing custom data types, a blueprint for creating objects
#        Custom containers with custom names for pieces of data
#        You can also define methods for the class
# object: Instance of a class
# method: Function inside a class
class Student:
    # ... -> works as a placeholder
    def __init__(self, name, house): # The function that is called to construct the object
        # self -> refers to the current object that was just created
        self.name = name # create new attribute / instance variable for the new empty object
        self.house = house


def main():
    student = get_student()
    # print(f"{student['name']} from {student['house']}")
    print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return (name, house) -> using "," returns a tuple even without ()
#     return [name, house] # returns a list where values can be changed

# def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    # --
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

def get_student():
    # student = Student() -> creates an object of the class
    # student.name = input"Name: ") -> adding attributes which can be accessed
    # student.house = input("House: ") -> also called instance variables
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # you can use the class as a function
                                   # constructor call to construct (instantiate) a student object
                                   # uses the student class as a template, it will always have a name and a house
    return student


if __name__ == "__main__":
    main()