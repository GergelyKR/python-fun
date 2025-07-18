# balance = 0
# 
# def main():
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)
# 
# def deposit(n):
#     global balance # reference the global variable
#     balance += n
# 
# def withdraw(n):
#     global balance
#     balance -= n
# 
# if __name__ == "__main__":
#     main()

class Account:
    def __init__(self):
        self._balance = 0

    @property   # protected instance variable, controlled read / write. Can't modify without setter.
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()