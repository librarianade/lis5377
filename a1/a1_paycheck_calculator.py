# Paycheck Calculator
# Developer: Ayansewa Adedeji

print("Paycheck Calculator")
print("Developer: Ayansewa Adedeji")
print("Program calculates net pay based upon hours worked, hourly rate, and taxes paid.\n")

hours_worked = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Rate: $"))
tax_rate = float(input("Tax Rate (percent): "))

gross_pay = hours_worked * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount

print("\nProgram Output:")
print(f"Gross Pay: ${gross_pay:,.2f}")
print(f"Tax Rate: {tax_rate:.2f}%")
print(f"Tax Amount: ${tax_amount:,.2f}")
print(f"Net Pay: ${net_pay:,.2f}")
