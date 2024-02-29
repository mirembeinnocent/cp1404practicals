
def main():
    """Calculate and display the monthly cumulative totals for incomes."""
    incomes = get_monthly_incomes()
    print_income_report(incomes)


def get_monthly_incomes():
    """Get monthly incomes from user input and return a list."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    return incomes


def print_income_report(incomes):
    """Print income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
