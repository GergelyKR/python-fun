# 2D list = list of lists, matrix of data

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["carrot", "potato", "onion"]
meats = ["chicken", "beef", "pork"]

groceries = [fruits, vegetables, meats] # 2D list
# groceries[0] = fruits (first index marks the row, second marks the column)
# groceries[1] = vegetables
# groceries[2] = meats
# print(groceries[1][0]) # row 1, column 0 -> carrot
# print(groceries[2][1]) # row 2, column 1 -> beef

groceries = [["apple", "orange", "banana", "coconut"],
            ["carrot", "potato", "onion"],
            ["chicken", "beef", "pork"]]
# to declare all rows and columns at once
# groceries = ({"apple", "orange", "banana", "coconut"},
#             {"carrot", "potato", "onion"},
#             {"chicken", "beef", "pork"}]
# Also possible to have list of tuples, or 2D tuple, or tuple of sets


for collection in groceries:
    # print(collection) # prints each row
    for food in collection:
        print(food, end=" ")
    print() # to add new line

# 2d numpad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", "0", "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print() # to add new line