def main():
        
    i = 0
    while i < 3:
        print("meow")
        i += 1

    print()

    # for i in[0, 1, 2]: -> assigns i to 0, 1, 2 and runs the indented code every time
    #     print("meow")

    for _ in range(3): # _ for variables that won't be used later. Range will act the same way as "for i in[0, 1, 2]"
        print("meow")

    number = get_number()
    meow(number)

    print()
    # ---

    students = ["Harry", "Hermione", "Ron"]
    
    # for i in range(students) -> Students is not a number, it's not an integer, range expects an integer.
    for i in range(len(students)): # len will return the number of items as integer, so range works
        print(i + 1, students[i])


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