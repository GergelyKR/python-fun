# dictionary = a collection of {key:value} pairs
#              ordered, changeable, no duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))  # returns "Washington D.C."

if capitals.get("Japan"):
    print("That capital is in the dictionary.")
else:
    print("That capital is not in the dictionary.")

capitals.update({"Germany": "Berlin"}) # adds or updates a key-value pair
# capitals.pop("China")  # removes a key-value pair
# capitals.popitem()  # removes the last inserted key-value pair
# capitals.clear()  # removes all key-value pairs

keys = capitals.keys()
print(keys)  # returns the list of keys in a list-like object
for key in capitals.keys(): # iterating through keys
    print(key)

values = capitals.values()
for value in capitals.values():  # iterating through values
    print(value)

items = capitals.items()  # returns a 2D list of tuples (key, value)
for key, value in capitals.items():  # iterating through key-value pairs with two counters
    print(f"{key}: {value}")