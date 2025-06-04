# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower()== "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    if food == foods[-1]:
        print(food, end="")
        break
    print(food, end=", ")

for price in prices:
    total += price

print() # to add new line
print(f"Your total is: ${total}")