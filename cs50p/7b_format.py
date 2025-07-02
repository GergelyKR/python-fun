import re

name = input("What's your name? ").strip()
# matches = re.search(r"^=(.+), (.+)$", name)

# if matches:
    # last, first = matches.groups() -> example 1
    # last = matches.group(1) -> example 2
    # first = matches.group(2)
    # name = f"{first} {last}"
    # name = matches.group(2) + " " + matches.group(1)

# With walrus operator -> Assign a value to a variable if the condition is true
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")