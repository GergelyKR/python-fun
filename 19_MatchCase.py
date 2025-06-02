# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Cleaner and more readable syntax. Python 3.10+ only.


def get_season(month):
    match month:
        case 1 | 2 | 3:
            return "That month is in Winter"
        case 4 | 5 | 6:
            return "That month is in Spring"
        case 7 | 8 | 9:
            return "That month is in Summer"
        case 10 | 11 | 12:
            return "That month is in Autumn"
        case _: # _ is a wildcard for no matching cases
            return "Invalid month"

month = int(input("Enter the number of a month: "))
print(get_season(month))

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Saturday":
            return True
        case _:
            return False
        
day = input("Enter a day of the week to check if it's part of the weekend: ")
print(is_weekend(day))