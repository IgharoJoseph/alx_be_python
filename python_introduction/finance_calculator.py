monthly_income = input("Enter your monthly income:")
total_monthly_expense = input("Enter your monthly total expense:")

monthly_savings =  float(monthly_income) - float(total_monthly_expense)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")