# ===== ATM System =====

pin = "1234"
balance = 10000

print("===== Welcome to Python ATM =====")

user_pin = input("Enter Your 4-Digit PIN: ")

if user_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter Your Choice (1-4): ")

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter Deposit Amount: "))
            if amount > 0:
                balance += amount
                print("Deposit Successful!")
                print("New Balance:", balance)
            else:
                print("Invalid Amount!")

        elif choice == "3":
            amount = float(input("Enter Withdraw Amount: "))
            if amount <= balance and amount > 0:
                balance -= amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                print("Invalid Amount!")

        elif choice == "4":
            print("Thank You for Using Python ATM!")
            break

        else:
            print("Invalid Choice! Please Try Again.")

else:
    print("Incorrect PIN! Access Denied.")
