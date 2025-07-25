# inheritance: define multiple classes that are related

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard): # inherits from Wizard "superclass"
    def __init__(self, name, house):
        super().__init__(name) # accessing the superclass' init method
        self.house = house
    
    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject



wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Potions")