#Class setup for the ATM system

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds!")
        elif amount <= 0:
            print("❌ Invalid amount.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"✅ Successfully withdrew ${amount}. New balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"✅ Successfully deposited ${amount}. New balance: ${self.balance}")
        else:
            print("❌ Invalid deposit amount.")