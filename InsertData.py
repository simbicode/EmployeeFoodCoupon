import sqlite3
import employeeStruct as emp


def insertData(Employee):
    # Connect to the database
    conn = sqlite3.connect('FoodCoupon.db')

    # Create a cursor object
    c = conn.cursor()
    # Insert employee data into the database
    c.execute("INSERT INTO foodCoupon (name, emaidID, phoneNo, couponsGiven, balanceRemaining) VALUES (?, ?, ?, ?, ?)", (Employee.userName, Employee.userMailID, Employee.userPhone, Employee.userCoupons, Employee.userBalance))
    print("Congratulations! New Entry Made")
    # Save the changes
    conn.commit() 
    # Close the connection
    conn.close()
