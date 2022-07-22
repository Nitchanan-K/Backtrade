from tkinter import *

window = Tk()

# make Entry
entry = Entry(master=window,
              font=('Arial',50),
              foreground="#00FF00",
              background="black",
              # show="*"  ## display as * when enter any chars

              )
# make default text
entry.insert(0,"default text")

# make func of submit button
def submit():
    username = entry.get() # this return a str from the entry object box
    entry.config(state=DISABLED) # after submit or run this func we config state to disabled
    print(username)

# make func of delete button
def delete():
    entry.delete(0,END) # (index if char, to what point) ( index0 to END of box entry)

# make func of backspace button
def backspace():
    entry.delete(len(entry.get())-1,END)

# make submit button
submit_button = Button(master=window,
                       text="submit",
                       command=submit
                       )
# make delete button
delete_button = Button(master=window,
                       text="delete",
                       command=delete
                       )
# make backspacee button
backspace_button = Button(master=window,
                       text="backspace",
                       command=backspace
                       )



# place
entry.pack(side=LEFT)
submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)




window.mainloop()