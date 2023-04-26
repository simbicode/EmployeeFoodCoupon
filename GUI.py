# Python program to create a
# GUI mark sheet using tkinter


# Import tkinter as tk
from itertools import groupby
import tkinter as tk
from tkinter import ttk
import ExtractData as ext

# creating a new tkinter window
master = tk.Tk()

# assigning a title
master.title("Food Coupon Management")

# specifying geometry for window size
master.geometry("1000x450")

#set the background color
master.configure(bg="grey")

userName = ""
userPhone = 0
userCoupons = 0
userBalance = 0

def display():
	print("Getting Data")
	emailGet = emailSearch.get()
	ext.extractData(emailGet, userName,userPhone, userCoupons,userBalance)
	print ("Name : ", userName, "Phone : ", userPhone,"Coupons : " ,userCoupons,"Balance : ", userBalance)
	displayNameLabel.config(text=userName)
	displayBalanceLabel.config(text=userPhone)
	displayCouponsLabel.config(text=userCoupons)
	displayUserIdLabel.config(text=userBalance)



#=====================Group box=====================
dataEntryBox = ttk.LabelFrame(master, text='Data Entry')
dataEntryBox.grid(column=0, row=0, padx=20, pady=20)

#====================== end of display function======================

#Cosmetics Variable
sizeOfLabel = 15
fontOfLabel = "Arial"
#=============================ENTRY COLUMN=================================
# label to enter name
tk.Label(dataEntryBox, text="Name : ", anchor = 'w',font=(fontOfLabel, sizeOfLabel)).grid(row = 0, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 1, column=0)
# label for email id
tk.Label(dataEntryBox, text="UserID : ", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 2, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 3, column=0)
# label for phone no.
tk.Label(dataEntryBox, text="Phone : ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 4, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 5, column=0)
# label for Coupons Given
tk.Label(dataEntryBox, text="Coupons :", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 6 , column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 7, column=0)
# label for Balance Remaining
tk.Label(dataEntryBox, text="Balance : ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 8, column=0)
tk.Label(dataEntryBox, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 9, column=0)

# taking entries of name, reg, roll number respectively

entryBoxWidth = 30
nameEntry = tk.Entry(dataEntryBox, width =entryBoxWidth)
emailEntry = tk.Entry(dataEntryBox, width = entryBoxWidth)
phoneEntry = tk.Entry(dataEntryBox, width = entryBoxWidth)
couponEntry = tk.Entry(dataEntryBox, width = entryBoxWidth)
balanceEntry = tk.Entry(dataEntryBox, width = entryBoxWidth)

# organizing them in the grid
nameEntry.grid(row=0, column=1)
emailEntry.grid(row=2, column=1)
phoneEntry.grid(row=4, column=1)
couponEntry.grid(row=6, column=1)
balanceEntry.grid(row=8, column=1)

button1 = tk.Button(dataEntryBox, text="Enter", bg="green", command=display, font=(fontOfLabel, sizeOfLabel))
button1.grid(row=11, column=1)

#==========================DATA SEARCH COLUMN===================================

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
emailSearch = tk.Entry(dataSearchBox,width = entryBoxWidth)
numSearch = tk.Entry(dataSearchBox,width = entryBoxWidth)

# organizing them in the grid
emailSearch.grid(row=0, column=5)
numSearch.grid(row=2, column=5)

button1 = tk.Button(dataSearchBox, text="Search", bg="green", command=display, font=(fontOfLabel, sizeOfLabel))
button1.grid(row=4, column=5)


#=================DISPLAY SEARCHED ENTRY======================
displayResult = ttk.LabelFrame(master, text='Data Display')
displayResult.grid(column=5, row=0, padx=20, pady=20)

# label to enter name
tk.Label(displayResult, text="Name : ", anchor = 'w',font=(fontOfLabel, sizeOfLabel)).grid(row = 0, column=2)
displayNameLabel = tk.Label(displayResult, text="--------------------", anchor = 'w',font=(fontOfLabel, sizeOfLabel)).grid(row = 0, column=3)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 1, column=2)
# label for email id
tk.Label(displayResult, text="UserID : ", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 2, column=2)
displayUserIdLabel = tk.Label(displayResult, text="--------------------", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 2, column=3)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 3, column=2)
# label for phone no.
tk.Label(displayResult, text="Coupons : ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 4, column=2)
displayCouponsLabel = tk.Label(displayResult, text="--------------------", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 4, column=3)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 5, column=2)
# label for Coupons Given
tk.Label(displayResult, text="Balance : ", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 6 , column=2)
displayBalanceLabel = tk.Label(displayResult, text="--------------------", font=(fontOfLabel, sizeOfLabel), anchor = 'w').grid(row = 6 , column=3)
tk.Label(displayResult, text="", anchor = 'w', font=(fontOfLabel, sizeOfLabel)).grid(row = 7, column=2)


master.mainloop()
