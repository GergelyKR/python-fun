def main():
    print_column(3)
    print_row(5)
    print()
    print_square(3)

def print_column(height):
    # for i in range(height):
    #     print("#")
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):

    # for i in range(size):
    #     print("#" *size)

    # For each row in square
    for i in range(size):
        # print_row(size) -> If that function is available

        # For each brick in row
        for j in range(size):

            # Print a brick
            print("#", end="")
        print()

main()