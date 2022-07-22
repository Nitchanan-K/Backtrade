from tkinter import *

# grid() = geometry manager that organizes widgets in table-liek structure in a parent

# make window
window = Tk()

# make title
titleLabel = Label(master=window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2,pady=20,padx=20)

# make Label and Entry
firstnameLabel = Label(master=window,text="First name: ",width=20,bg="red").grid(row=1,column=0,pady=4,padx=4)
firstnameEntry = Entry(master=window).grid(row=1,column=1)

lastnameLabel = Label(master=window,text="Last name: ",bg="green").grid(row=2,column=0,pady=4,padx=4)
lastnameEntry = Entry(master=window).grid(row=2,column=1)

emailLabel = Label(master=window,text="Email: ",bg="blue",width=30).grid(row=3,column=0,pady=4,padx=4)
emailEntry = Entry(master=window).grid(row=3,column=1)

# size of the colum with auto expand to the largest widget in this case is email with width = 30 see by the color

# make submit button
submitButton = Button(master=window,text="Submit").grid(row=4,column=0,columnspan=2) # columnspan = set this widget to take 2 spaces of colum avalible


# run window
window.mainloop()

