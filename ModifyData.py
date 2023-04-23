import sqlite3

#NOTE:
"""
1. email id cannot be updated
2. Items that can be updated are as follows:
	a) Name
	b) phone Number
	c) Coupons Given
	d) balance Remaining
"""

# Connect to the database
conn = sqlite3.connect('FoodCoupon.db')

# Create a cursor object to execute SQL statements
c = conn.cursor()

emailId = input("Enter employee's email id for reference :")

print("What do you want to modify ? ")
print ("Enter 1 for Name \n")
print ("Enter 2 for Phone No. \n")
print ("Enter 3 for Coupons Given \n")
print ("Enter 4 for Balance Remaining \n")

enteredNo = int(input("Enter here: "))

if enteredNo == 1:
	correctName = input("Enter correct name : ")
	c.execute("UPDATE foodCoupon SET name = ? WHERE emaidId = ?", (correctName, emailId))
elif enteredNo == 2:
	correctPhone = int(input("Enter correct phone num : "))
	c.execute("UPDATE foodCoupon SET phoneNo = ? WHERE emaidId = ?", (correctPhone, emailId))
elif enteredNo == 3:
	correctCoupons = int(input("Enter correct coupons given : "))
	c.execute("UPDATE foodCoupon SET couponsGiven = ? WHERE emaidId = ?", (correctCoupons, emailId))
else:
	correctBalance = int(input("Enter correct balance ramaining : "))
	c.execute("UPDATE foodCoupon SET balanceRemaining = ? WHERE emaidId = ?", (correctBalance, emailId))	

# Commit the transaction
conn.commit()

# Close the cursor and database connection
c.close()
conn.close()
