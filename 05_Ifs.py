# if = Do some code if the condition is true,
#      else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to drive.")
elif age >= 18:
    print("You are eligible for a driver's license.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You must be 18+ to sign up for a driver's license.")

response = input("Would you like food? (Y/N): ")

if response == "Y": # == makes a comparison, = would assign a value
    print("Have some food!")
else:
    print("No foor for you then.")

name = input("Enter your name: ")

if name == "":
    print("No name entered!")
else:
    print(f"Hello {name}!")

for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is NOT for sale.")