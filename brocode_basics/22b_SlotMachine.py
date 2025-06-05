# Python Slot Machine

import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    # results = []
    # for symbol in range(3):
    #    results.append(random.choice(symbols))
    # return results

    return [random.choice(symbols) for _ in range(3)] # for every iteration in range(3), return a random symbol

def print_row(row):
    print("+--+----+---+")
    print(" | ".join(row)) # take iterable and join each element with some characters
    print("+--+----+---+")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100

    print("*******************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("*******************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue # skips current iteration of the loop and restarts it

        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout
        else:
            print("You lost.")

        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print(f"Final balance: ${balance}")

    print("*******************")
    print("Thanks for playing!")
    print("*******************")

if __name__ == '__main__':
    main()