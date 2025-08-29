# Esther Paul
# CIS261 Project Phase 4 -  User Management Application
# August 29, 2025

# necessary libraries
import os
from datetime import datetime

################################################################################
# CLASS LOGIN
class Login:
    def __init__(self, user_id="", password="", authorization=""):
        self.username = user_id
        self.password = password
        self.role = authorization

    def __str__(self):
        return f"{self.username}|{self.password}|{self.role}"

    def display_info(self):
        print(f"\nUser Information:")
        print(f"User ID: {self.username}")
        print(f"Password: {'*' * len(self.password)}") # Masking password for security
        print(f"Authorization: {self.role}")

    def is_admin(self):
        return self.role.lower() == "admin"

################################################################################
# USER MANAGEMENT FUNCTIONS
def main_user_management():
    print('##### Create users, passwords, and roles #####')
    # if no user has bn selected
    if not os.path.exists("Users.txt"):
        open("Users.txt", "w").close()
    # Opening the file Users.txt in append mode
    UserFile = open("Users.txt", "a+")
    UserFile.seek(0)
    existing_users = []

    for line in UserFile:
        parts = line.strip().split("|")
        if len(parts) >= 1:
            existing_users.append(parts[0])

    while True:
        # calling function GetUserName and assigning the return value to username
        username = GetUserName()
        if (username.upper() == "END"):
            break

        if username in existing_users:
            print("User ID already exists, please enter a different username.")
            continue
        # Calling function GetUserPassword and assigning the return value to userpwd
        userpwd = GetUserPassword()
        # calling function GetUserRole() and assigning the return value to userrole
        userrole = GetUserRole()

        # An instance of the LogIn class
        user = Login(username, userpwd, userrole)
        UserFile.write(str(user) + "\n")
        existing_users.append(username)

    # Closing the file UserFile
    UserFile.close()    

def GetUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd

def GetUserRole():
     userrole = input("Enter role (Admin or User): ")
     while True:       
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ") 

def printuserinfo():
    if not os.path.exists("Users.txt") or os.path.getsize("Users.txt") == 0:
        print("No users found.")
        return

    with open("Users.txt","r") as UserFile:
        for line in UserFile:
            UserDetail = line.strip()
            if not UserDetail:
                continue
            UserList = UserDetail.split("|")
            if len(UserList) == 3:
                username, userpassword, userrole = UserList
                user = Login(username, userpassword, userrole)
                # displaying user information while masking user's password
                user.display_info()  

################################################################################
# LOGIN FUNCTION
def login_process():
    # if no user has been registered
    if not os.path.exists("Users.txt"):
        open("Users.txt", "w").close()

    while True:
        # opening file Users.txt in read mode
        UserFile = open("Users.txt", "r")
        
        UserName = input("Enter User Name: ")
        UserPwd = input("Enter Password: ")
        UserRole = "NONE"
        found = False  
        while True:
            UserDetail = UserFile.readline()
            if not UserDetail:
                break  
            
            UserDetail = UserDetail.strip()
            # Splitting UserDetail on the pipe delimiter (|) and assign it to UserList
            UserList = UserDetail.split("|")
                    
            if UserName == UserList[0]:
                found = True
                if UserPwd == UserList[1]:
                    UserRole = UserList[2]  
                    print(f"Welcome {UserName}, role: {UserRole}")
                    UserFile.close()
                    return UserRole, UserName
                else:
                    print(f"Invalid password for user {UserName}. Please try again.\n")
                    break  
        UserFile.close()
        if not found:
            print(f"User {UserName} does not exist. Please try again.\n")
            
################################################################################
# EMPLOYEE FUNCTIONS
def GetEmpName():
    empname = input("Enter employee name or 'End' to quit: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours

def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input ("Enter tax rate (e.g 0.2 for 20%): "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    # if no empoyees data has been entered / if no Employees.txt existing
    if not os.path.exists("Employees.txt"):
        open("Employees.txt", "w").close()

    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    with open("Employees.txt","r") as EmpFile:
        while True:
            rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
            if (rundate.upper() == "ALL"):
                break
            try:
                rundate = datetime.strptime(rundate, "%m/%d/%Y")
                break
            except ValueError:
                print("Invalid date format. Try again.\n")
                continue

        for EmpDetail in EmpFile:
            EmpDetail = EmpDetail.strip()
            if not EmpDetail:
                continue
            EmpList = EmpDetail.split("|")
            fromdate = EmpList[0]
            if (str(rundate).upper() != "ALL"):
                checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
                if (checkdate < rundate):
                    continue        
            todate = EmpList[1]
            empname = EmpList[2]
            hours = float(EmpList[3])
            hourlyrate  = float(EmpList[4])
            taxrate = float(EmpList[5])
            grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
            print(fromdate, todate, empname, f"{hours:,.2f}",  
                  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  
                  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  
                  f"{netpay:,.2f}")
            TotEmployees += 1
            TotHours += hours
            TotGrossPay += grosspay
            TotTax += incometax
            TotNetPay += netpay
            EmpTotals = {}
            EmpTotals["TotEmp"] = TotEmployees
            EmpTotals["TotHrs"] = TotHours
            EmpTotals["TotGrossPay"] = TotGrossPay
            EmpTotals["TotTax"] = TotTax
            EmpTotals["TotNetPay"] = TotNetPay
            DetailsPrinted = True   

    if (DetailsPrinted):
        PrintTotals(EmpTotals)
    else:
        print("No detail information to print")

def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')

################################################################################
# MAIN APPLICATION
def main_application():
    # Check if any users exist
    if not os.path.exists("Users.txt") or os.path.getsize("Users.txt") == 0:
        print("No users found. Returning to User Management to create users.\n")
        main_user_management()
        return

    printuserinfo()
    
    print()
    print("##### Main Application #####")
    UserRole, UserName = login_process()
     
    DetailsPrinted = False  
    EmpTotals = {}  

    if UserRole == "NONE":
        pass
    else:
        if UserRole.upper() == "ADMIN":
            EmpFile = open("Employees.txt", "a+")                
            while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDetail = fromdate + "|" + todate  + "|" + empname  + "|" + str(hours)  + "|" + str(hourlyrate)  + "|" + str(taxrate) + "\n"  
                EmpFile.write(EmpDetail)
            EmpFile.close()               
    
        if os.path.exists("Employees.txt"):
            printinfo(DetailsPrinted)
        else:
            print("No employee data available yet.")

################################################################################
# MAIN MENU
def main_menu():
    while True:
        print("\n=== CIS261 Course Project Phase 4 ===")
        print("1. User Management Application")
        print("2. Main Application")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            main_user_management()
        elif choice == "2":
            main_application()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
