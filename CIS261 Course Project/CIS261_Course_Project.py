# Name: Simone Chance
# Course: CIS261
# Lab Title: Course Project

import re

# Function to get dates
def get_dates():
    """Input and return the from date and to date with validation."""
    date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
                
    while True:
        from_date = input("Enter from date (mm/dd/yyyy): ")
        if not date_pattern.match(from_date):
            print("Invalid format. Please enter date as mm/dd/yyyy.")
            continue
                                                                        
        to_date = input("Enter to date (mm/dd/yyyy): ")
        if not date_pattern.match(to_date):
            print("Invalid format. Please enter date as mm/dd/yyyy.")
            continue
                                                                                                                
        return from_date, to_date

# Function to get employee name
def get_employee_name():
    """Input and return the employee's name."""
    name = input("Enter employee's name (or type 'End' to finish): ")
    return name

# Function to get total hours worked
def get_total_hours():
    """Input and return the total hours worked."""
    while True:
        try:
           hours = float(input("Enter total hours worked: "))
           return hours
        except ValueError:
           print("Please enter a valid number.")

# Function to get hourly rate
def get_hourly_rate():
    """Input and return the hourly rate."""
    while True:
        try:
           rate = float(input("Enter hourly rate: "))
           return rate
        except ValueError:
           print("Please enter a valid number.")

# Function to get income tax rate
def get_income_tax_rate():
    """Input and return the income tax rate."""
    while True:
        try:
           tax_rate = float(input("Enter income tax rate (as a percentage): "))
           return tax_rate / 100  # Convert to decimal
        except ValueError:
           print("Please enter a valid number.")

# Function to calculate payroll: gross pay, income tax, and net pay
def calculate_pay(total_hours, hourly_rate, tax_rate):
    """Calculate and return gross pay, income tax, and net pay."""
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Function to display employee details
def display_employee_info(employee):
    """Display employee details."""
    print(f"\nEmployee Name: {employee['employee_name']}")
    print(f"From Date: {employee['from_date']}, To Date: {employee['to_date']}")
    print(f"Total Hours: {employee['total_hours']}")
    print(f"Hourly Rate: ${employee['hourly_rate']:.2f}")
    print(f"Gross Pay: ${employee['gross_pay']:.2f}")
    print(f"Income Tax Rate: {employee['income_tax_rate'] * 100:.2f}%")
    print(f"Income Tax: ${employee['income_tax']:.2f}")
    print(f"Net Pay: ${employee['net_pay']:.2f}\n")

# Function to display the totals
def display_totals(totals):
    """Display summary of all employees."""
    print("\nSummary:")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours: {totals['total_hours']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")
    print(f"Total Tax: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}\n")

# Main function to execute the program
def main():
    """Main function to execute the program."""
    employees = []  # List to hold employee data
    totals = {
        'total_employees': 0,
        'total_hours': 0,
        'total_gross_pay': 0,
        'total_tax': 0,
        'total_net_pay': 0
    }

    while True:
        # Get employee details
        employee_name = get_employee_name()
        if employee_name.lower() == 'end':
            break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        from_date, to_date = get_dates()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        # Calculate pay
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        # Store employee data in a dictionary
        employee = {
            'from_date': from_date,
            'to_date': to_date,
            'employee_name': employee_name,
            'total_hours': hours,
            'hourly_rate': rate,
            'income_tax_rate': tax_rate,
            'gross_pay': gross_pay,
            'income_tax': income_tax,
            'net_pay': net_pay
        }

        employees.append(employee)  # Add employee to the list
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        # Display employee info
        display_employee_info(employee)

        # Update totals
        totals['total_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross_pay'] += gross_pay
        totals['total_tax'] += income_tax
        totals['total_net_pay'] += net_pay

    # Display totals after the loop
    display_totals(totals)

if __name__ == "__main__":
    main()

 