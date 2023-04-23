# EmployeeFoodCoupon
Manage distribution of food coupons to employees

1. Install sqlite3 from sqlite website. Download the precompiled windows binaries.
2. database Name : foodCoupon

======SQLITE DEVELOPMENT=======
 Steps to create first db entries:
   a) sqlite3 FoodCoupon.db
   b) Create Table : CREATE TABLE foodCoupon (id INTEGER PRIMARY KEY, name TEXT, emaidID TEXT, phoneNo INTEGER, couponsGiven INTEGER, balanceRemaining REAL);
   c) Insert Data : INSERT INTO foodCoupon name, emaidID, phoneNo, couponsGiven, balanceRemaining VALUES ('Prashant','prashant.sharma@3ds.comm', 82916173712, 30, 0);
   d) Display Entry : SELECT name, emaidID, phoneNo, couponsGiven, balanceRemaining FROM  FoodCoupon;
   
   
