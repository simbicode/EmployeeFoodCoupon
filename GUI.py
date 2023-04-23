# Python program to create a
# GUI mark sheet using tkinter


# Import tkinter as tk
from itertools import groupby
import tkinter as tk
from tkinter import ttk

# creating a new tkinter window
master = tk.Tk()

# assigning a title
master.title("Food Coupon Management")

# specifying geometry for window size
master.geometry("900x450")

#set the background color
master.configure(bg="grey")


# declaring objects for entering data
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)


# function to display the total subject
# credits total credits and SGPA according
# to grades entered
def display():

	# Variable to store total marks
	tot = 0

	# 10*number of subject credits
	# give total credits for grade A
	if e4.get() == "A":

		# grid method is used for placing
		# the widgets at respective positions
		# in table like structure .
		tk.Label(master, text="40").grid(row=3, column=4)
		tot += 40

	# 9*number of subject credits give
	# total credits for grade B
	if e4.get() == "B":
		tk.Label(master, text="36").grid(row=3, column=4)
		tot += 36

	# 8*number of subject credits give
	# total credits for grade C
	if e4.get() == "C":
		tk.Label(master, text="32").grid(row=3, column=4)
		tot += 32

	# 7*number of subject credits
	# give total credits for grade D
	if e4.get() == "D":
		tk.Label(master, text="28").grid(row=3, column=4)
		tot += 28

	# 6*number of subject credits give
	# total credits for grade P
	if e4.get() == "P":
		tk.Label(master, text="24").grid(row=3, column=4)
		tot += 24

	# 0*number of subject credits give
	# total credits for grade F
	if e4.get() == "F":
		tk.Label(master, text="0").grid(row=3, column=4)
		tot += 0

	# Similarly doing with other objects
	if e5.get() == "A":
		tk.Label(master, text="40").grid(row=4, column=4)
		tot += 40
	if e5.get() == "B":
		tk.Label(master, text="36").grid(row=4, column=4)
		tot += 36
	if e5.get() == "C":
		tk.Label(master, text="32").grid(row=4, column=4)
		tot += 32
	if e5.get() == "D":
		tk.Label(master, text="28").grid(row=4, column=4)
		tot += 28
	if e5.get() == "P":
		tk.Label(master, text="28").grid(row=4, column=4)
		tot += 24
	if e5.get() == "F":
		tk.Label(master, text="0").grid(row=4, column=4)
		tot += 0

	if e6.get() == "A":
		tk.Label(master, text="30").grid(row=5, column=4)
		tot += 30
	if e6.get() == "B":
		tk.Label(master, text="27").grid(row=5, column=4)
		tot += 27
	if e6.get() == "C":
		tk.Label(master, text="24").grid(row=5, column=4)
		tot += 24
	if e6.get() == "D":
		tk.Label(master, text="21").grid(row=5, column=4)
		tot += 21
	if e6.get() == "P":
		tk.Label(master, text="28").grid(row=5, column=4)
		tot += 24
	if e6.get() == "F":
		tk.Label(master, text="0").grid(row=5, column=4)
		tot += 0

	if e7.get() == "A":
		tk.Label(master, text="40").grid(row=6, column=4)
		tot += 40
	if e7.get() == "B":
		tk.Label(master, text="36").grid(row=6, column=4)
		tot += 36
	if e7.get() == "C":
		tk.Label(master, text="32").grid(row=6, column=4)
		tot += 32
	if e7.get() == "D":
		tk.Label(master, text="28").grid(row=6, column=4)
		tot += 28
	if e7.get() == "P":
		tk.Label(master, text="28").grid(row=6, column=4)
		tot += 24
	if e7.get() == "F":
		tk.Label(master, text="0").grid(row=6, column=4)
		tot += 0

	# to display total credits
	tk.Label(master, text=str(tot)).grid(row=7, column=4)

	# to display SGPA
	tk.Label(master, text=str(tot/15)).grid(row=8, column=4)


