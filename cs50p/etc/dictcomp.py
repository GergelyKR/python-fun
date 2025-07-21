students = ["Hermione", "Harry", "Ron"]

# gryffindors = []
# 
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# With list comprehension: I want an dictionary for each student, with two keys
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# Creating a dictionary called gryffindor
# Every key is going to be a name of the student
# Every value is going to be Gryffindor
# This dictionary comprehension will be constructed from the list of students one at a time
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)