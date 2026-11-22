print("===== PERSONAL EXPENSE TRACKER =====")

income = float(input("Enter your total income: "))
food = float(input("Enter your food expenses: "))
transport = float(input("Enter your transport expenses: "))
education = float(input("Enter your education expenses: "))
other = float(input("Enter your other expenses: "))

total_expenses = food + transport + education + other
remaining_balance = income - total_expenses

print("\n===== EXPENSE SUMMARY =====")
print("Total income:", income)
print("Total expenses:", total_expenses)
print("Remaining balance:", remaining_balance)