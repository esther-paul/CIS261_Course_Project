# ********************************************************
# Name: Esther Paul
# Class: CIS 261
# Lab: Employee Payroll System
# Date: August 1, 2025
# ********************************************************

def get_input(prompt, min_val=0, max_val=float('inf')):
    """Get and validate numeric input from user"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Input must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, tax amount, and net pay"""
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def display_employee(name, hours, rate, gross, tax_rate, tax, net):
    """Display information for a single employee"""
    print("\n======= Employee Information =======")
    print(f"Employee Name   : {name}")
    print(f"Hours Worked    : {hours}")
    print(f"Hourly Rate     : ${rate:.2f}")
    print(f"Gross Pay       : ${gross:.2f}")
    print(f"Tax Rate        : {tax_rate:.2%}")
    print(f"Tax Deducted    : ${tax:.2f}")
    print(f"Net Pay         : ${net:.2f}")
    print("====================================\n")

def display_totals(emps, hours, gross, tax, net):
    """Display summary totals"""
    print("\n========= Payroll Summary =========")
    print(f"Total Employees : {emps}")
    print(f"Total Hours     : {hours}")
    print(f"Total Gross Pay : ${gross:.2f}")
    print(f"Total Tax       : ${tax:.2f}")
    print(f"Total Net Pay   : ${net:.2f}")
    print("===================================\n")

def main():
    # Initialize accumulators for totals
    total_emps = 0
    total_hours = 0
    total_gross = 0
    total_tax = 0
    total_net = 0

    while True:
        name = input("Enter employee name (or type 'End' to finish): ")
        if name.lower() == "end":
            break

        hours = get_input("Enter number of hours worked: ", 0)
        rate = get_input("Enter hourly rate: ", 0)
        tax_rate = get_input("Enter income tax rate (as a decimal): ", 0, 1)

        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        display_employee(name, hours, rate, gross, tax_rate, tax, net)

        total_emps += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

    if total_emps > 0:
        display_totals(total_emps, total_hours, total_gross, total_tax, total_net)
    else:
        print("No employee data entered.")

if __name__ == "__main__":
    main()
