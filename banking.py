"""
We have covered core python, now it's time to test your coding and logical skills, also to know how confident you are with the syntax,
i'm giving you a small project:
Write a python program to replicate a Banking system. The following features are mandatory:
1. Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also.
"""
class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def main():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    bank_account = BankAccount(account_number, pin)

    print("Welcome to the banking system!")
    login_success = False
    while not login_success:
        entered_pin = input("Enter PIN to login: ")
        try:
            if entered_pin == bank_account.pin:
                print("Login successful!")
                login_success = True
            else:
                raise ValueError("Invalid PIN. Please try again.")
        except ValueError as e:
            print(e)

    while True:
        print("\nBanking Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        try:
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                bank_account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                bank_account.withdraw(amount)
            elif choice == '3':
                bank_account.check_balance()
            elif choice == '4':
                print("Thank you for using the banking system. Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please enter a valid option.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()