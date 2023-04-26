import sqlite3

def insertData():
    # Connect to the database
    conn = sqlite3.connect('FoodCoupon.db')

    # Create a cursor object
    c = conn.cursor()

    # Accept employee data from the user
    name = input("Enter employee name: ")
    emaidID = input("Enter employee email id: ")
    phoneNo = int(input("Enter employee phone No.: "))
    couponsGiven = int(input("Coupons Given: "))
    balanceRemaining = int(input("Enter employee's balance remainig: "))

    # Insert employee data into the database
    c.execute("INSERT INTO foodCoupon (name, emaidID, phoneNo, couponsGiven, balanceRemaining) VALUES (?, ?, ?, ?, ?)", (name, emaidID, phoneNo, couponsGiven, balanceRemaining))

    # Save the changes
    conn.commit()

    # Close the connection
    conn.close()
