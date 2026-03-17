expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Travel/Shopping/Other): ")

        expenses.append({"amount": amount, "category": category})
        print("Expense Added Successfully!")

    elif choice == "2":
        print("\nYour Expenses:")
        for e in expenses:
            print(e["category"], "-", e["amount"])

    elif choice == "3":
        total = sum(e["amount"] for e in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")