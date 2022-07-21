from tkinter import *
# list box = a listing of selectable text items within it's own container

# func submit bottom

'''
# submit for single object
def submit_button():
    print("You have ordered:")
    print(listbox.get(listbox.curselection()))

'''


def submit_button():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered:")

    for index in food:
        print(index)

# func for add button
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

''' delete button for single object 
# func for delete button
def delete_button():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
'''

# func for delete button multiple object
def delete_button():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


# make window
window = Tk()

#make listbox
listbox = Listbox(master=window,
                  bg="#F7FFDE",
                  font=("Constantin",35),
                  width=12,
                  selectmode=MULTIPLE # select multiple thing
                  )
# place list box
listbox.pack()

# insert text to list box
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

# change size
listbox.config(height=listbox.size())


# make entry box
entryBox = Entry(master=window)
#place entrybox
entryBox.pack()


# submit button
submit_button = Button(master=window,
                       text='submit',
                       command=submit_button
                       )
# place submit button
submit_button.pack()


# add button for add text to list box
add_button = Button(master=window,
                       text='add',
                       command=add
                       )
#place add button
add_button.pack()

# delete button
deleteButton = Button(master=window,
                       text='delete',
                       command=delete_button
                       )
# place delete button
deleteButton.pack()

# run
window.mainloop()