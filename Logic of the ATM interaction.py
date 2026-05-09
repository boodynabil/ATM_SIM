"""Logic of the ATM interaction simulation. This code is not meant to be run as-is, 
but rather serves as a template for how the ATM class can be used in a simulation loop.
"""
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

