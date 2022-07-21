from tkinter import *


# function display
# to check value of variable x = 1 or 0
def display():
    if (x.get() == 1):
        print("You checked the check box")
    elif (x.get() == 0):
        print("You not checked the check box")

# to check value of variable x = Ture or False
def display_2():
    if (y.get()):
        print("You checked the check box")
    else:
        print("You not checked the check box")

# make window
window = Tk()

# make x variable for put in the check box param and def display for ref value
x = IntVar()

# make y variable for put in the check box param and def display for ref value
y = BooleanVar()


# convert png to pti
icon = PhotoImage(file="google img.png")

# check button 1 ro 0 value
# it return 1 or 0
check_button = Checkbutton(master=window,
                           text=" I agree to something",
                           variable=x,
                           onvalue=1,   # if toggle on value = 1
                           offvalue=0,   # if toggle off value = 0
                           command=display,
                           font=('Arial',20),
                           foreground="#00FF00",
                           background="black",
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=20,
                           pady=10,
                           image=icon,
                           compound='left'
                           )

# check button  Ture or False value
# it return Ture or False

check_button_2 = Checkbutton(master=window,
                           text=" I agree to something",
                           variable=y,
                           onvalue=True,   # if toggle on value = True
                           offvalue=False,   # if toggle off value = False
                           command=display_2,
                           font=('Arial',40),
                           foreground="#00FF00",
                           background="black",
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=20,
                           pady=10,
                           )
# place
check_button.pack()
check_button_2.pack(side="bottom")

# run window
window.mainloop()