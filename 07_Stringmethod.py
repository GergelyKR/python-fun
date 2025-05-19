name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("c") # Find first occurence
# result = name.rfind("q") # Find last occurence
# name = name.capitalize() # Capitalize the first letter
# name = name.upper() # Convert to uppercase
# name = name.lower() # Convert to lowercase
# result = name.isdigit() # Check if all characters are digits
# result = name.isalpha() # Check if all characters are alphabetic
# result = phone_number.count("-") # Count the number of dashes
result = phone_number.replace("-", " ") # Replace first with second

print(result)

# print(help(str)) # Display the help documentation for the str class