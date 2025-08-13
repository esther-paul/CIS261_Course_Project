# Esther Paul
# CIS261
# CIS261 Project Phase 3
# August 13, 2025

from datetime import datetime

def GetEmpName():
    empname = input("Enter employee name (or END to Stop): ")
    return empname

def GetDatesWorked():    
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate (e.g., 0.2 for 20%): "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpTotals = {}

    ###################################################################
    # write the line of code to open Employees.txt file in read mode and assign to EmpFile

    with open('Employees.txt', 'r') as EmpFile:

        # Get the date filter from the user
        while True:
            rundate_str = input("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
            if rundate_str.upper() == "ALL":
                rundate = None  
                break
            try:
                rundate = datetime.strptime(rundate_str, "%m/%d/%Y")
                break
            except ValueError:
                print("Invalid date format. Try again.\n")

        while True:
            # write the line of code to read a record from EmpFile and assign it to EmpDetail
            EmpDetail = EmpFile.readline()

            if not EmpDetail:
                break

            #write the line of code to remove the carriage return from the end of the record read from the file
            EmpDetail = EmpDetail.strip()
            #write the line of code to split the record read in on the pipe delimiter and assign it to EmpList
            EmpList = EmpDetail.split("|")

            fromdate = EmpList[0]

            # Filtering logic only if a specific date was entered
            if rundate is not None:
                checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
                if checkdate < rundate:
                    continue

        ######################################################################

            todate = EmpList[1]
            empname = EmpList[2]
            hours = float(EmpList[3])
            hourlyrate = float(EmpList[4])
            taxrate = float(EmpList[5])
            grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)

            print(fromdate, todate, empname,
                  f"{hours:,.2f}", f"{hourlyrate:,.2f}",
                  f"{grosspay:,.2f}", f"{taxrate:,.1%}",
                  f"{incometax:,.2f}", f"{netpay:,.2f}")

            TotEmployees += 1
            TotHours += hours
            TotGrossPay += grosspay
            TotTax += incometax
            TotNetPay += netpay

            EmpTotals["TotEmp"] = TotEmployees
            EmpTotals["TotHrs"] = TotHours
            EmpTotals["TotGrossPay"] = TotGrossPay
            EmpTotals["TotTax"] = TotTax
            EmpTotals["TotNetPay"] = TotNetPay
            DetailsPrinted = True

    if DetailsPrinted:
        PrintTotals(EmpTotals)
    else:
        print("No detail information to print")

def PrintTotals(EmpTotals):
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')

if __name__ == "__main__":
    # write the line of code to open a file Employees.txt in append mode and assign it to EmpFile
    with open('Employees.txt', 'a') as EmpFile:
        EmpTotals = {}
        DetailsPrinted = False
        while True:
            empname = GetEmpName()
            if empname.upper() == "END":
                break
            fromdate, todate = GetDatesWorked()
            hours = GetHoursWorked()
            hourlyrate = GetHourlyRate()
            taxrate = GetTaxRate()

            ##############################################################
            # write the line of code that will concatenate fromdate, todate, empname, hours, hourlyrate, and taxrate. Pipe delimit each value and add a carriage return to the end of the line
            # and assign the line to EmpDetail

            EmpDetail = f"{fromdate}|{todate}|{empname}|{hours}|{hourlyrate}|{taxrate}\n"
            EmpFile.write(EmpDetail)

     # write the line of code to close EmpFile
    printinfo(DetailsPrinted)
    ####################################################################
