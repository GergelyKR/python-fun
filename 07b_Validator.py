# validate user input
# 1. username is no longer than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username can't be longer than 12 characters.")
# elif username.find(" ") > 0:
elif not username.find(" ") == -1: # -1 means no spaces found
    print("Username can't contain spaces.")
# elif username.isalpha() == False:
elif not username.isalpha(): # isalpha() returns True if all characters are alphabetic
    print("Username can't contain digits.")
else:
    print(f"Username is valid. Welcome {username}!")