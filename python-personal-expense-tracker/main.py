#Day 1 coding challenge
name = input("Enter your name: ")
salary = float(input("Enter your Monthly Salary: "))
food = float(input("Enter your Food Expenses: "))
transportation = float(input("Enter your transportation Expenses: "))
total_expense = food + transportation
remain = salary - total_expense

print(f"My name is {name}.")
print(f"My salary is {salary:.2f}.")
print(f"My food expense is {food:.2f}.")
print(f"My tp is {transportation:.2f}.")
print(f"My Total Expense is {total_expense:.2f}.")
print(f"My Remaining Balance is {remain:.2f}.")

if remain < 0:
    print("Warning: You are over budget!")
elif remain > 0:
    print("You have money remaining.")
elif remain == 0:
    print("You have used your entire budget.")


while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Income feature coming soon.")

    elif choice == "2":
        print("Expense feature coming soon.")

    elif choice == "3":
        print("Balance feature coming soon.")  

    elif choice == "4":
            print("Exiting...")       
            break
    else:
        print("Your Input is invalid")


    