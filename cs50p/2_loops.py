def main():
        
    i = 0
    while i < 3:
        print("meow")
        i += 1

    print()

    # for i in[0, 1, 2]:
    #     print("meow")

    for _ in range(3): # _ for variables that won't be used later
        print("meow")

    number = get_number()
    meow(number)

def get_number():
    while True: # Keep looping until you get valid input
        n = int(input("\nHow many meows? "))
        if n > 0:
            # break
            return n
        # return n
    
def meow(n):
    for _ in range(n):
        print("meow")

main()