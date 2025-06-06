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

    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

    # Check parity

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

main()