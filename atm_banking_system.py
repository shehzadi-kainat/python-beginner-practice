balance = 10000
transactions = []

while True:

    print("\n===== ATM BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: Rs. {amount}")
            print("Money deposited successfully!")
        else:
            print("Invalid deposit amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            balance -= amount
            transactions.append(f"Withdrawn: Rs. {amount}")
            print("Withdrawal successful!")

    elif choice == "4":

        if len(transactions) == 0:
            print("No transactions yet.")

        else:
            print("\nTransaction History:")

            for transaction in transactions:
                print(transaction)

    elif choice == "5":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice! Please try again.")