import sys


def get_requirements():
    print("Developer: Ayansewa Adedeji")
    print("Compound Interest Investment Report Program\n")

    print("Program Requirements:")
    print("1. Write a program that prints a yearly compound interest report table.")
    print("2. Must perform data validation.")
    print("3. Must support yearly, quarterly, monthly, and daily compounding.\n")


def menu():

    print("\nMENU:")
    print("y=Yearly")
    print("q=Quarterly")
    print("m=Monthly")
    print("d=Daily")
    print("e=Exit")

    command = input("\nEnter command: ").lower()

    return command


def run_calculation(command):

    n = get_period(command)

    principal = get_principal()
    rate = get_rate()
    years = get_years()

    print_report(principal, rate, years, n)


def get_period(command):

    if command == "y":
        return 1
    elif command == "q":
        return 4
    elif command == "m":
        return 12
    elif command == "d":
        return 365
    else:
        print("Invalid command")
        return 1


def get_principal():

    while True:
        try:
            p = float(input("Enter principal: $"))
            if p <= 0:
                print("Principal must be positive.")
            else:
                return p
        except ValueError:
            print("Not a float! Try again.")


def get_rate():

    while True:
        try:
            r = float(input("Enter rate (%): "))
            if r <= 0 or r > 100:
                print("Rate must be between 1 and 100.")
            else:
                return r / 100
        except ValueError:
            print("Not a float! Try again.")


def get_years():

    while True:
        try:
            y = int(input("Enter years: "))
            if y <= 0:
                print("Years must be positive.")
            else:
                return y
        except ValueError:
            print("Not an int! Try again.")


def print_report(principal, rate, years, n):

    print("\nYear\tStarting\tInterest\tEnding")

    balance = principal
    total_interest = 0

    for year in range(1, years + 1):

        start = balance

        balance = balance * (1 + rate / n) ** n

        interest = balance - start

        total_interest += interest

        print(f"{year}\t{start:,.2f}\t\t{interest:,.2f}\t\t{balance:,.2f}")

    print(f"\nEnding principal: ${balance:,.2f}")
    print(f"Total interest earned: ${total_interest:,.2f}")