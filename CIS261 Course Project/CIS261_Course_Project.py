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

# Function to save employee data to file in pipe-delimited format
def save_employee_to_file(file_name, employee):
    """Save the employee data to a text file in a pipe-delimited format."""
    with open(file_name, 'a') as file:    # 'a' to append data to the file 
        record = f"{employee['from_date']}|{employee['to_date']}|{employee['employee_name']}|{employee['total_hours']}|{employee['hourly_rate']}|{employee['income_tax_rate']}\n"
        file.write(f"{employee['from_date']}|{employee['to_date']}|{employee['employee_name']}|{employee['total_hours']}|{employee['hourly_rate']}|{employee['income_tax_rate']}\n")

# Function to get the from date input for filtering records
def get_from_date_input():
    """Get the from date input for filtering records."""
    while True:
        from_date = input("Enter From Date (mm/dd/yyyy) or 'All' to display all records: ").strip()
        if from_date.lower() == 'all' or re.match(r"\d{2}/\d{2}/\d{4}", from_date):
            return from_date
        else:
            print("Invalid date format. Please enter mm/dd/yyyy or 'All'.")

# Function to process records from the file based on the entered from date
def process_records(file_name, from_date):
    """Process the employee records based on the from date."""
    totals = {
        'total_employees': 0,
        'total_hours': 0,
        'total_gross_pay': 0,
        'total_tax': 0,
        'total_net_pay': 0
    }

    with open(file_name, 'r') as file:
        for line in file:
            # Parse the record
            record = line.strip().split('|')
            record_from_date = record[0]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            # If "All" or matching from date, process the record
            if from_date == 'All' or record_from_date == from_date:
                # Extract the employee data from the record
                employee_name = record[2]
                hours = float(record[3])
                rate = float(record[4])
                tax_rate = float(record[5])

                # Calculate payroll
                gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

                # Display employee info
                print(f"\nEmployee: {employee_name}, From Date: {record_from_date}")
                print(f"Total Hours: {hours}, Hourly Rate: ${rate:.2f}, Gross Pay: ${gross_pay:.2f}, Income Tax: ${income_tax:.2f}, Net Pay: ${net_pay:.2f}")
                
                # Update totals
                totals['total_employees'] += 1 
                totals['total_hours'] += hours
                totals['total_gross_pay'] += gross_pay
                totals['total_tax'] += income_tax
                totals['total_net_pay'] += net_pay

    # Display totals
    if totals['total_employees'] > 0:  # Only display if there are any records
        display_totals(totals)
    else:
        print("No records found for the given From Date or 'All'.")
        
# Main function to execute the program
def main():
    """Main function to execute the program."""
    employees = []  # List to hold employee data
    file_name = "employee_data.txt" # Text file to store employee 
    
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        # Save employee data to file
        save_employee_to_file(file_name, employee)

        # Display employee info
        display_employee_info(employee)

    # After data entry, get From Date input and process the records
    from_date_input = input("Enter the From Date (mm/dd/yyyy) to filter by or type 'All' to see all records: ") 
    process_records(file_name, from_date_input)  # Process and display records based on from date

if __name__ == "__main__":
    main()
    