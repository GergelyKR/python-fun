# keyword arguments = an argument preceeded by an identifier
#                     matches the name of the function's parameters
#                     helps with readibility
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# hello("Hello", "John", "Doe", "Mr.") -> position matters

hello("Hello", title="Mr.", last="Doe", first="John") # Positional arguments come before keyword arguments

for x in range(1, 11):
    print(x, end=" ") # end is a keyword argument of print function

print()
print("1", "2", "3", "4", "5", sep="-")

# ---

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)