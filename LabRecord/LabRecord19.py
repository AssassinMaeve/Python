class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance!")
        self.balance -= amount
        print(f"Withdrawn: {amount}, New Balance: {self.balance}")

# Example usage
account = BankAccount(1000)
account.deposit(500)
try:
    account.withdraw(2000)
except Exception as e:
    print("Error:", e)
account.withdraw(300)