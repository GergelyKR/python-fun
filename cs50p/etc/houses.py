students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# houses = []
houses = set() # data type where duplicates are eliminated
for student in students:
    # if student["house"] not in houses:
        # houses.append(student["house"]) 
    houses.add(student["house"]) # for sets, "add" instead of "append"

for house in sorted(houses):
    print(house)