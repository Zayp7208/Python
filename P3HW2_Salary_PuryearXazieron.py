 # CTI-110

   # P3HW2 - Salary

   # Xazieron Puryear

   # 12/14/23

   #



   # Get employee details
employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours the employee worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Check for overtime and calculate pay accordingly
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    regular_hours = hours_worked
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
    gross_pay = regular_pay

# Display employee's pay details
print("\nEmployee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Number of Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)
