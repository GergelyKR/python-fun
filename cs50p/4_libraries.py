import random # to import a whole library, then call with random.****
# from random import choice -> loads function into the namespace
import statistics

coin = random.choice(["heads", "tails"])
print(f"Coin flip: {coin}")

number = random.randint(1, 10)
print(f"Random number: {number}")

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
for card in cards:
    print(card, end=" ")

print()
print(statistics.mean([100, 90]))