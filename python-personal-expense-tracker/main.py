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
elif remain = 0:
    print("You have used your entire budget.")


