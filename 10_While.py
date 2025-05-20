# while loop = executes some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "": # like a repeating if statement
    print("You didn't enter a name.")
    name = input("Enter your name: ") # needed for exiting the loop

print(f"Hello {name}.") # once the condition is false, the loop ends

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")

print("Ok, how about some numbers?")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}.")