from tkinter import *
from tkinter import ttk # get more wigget

# make window
window = Tk()


# make notebook object by ttk.Notebook set master to window
notebook = ttk.Notebook(master=window) # widget that manages a collection of windows/displays

# make tab1 by using Frame set master to the notebook
tab1 = Frame(master=notebook) # new frame = tab 1
# make tab2 by using Frame set master to the notebook
tab2 = Frame(master=notebook) # new frame = tab 2

# after make tab by use frame
# add that tab by use notebook.add
notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")

# run notebook
notebook.pack(expand=True,fill="both") # expand = expand to fill any space bot otherwise used
                                       # fill = fill will spcae on x and y
                                       # now tab will expand to the window size 

# make label object for tab 1
label_tab1 = Label(tab1,text="This is Tab number 1",width=50,height=25)
label_tab1.pack()
# make label object for tab 1
label_tab2 = Label(tab2,text="This is Tab number 1",width=50,height=25)
label_tab2.pack()

# run window
window.mainloop()







