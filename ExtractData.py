import sqlite3
import employeeStruct as emp

employeeObj = emp.Employee("some@3ds.com", "simbi", "0000", "0","0" )

def extractData(userMailOrPhone):
    # Connect to the database
    conn = sqlite3.connect('FoodCoupon.db')

    # Create a cursor object to execute SQL statements
    c = conn.cursor()

    # Execute a SELECT statement to retrieve the employee name and salary
    c.execute("SELECT name, emaidID, phoneNo, couponsGiven, balanceRemaining FROM foodCoupon")

    # Fetch all rows returned by the SELECT statement
    rows = c.fetchall()

    # Iterate over the rows and print the employee name and salary
    for row in rows:
        emailId = row[1]
        phoneNo = row[2]
        if(userMailOrPhone == emailId or  userMailOrPhone == phoneNo):
            name = row[0]
            employeeObj.userName = row[0]
            employeeObj.userMailID = row[1]
            phoneNo = row[2]
            employeeObj.userPhone = row[2]
            couponsGiven = row[3]
            employeeObj.userCoupons = row[3]
            balanceRemaining = row[4]
            employeeObj.userBalance = row[4]
            print(f" Employee Name: {name} \n Emaid ID: {emailId}\n Phone No. : {phoneNo}\n Coupons Given : {couponsGiven}\n Balance Remaining : {balanceRemaining}\n")
            break

    # Close the cursor and database connection
    c.close()
    conn.close()

    return employeeObj
