students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Harry"]) # returns "Gryffindor"

for student in students:
    # print(student) -> Iterates over keys
    print(f"{student} is in {students[student]}") # Iterates over values

print()
# ---

studentpatron = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    }
]

for student in studentpatron:
    # print(student["name"], student["house"], student["patronus"], sep=", ")
    print(f"{student['name']} is in {student['house']} and their patronus is {student['patronus']}")