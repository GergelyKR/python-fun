# List comprehension = A concise vay to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression FOR value IN iterable IF condition]

# doubles = []
# for x in range(1, 11): # In the range function, second number is exclusive
#     doubles.append(x * 2)
# print(doubles)

doubles = [x * 2 for x in range(1, 11)]
print(doubles)

triples = [y * 3 for y in range(1, 11)]
print(triples)

squares = [z * z for z in range(1, 11)]
print(squares)

print()
# ---

fruits = ["apple", "banana", "coconut", "orange"]
fruit_chars = [fruit[0] for fruit in fruits]
# fruits = [fruit.upper() for fruit in ["apple", "banana", "coconut"]]
print(fruit_chars)

print()
# ---

numbers = [1, -2, 3, -4, 5, -6, 8]
positive_nums = [num for num in numbers if num>= 0] # We do not modify, we just return the number
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(f"Positive numbers: {positive_nums}")
print(f"Negative numbers: {negative_nums}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")

print()
# ---

grades = [85, 42, 79, 80, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(f"Passing grades: {passing_grades}")