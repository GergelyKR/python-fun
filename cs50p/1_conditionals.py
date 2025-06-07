# Check grade

def main():

    score = int(input("Enter your score: "))

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

    # Check parity

    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

    # Check house

    name = input("Enter your name: ")

    # if name == "Harry" or name == "Hermione" or name == "Ron":
    #     print("Gryffindor")
    # elif name == "Draco":
    #     print("Slytherin")
    # else:
    #     print("Who are you?")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who are you?")

def is_even(n):
    # return True if n % 2 == 0 else False

    return (n % 2 == 0)

    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

main()