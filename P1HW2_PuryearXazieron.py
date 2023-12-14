# Date
# CTI-110 P1HW2 - Travel Expense
# Xazieron Puryear




budget = float(input("Enter your budget for the trip: $"))

destination = input("Enter your travel destination: ")

gas_expense = float(input("Enter the amount you will spend on gas: $"))

accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

food_expense = float(input("Enter the amount you will spend on food: $"))

total_expenses = gas_expense + accommodation_expense + food_expense

remaining_budget = budget - total_expenses

print("----Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas_expense)
print("Accommodation:", accommodation_expense)
print("Food:", food_expense)
print("\nTravel Expense Summary")
print("Remaining Budget: $", remaining_budget)
