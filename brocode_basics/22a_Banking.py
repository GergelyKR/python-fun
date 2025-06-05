# Python Banking Program

def show_balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")

def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount > 0:
        print("*******************")
        print(f"Deposit of ${amount:.2f} successful.")
        print("*******************")
        return amount
    else:
        print("*******************")
        print("Deposit amount must be greater than zero.")
        print("*******************")
        return 0

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount > balance:
        print("*******************")
        print("Insufficient funds.")
        print("*******************")
        return 0
    elif amount > 0:
        print("*******************")
        print(f"Withdrawal of ${amount:.2f} successful.")
        print("*******************")
        return amount
    else:
        print("*******************")
        print("Withdrawal amount must be greater than zero.")
        print("*******************")
        return 0

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("  Banking Program  ")
        print("*******************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        print("*******************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*******************")
            print("Invalid choice. Please try again.")
            print("*******************")

    print("*******************")
    print("Thank you for using our banking program.")
    print("*******************")

if __name__ == "__main__":
    main()