# input() promts the user to enter data and stores it as string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old!")

# Rectangle area calculator

print("Let me help with some rectangle area calculation!")
rec_l = float(input("What is the length of the rectangle?: "))
rec_w = float(input("What is the width of the rectangle?: "))
print(f"Length = {rec_l} Width = {rec_w}") 
print(f"The area you are looking for is {rec_l * rec_w} square units")

# Shopping cart

item = input("What would you like to buy?")
quantity = int(input("How many do you need?"))
price = float(input("How much does it cost per item?"))
print(f"You have bought {quantity} x {item}/s")
print(f"Total cost of shopping is ${quantity * price}")