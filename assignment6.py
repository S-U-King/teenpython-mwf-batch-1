pin = "5654"
balance = 150000

print("Welcome the Zain Bank ATM")
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin:
    print("Incorrect PIN. Access Blocked.")
else:
    print("\n--- Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    
    choice = input("\nEnter choice (1-4): ")
 
    if choice == "1":
        print(f"Your current balance is: Rs. {balance}")
   
    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount <= 0:
            print("Invalid amount. Deposit must be greater than 0.")
        else:
            balance += deposit_amount
            print(f"Successfully deposited Rs. {deposit_amount}")
            print(f"New balance: Rs. {balance}")
    
    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= 0:
            print("Invalid amount. Withdrawal must be greater than 0.")
        elif withdraw_amount > balance:
            print("Insufficient Balance")
        else:
            balance -= withdraw_amount
            print(f"Successfully withdrew Rs. {withdraw_amount}")
            print(f"Remaining balance: Rs. {balance}")
    
    elif choice == "4":
        old_pin = input("Enter your old PIN: ")
        if old_pin != pin:
            print("Verification failed. Old PIN does not match.")
        else:
            new_pin = input("Enter your new 4-digit PIN: ")
            if new_pin == pin:
                print("Error: New PIN cannot be the same as the old PIN.")
            elif len(new_pin) != 4 or not new_pin.isdigit():
                print("Error: PIN must be exactly 4 digits.")
            else:
                pin = new_pin
                print("PIN changed successfully!")
     
    else:
        print("Error: Invalid option selected.")
