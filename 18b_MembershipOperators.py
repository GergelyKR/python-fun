# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word: # Returns True or False
    print(f"{letter} is in the word.")
else:
    print(f"{letter} is not in the word.")

if letter not in word: # Returns True or False
    print(f"{letter} was not found.")
else:
    print(f"There is a {letter}.")

print()
# ---

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter a student name: ")
if student in students:
    print(f"{student} is a student.")
else:
    print(f"{student} was not found.")

print()
# ---

grades = {"Sandy": "A", "Patrick": "B", "Spongebob": "C"}

student = input("Enter the name of the student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found.")

print()
# ---

email = input("Enter your email address: ")

if "@" in email and "." in email:
    print("E-mail address is valid.")
else:
    print("E-mail address is not valid.")