#=====================Group box=====================
dataEntryBox = ttk.LabelFrame(master, text='Data Entry')
dataEntryBox.grid(column=0, row=0, padx=20, pady=20)

#====================== end of display function======================

#Cosmetics Variable
sizeOfLabel = 15
fontOfLabel = "Arial"
#=============================ENTRY COLUMN=================================
# label to enter name
tk.Label(dataEntryBox, text="Name ", anchor = 'w',font=(fontOfLabel, sizeOfLabel)).grid(row = 0, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 1, column=0)
# label for email id
tk.Label(dataEntryBox, text="UserID ", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 2, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 3, column=0)
# label for phone no.
tk.Label(dataEntryBox, text="Phone ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 4, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 5, column=0)
# label for Coupons Given
tk.Label(dataEntryBox, text="Coupons", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 6 , column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 7, column=0)
# label for Balance Remaining
tk.Label(dataEntryBox, text="Balance", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 8, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 9, column=0)

# taking entries of name, reg, roll number respectively
nameEntry = tk.Entry(dataEntryBox)
emailEntry = tk.Entry(dataEntryBox)
phoneEntry = tk.Entry(dataEntryBox)
couponEntry = tk.Entry(dataEntryBox)
balanceEntry = tk.Entry(dataEntryBox)

# organizing them in the grid
nameEntry.grid(row=0, column=1)
emailEntry.grid(row=2, column=1)
phoneEntry.grid(row=4, column=1)
couponEntry.grid(row=6, column=1)
balanceEntry.grid(row=8, column=1)

button1 = tk.Button(dataEntryBox, text="Enter", bg="green", command=display, font=(fontOfLabel, sizeOfLabel))
button1.grid(row=11, column=1)

#==========================QUERY COLUMN===================================

#Groupbox
dataSearchBox = ttk.LabelFrame(master, text='Data Search')
dataSearchBox.grid(column=3, row=0, padx=20, pady=20)

#Create radio buttons
selected_value = tk.StringVar()

# Create three Radiobuttons with different values and labels
radio_button1 = tk.Radiobutton(dataSearchBox, variable=selected_value, value="1")
radio_button1.grid(row=0, column=3)

radio_button2 = tk.Radiobutton(dataSearchBox, variable=selected_value, value="2")
radio_button2.grid(row=2, column=3)


# labels for subject codes
tk.Label(dataSearchBox, text="Email id : ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 0, column=4)
tk.Label(dataSearchBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 1, column=4)
tk.Label(dataSearchBox, text="Phone  num : ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 2, column=4)
tk.Label(dataSearchBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 3, column=4)


# taking entries of name, reg, roll number respectively
emailSearch = tk.Entry(dataSearchBox)
numSearch = tk.Entry(dataSearchBox)

# organizing them in the grid
emailSearch.grid(row=0, column=5)
numSearch.grid(row=2, column=5)

button1 = tk.Button(dataSearchBox, text="Search", bg="green", command=display, font=(fontOfLabel, sizeOfLabel))
button1.grid(row=4, column=5)


#=================DISPLAY SEARCHED ENTRY======================
displayResult = ttk.LabelFrame(master, text='Data Display')
displayResult.grid(column=5, row=0, padx=20, pady=20)

# label to enter name
tk.Label(displayResult, text="Name ", anchor = 'w',font=(fontOfLabel, sizeOfLabel)).grid(row = 0, column=2)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 1, column=2)
# label for email id
tk.Label(displayResult, text="UserID ", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 2, column=2)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 3, column=2)
# label for phone no.
tk.Label(displayResult, text="Coupons ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 4, column=2)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 5, column=2)
# label for Coupons Given
tk.Label(displayResult, text="Balance", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 6 , column=2)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 7, column=2)




master.mainloop()


# This Marksheet can be snapshotted and printed out
# as a report card for the semester

# This code has been contributed by Soumi Bardhan
