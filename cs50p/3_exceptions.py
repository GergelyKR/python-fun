def main():
    x = get_int("What's x? ")
    print(f"x is {x}.")
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            # break -> could be done here too
            # return int(input("What's x? \n")) -> to avoid using else
        except ValueError:
            # pass -> reprompt without error message
            print("x is not an integer")
        else:
            return x # breaks out and also returns value

main()