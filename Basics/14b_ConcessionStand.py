# Concession stand program

menu = {"pizza": 3.0,
        "soda": 1.5,
        "nachos": 2.0,
        "popcorn": 1.25,
        "chips": 1.0,
        "fries": 2.5,
        "pretzel": 2.0,
        "lemonade": 1.75}

cart = [] # to track selected items
total = 0 # to track total cost

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total cost: ${total:.2f}")