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

# --- Simulation Loop ---
my_atm = ATM(pin="1234", balance=1000)

print("--- Welcome to Python Bank ATM ---")
tries = 3
authenticated = False

while tries > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if my_atm.check_pin(entered_pin):
        authenticated = True
        break
    else:
        tries -= 1
        print(f"❌ Incorrect PIN. {tries} attempts left.")

if authenticated:
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transaction History\n5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            print(f"💰 Current Balance: ${my_atm.balance}")
        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            my_atm.deposit(amt)
        elif choice == "3":
            amt = float(input("Enter withdrawal amount: "))
            my_atm.withdraw(amt)
        elif choice == "4":
            print("\n--- History ---")
            for item in my_atm.transaction_history:
                print(item)
        elif choice == "5":
            print("Goodbye! 👋")
            break
else:
    print("Locked out. Please contact support.")