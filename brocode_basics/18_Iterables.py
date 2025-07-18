# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers): # for every element in the iterable of elements
    print(number, end= " - ")

fruits = {"apple", "orange", "banana", "coconut"}
print()

# for fruit in reversed(fruits): -> Tuples are not reversible
#     print(fruit)

name = "John Smith"

for character in name:
    print(character, end =" ")

print()

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key in my_dictionary:
    print(key)
for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(f"{key} = {value}")