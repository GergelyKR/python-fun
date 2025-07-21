students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# List comprehension with if condition:

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]
# 
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

def is_gryffindor(s):
    # if s["house"] == "Gryffindor":
    #     return True
    # return False
    return s["house"] == "Gryffindor" # If it does, "True", otherwise "False"

# Map returns one value for each element in the sequence
# For adding students conditionally, we can use filter. Filter expects a "True or False" / "Include or not include" function
gryffindors = filter(is_gryffindor, students) # Apply function to each element

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]): # Lambda: anonymous function
    print(gryffindor["name"])

"""
sorted() is a built-in function that returns a new sorted list.
key=lambda s: s["name"] tells Python how to sort the list.
lambda s: s["name"] is an anonymous function that takes one element (s) from the list and returns its "name" value. This is used as the basis for sorting.
"""