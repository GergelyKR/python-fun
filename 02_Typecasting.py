# Typecasting is used to convert variables from one type to another.

name = "John Spartan"
age = 32
gpa = 3.4
is_student = True

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(gpa))  # <class 'float'>

gpa = int(gpa)  # Convert float to int
print(gpa)

age = float(age)  # Convert int to float
print(age)

age = str(age)
age += "1"
print(f"Your new age is {age}")
print(type(age))

name = bool(name)  # Convert str to bool
print(name)