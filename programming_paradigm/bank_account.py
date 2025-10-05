import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")


def main():
    account = BankAccount(100)  # Initial balance

    if len(sys.argv) != 2:
        print("Invalid command.")
        return

    command = sys.argv[1]

    # Deposit
    if command.startswith("deposit:"):
        try:
            amount = float(command.split(":")[1])
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        except:
            print("Invalid command.")

    # Withdraw
    elif command.startswith("withdraw:"):
        try:
            amount = float(command.split(":")[1])
            if account.withdraw(amount):
                print(f'Withdrew: ${amount}')
            else:
                print("Insufficient funds.")
        except:
            print("Invalid command.")

    # Display
    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
