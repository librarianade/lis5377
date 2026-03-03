"""Defines program functions."""
    

def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Ayansewa Adedeji")
    print("Annual Compound Interest Investment Report.\n")

    print("Program Requirements:\n"
          + "1. Write a program that prints a yearly compound interest report table.\n"
          + "2. Must perform data validation.\n")

    print("***Resource(s):***\n"
          + "https://www.fool.com/saving/how-often-is-interest-accrued-on-a-savings-account.aspx\n"
          + "https://www.nerdwallet.com/article/banking/how-to-calculate-interest-in-a-savings-account\n"
          + "Verify calculation: https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator\n")

    print("Input:")


def get_principal():
    """Accepts 0 args. Prompts for principal amount, returns validated value."""
    while True:
        try:
            principal = float(input("Enter principal: $"))
            if principal >= 1 and principal <= 1000000:
                return principal
            else:
                print("Principal must be between $1 and $1,000,000.\n")
        except ValueError:
            print("Not a float! Try again.\n")


def get_rate():
    """Accepts 0 args. Prompts for interest rate, returns validated value."""
    while True:
        try:
            rate = float(input("Enter rate (%): "))
            if rate >= 1 and rate <= 10:
                return rate
            else:
                print("Rate must be between 1% and 10% (no percent sign!).\n")
        except ValueError:
            print("Not a float! Try again.\n")


def get_years():
    """Accepts 0 args. Prompts for number of years, returns validated value."""
    while True:
        try:
            years = int(input("Enter years: "))
            if years >= 1 and years <= 50:
                return years
            else:
                print("Years must be between 1 and 50.\n")
        except ValueError:
            print("Not an int! Try again.\n")


def calculate_interest(principal, rate, years):
    """Accepts principal, rate, years. Prints yearly compound interest table."""
    
    total_interest = 0.0
    rate = rate / 100  # convert percent to decimal

    print()
    print("{:<6} {:>12} {:>12} {:>12}".format("Year", "Starting", "Interest", "Ending"))

    for year in range(1, years + 1):
        interest = principal * rate
        end_principal = principal + interest

        print("{:<6} {:>12.2f} {:>12.2f} {:>12.2f}".format(
            year, principal, interest, end_principal))

        principal = end_principal
        total_interest += interest

    print("\nEnding principal: ${:,.2f}".format(principal))
    print("Total interest earned: ${:,.2f}".format(total_interest))