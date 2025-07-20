# first, last = input("What's your name? ").split(" ")
# print(f"Hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# coins = (100, 50, 25)
# print(total(*coins), "Knuts") # Use * to pass individual members of a list (unpack)

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts") # Use ** to unpack dictionaries, passes keys with values

# ---

# *args = allows to pass a variable number of positional (left to right) arguments
# **kwargs = allows to pass a variable number of keyword arguments

def f(*args, **kwargs):
    print("Positional: ", args)
    print("Named:", kwargs)

f(100, 50, 25, galleons=100, sickles=50, knuts=25)