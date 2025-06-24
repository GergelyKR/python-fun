# with open("d:\\Code\\python-fun\\cs50p\\students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         print(f"{name} is in {house}")

import csv

students = []

with open("d:\\Code\\python-fun\\cs50p\\students.csv") as file:
#   reader = csv.reader(file) -> will return a list
    reader = csv.DictReader(file) # returns a list of dictionaries
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# def get_name(student):
#     return student["name"] -> replaced by lambda (unnamed function)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")