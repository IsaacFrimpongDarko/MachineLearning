import random

#My details
print("Nam: Isaac Frimpong Darko \nRef: UA2401546")


#ATM Welcome notes
print("\nWelcome to Darko Development Bank\n\nInsert your ATM card\n")


#A hint on password
print("Your password is any random four digits between 1 - 9 \n")

#some
choice = 0
bing = "https://www.bing.com/"
call = 233257297111
balance = 100
attempts = 3  
name = input("Enter your name: ")
transactions = []

# PIN entry with up to 3 attempts
while attempts > 0:
    pin = int(input("Enter your four digit PIN: "))
    
    if 1000 <= pin <= 9999:
        print("\nPIN accepted.\nWelcome,", name, "!")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.\n")
    
    if attempts == 0:
        print("Card failed. Please contact customer service for assistance.")
        quit()  

# ATM Menu (only accessible if PIN is correct)
while choice != 6:
    print("\n"" ATM Menu """)
    print("1: Check Balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Help")
    print("5: Print statement")
    print("6: Exit\n")

    choice = int(input("Select : "))

    if choice == 1:
        # Balance Check
        print("\n"" ATM Balance Menu """)
        print(f"Hello {name}, your current balance is Ghs {balance}")
        while True:
            back_choice = int(input("\nPress 0 to return to the main menu: "))
            if back_choice == 0:
                break
            else:
                print("Invalid input. Please press 0 to return to the main menu.")
                transactions.append({"type": "Balace", "amount": balance, "balance": balance})
                
    elif choice == 2:
        # Deposit Funds
        print("\n"" ATM Deposit Menu """)
        Dep = int(input("Enter your deposit amount: Ghs"))
        balance += Dep
        print("\nDeposited amount: Ghs", Dep)
        print("New Balance = Ghs", balance)
        while True:
            back_choice = int(input("\nPress 0 to return to the main menu: "))
            if back_choice == 0:
                break
            else:
                print("Invalid input. Please press 0 to return to the main menu.")
        transactions.append({"type": "Deposit", "amount": Dep, "balance": balance})
                
    elif choice == 3:
        # Withdraw Funds
        print("\n"" ATM Withdrawal Menu """)
        Wit = int(input("Enter amount: Ghs"))
        if Wit > balance:
            print("Insufficient balance")
        else:
            balance -= Wit
            print(f"\nWithdrawn amount: Ghs {Wit}")
            print(f"New Balance = Ghs {balance}")
        while True:
            back_choice = int(input("\nPress 0 to return to the main menu: "))
            if back_choice == 0:
                break
            else:
                print("Invalid input. Please press 0 to return to the main menu.")
        transactions.append({"type": "Withdrawal", "amount": Wit , "balance": balance})
                
    elif choice == 4:
        # Help Menu
        print("\n"" ATM Help Menu """)
        print(f"For assistance, please call us at {call}.")
        print(f"Or visit our website at: {bing}\n")
        while True:
            back_choice = int(input("Press 0 to return to the main menu: "))
            if back_choice == 0:
                break
            else:
                print("Invalid input. Please press 0 to return to the main menu.")

    elif choice == 5:
        # Transaction Statement
        print("\n""Transaction Statement """)
        if transactions:
            print("Type       |Amount | Balance")
            print("-------------------------------")
            for trans in transactions:
                print(f"{trans['type']:12} | Ghs {trans['amount']:6} | Ghs {trans['balance']}")
        else:
            print("No transactions available.")
        print("\nEnd of statement.")
        while True:
            back_choice = int(input("\nPress 0 to return to the main menu: "))
            if back_choice == 0:
                break
            else:
                print("Invalid input. Please press 0 to return to the main menu.")
                
    elif choice == 6:
        # Exit
        print("\nTransaction cancelled. Thank you for using Darko Development Bank.")
        print("\nPlease take your card.")
        quit()
    
    else:
        # Invalid menu selection
        print("\nInvalid selection. Please choose a valid option from 1 to 6.\n")
