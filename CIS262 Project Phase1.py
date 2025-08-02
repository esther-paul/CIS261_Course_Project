# ********************************************************
# Name: Esther Paul
# Class: CIS 261
# Lab: Employee Payroll System
# Date: August 1, 2025
# ********************************************************

def get_input(prompt, min_val=0, max_val=float('inf')):
    """Get and validate numeric input from user"""
    # TODO: Implement input validation
    # Hint: Use try/except for number I'mconversion
    # Return the validated number
    pass

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, tax amount, and in net pay"""
    # TODO: Calculate gross_pay (hours * rate)
    # TODO: Calculate tax (gross_pay * tax_rate)
    # TODO: Calculate net_pay (gross_pay - tax)
    # Return all three values
    pass

def display_employee(name, hours, rate, gross, tax_rate, tax, net):
    """Display information for a single employee"""
    # TODO: Print employee details
    # Format numbers to 2 decimal places
    pass

def display_totals(emps, hours, gross, tax, net):
    """Display summary totals"""
    # TODO: Print summary statistics
    # Format numbers to 2 decimal places
    pass

def main():
    # Initialize accumulators for totals
    total_emps = total_hours = total_gross = total_tax = total_net = 0
    
    # TODO: Implement main program loop
    # Get employee name (exit if "End")
    # Get hours, rate, and tax rate
    # Calculate pay
    # Display employee info
    # Update totals
    # Display final totals if any employees were processed

if __name__ == "__main__":
    main()
