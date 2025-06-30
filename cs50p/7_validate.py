import re

# . = any character
# + = one or more
# ? = zero or one
# * = zero or more
# ^ = start of the string
# $ = end of the string

email = input("What's your email? ").strip() # .strip() removes spaces from the beginning and the end of the string

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")