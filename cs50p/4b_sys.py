import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print(f"Hello, {sys.argv[1]}")

for arg in sys.argv[1:]: # Slice of a list, starts at index 1
    print("Hello, my name is", arg)