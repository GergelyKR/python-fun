# collection = single "variable" used to store multiple values
#   1. List  = ordered and changeable. Duplicates OK
#   2. Set   = unordered and immutable, but Add/Remove OK. NO duplicates
#   3. Tuple = ordered and unchangeable. Duplicates OK. FASTER
#   Index operators and for loops work with all collections

fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits)) # dir lists different methods for the collection
# print(help(fruits)) # help lists the methods and their descriptions
print(len(fruits)) # len returns the number of items in the collection
print("apple" in fruits) # in checks if the item is in the collection

print(fruits[0]) # apple
print(fruits[1]) # orange
print(fruits[2]) # banana
print(fruits[3]) # coconut
print(fruits[::-1])

for fruit in fruits:
    print(fruit) # apple, orange, banana, coconut

fruits[0] = "pineapple" # change the first item
for fruit in fruits:
    print(fruit) # pineapple, orange, banana, coconut

fruits.append("grape") # add an item to the end of the list
fruits.remove("grape") # remove an item from the list
fruits.insert(0, "pineapple")
fruits.sort() # sort the list in alphabetical order
fruits.reverse() # reverse the order of the list, not alphabetical
# fruits.clear() # remove all items from the list
print(fruits.index("pineapple")) # returns the index of the item
print(fruits.count("banana")) # returns the number of times the item appears

animals = {"dog", "cat", "fish", "bird"} # set, no indexing, random order
animals.pop() # remove a random item from the set   

vegetables = ("carrot", "potato", "onion") # ordered but not changeable. Two methods, faster
# tuples should be used if list is not going to change