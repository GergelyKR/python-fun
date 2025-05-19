# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
                           # Print or assing one of two values based on a condition
                           # X if condition else Y

num = 5
a = 6
b = 7
age = 25
temp = 34
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Minor"
weather = "Hot" if temp > 30 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access"

print(f"The greater number is: {max_num}")
print(f"The smaller number is: {min_num}")
print(f"Your status is: {status}")
print(f"The weather is: {weather}")
print(f"Your access level is: {access_level}")
# The conditional expression is a one-line shortcut for the if-else statement