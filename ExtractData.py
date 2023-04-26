import sqlite3

def extractData(userMailID,userName,userPhone, userCoupons,userBalance ):
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
        if(userMailID == emailId):
            name = row[0]
            userName = row[0]
            phoneNo = row[2]
            userPhone = row[2]
            couponsGiven = row[3]
            userCoupons = row[3]
            balanceRemaining = row[4]
            userBalance = row[4]
            print(f" Employee Name: {name} \n Emaid ID: {emailId}\n Phone No. : {phoneNo}\n Coupons Given : {couponsGiven}\n Balance Remaining : {balanceRemaining}\n")

    # Close the cursor and database connection
    c.close()
    conn.close()
