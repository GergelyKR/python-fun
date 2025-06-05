# Method: A function that's built in to a type of value, like the functions used below
# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name (only works with two words)
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}")