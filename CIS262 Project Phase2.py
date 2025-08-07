# ********************************************************
# Name: Esther Paul
# Class: CIS 261
# Lab: Course Project Phase 2
# Date: August 7, 2025
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

def get_dates():
    while True:
        from_date=input("Enter the FROM date (mm/dd/yyyy) : ")
        to_date=input("Enter the TO date (mm/dd/yyyy) : ")
        if len(from_date)==10 and len(to_date)==10:
            return from_date, to_date
        else:
            print("Please ensure all dates formats are correct!! mm/dd/yyyy")

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, tax amount, and net pay"""
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def display_employee(name, from_date, to_date,hours, rate, gross, tax_rate,tax,net):
    """Display information for a single employee"""
    print("\n======= Employee Information =======")
    print(f"Employee Name   : {name}")
    print(f"From Date       : {from_date}")
    print(f"To Date         : {to_date}")
    print(f"Hours Worked    : {hours}")
    print(f"Hourly Rate     : ${rate:.2f}")
    print(f"Gross Pay       : ${gross:.2f}")
    print(f"Income Tax Rate : {tax_rate:.2%}")
    print(f"Net Pay         : ${net:.2f}")
    print("====================================\n")
def process_employees(employee_data_list):
    """
    Process each employee, calculate pay and track totals
    """
    totals={
        "emps": 0,
        "hours" :0,
        "gross": 0,
        "tax" :0,
        "net" :0
    }

    for emp in employee_data_list:
        name, from_date, to_date, hours, rate, tax_rate=emp
        gross, tax, net =calculate_pay(hours, rate, tax_rate)

        totals['emps']+=1
        totals['hours']+=hours
        totals['gross']+=gross
        totals['tax']+=tax
        totals['net']+=net
    return totals

def display_totals(totals_dict):
    """Display summary totals"""
    print("\n========= Payroll Summary =========")
    print(f"Total Employees : {totals_dict['emps']}")
    print(f"Total Hours     : {totals_dict['hours']}")
    print(f"Total Gross Pay : ${totals_dict['gross']:.2f}")
    print(f"Total Tax       : ${totals_dict['tax']:.2f}")
    print(f"Total Net Pay   : ${totals_dict['net']:.2f}")
    print("===================================\n")

def main():
    employee_data=[]

    while True:
        name = input("Enter employee name (or type 'End' to finish): ")
        if name.lower() == "end":
            break

        from_date, to_date= get_date()
        hours = get_input("Enter number of hours worked: ", 0)
        rate = get_input("Enter hourly rate: ", 0)
        tax_rate = get_input("Enter income tax rate (as a decimal): ", 0, 1)

        employee_data.append((name, from_date, to_date, rate, tax_rate))

    if employee_data:
        totals=process_employees(employee_data)
        display_totals(totals)
    else:
        print("No employee data entered.")

if __name__ == "__main__":
    main()
