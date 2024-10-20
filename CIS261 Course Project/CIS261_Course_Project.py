# Name: Simone Chance
# Course: CIS261
# Lab Title: Course Project
def get_employee_name():
    """Input and return the employee's name."""
    name = input("Enter employee's name (or type 'End' to finish): ")
    return name

def get_total_hours():
    """Input and return the total hours worked."""
    while True:
        try:
            hours = float(input("Enter total hours worked: "))
            return hours
        except ValueError:
            print("Please enter a valid number.")

def get_hourly_rate():
    """Input and return the hourly rate."""
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            return rate
        except ValueError:
            print("Please enter a valid number.")

def get_income_tax_rate():
    """Input and return the income tax rate."""
    while True:
        try:
            tax_rate = float(input("Enter income tax rate (as a percentage): "))
            return tax_rate / 100  # Convert to decimal
        except ValueError:
            print("Please enter a valid number.")

def calculate_pay(total_hours, hourly_rate, tax_rate):
    """Calculate and return gross pay, income tax, and net pay."""
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    """Display employee details."""
    print(f"\nEmployee Name: {name}")
    print(f"Total Hours: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate * 100:.2f}%")
    print(f"Income Tax: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

def display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    """Display summary of all employees."""
    print("\nSummary:")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours: {total_hours}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net_pay:.2f}\n")

def main():
    """Main function to execute the program."""
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_tax = 0
    total_net_pay = 0

    while True:
        employee_name = get_employee_name()
        if employee_name.lower() == 'end':
            break
        
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()
        
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
        
        display_employee_info(employee_name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

        # Update totals
        total_employees += 1
        total_hours += hours
        total_gross_pay += gross_pay
        total_tax += income_tax
        total_net_pay += net_pay

    # Display totals after the loop
    display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)

if __name__ == "__main__":
    main()

