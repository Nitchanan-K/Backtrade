from tkinter import *

# make function for make new window
def create_window():
    new_window = Toplevel() # = new window 'on top' or the other windows. linked to bottom window in this case bt is main window
    new_window_independent = Tk() # = use full for login from after login we enter main program

    # we can destory old window
    # window.destroy()
# make window
window = Tk()

button_new_window = Button(master=window,
                           text="create new window",
                           command=create_window
                           )
button_new_window.pack()

window.mainloop()



