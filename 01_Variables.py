# This is my first Python program
# Variable = Container for values, acts if it was the value itself

print("I like pizza!")
print("It's really good!")

first_name = "John"
food = "pizza"
email = "macska@fake.com"

# Strings
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 26
quantity = 3
num_of_students = 32

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.4
distance = 10.4

print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance} kilometers")

# Boolean

is_student = False
for_sale = True
is_online = True
print(f"Are you a student? {is_student}!")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available for sale")

if is_online:
    print("You are online")
else:
    print("You are offline")