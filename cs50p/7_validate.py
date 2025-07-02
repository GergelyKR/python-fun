import re

# . = any character
# + = one or more
# ? = zero or one
# * = zero or more
# ^ = start of the string
# $ = end of the string
# [] = a set of characters
# [^] = exclude a set of characters
# \w = word characters (a-z, A-Z, 0-9, _)
# \W = non-word characters
# \d = digits (0-9)
# \D = non-digits
# \s = whitespace (space, tab, newline)
# \S = non-whitespace
# A|B = either A or B
# (...) = group
# (?:...) = non-capturing group

email = input("What's your email? ").strip() # .strip() removes spaces from the beginning and the end of the string

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")