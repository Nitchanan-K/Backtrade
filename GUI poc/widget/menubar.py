from tkinter import *
from tkinter import filedialog

# functions for menu use
def openFile():
    # chose file
    filepath = filedialog.askopenfilename(initialdir = "C:\\Users\\Admin pc\\Desktop\\data",
                                          title = "Open file okay?",
                                          filetypes = (("text files","*.txt"),
                                                       ("all files","*.*"))

                                         )
    # now we can do whatever with filepath for ex open file and read
    # idea is to chose file and run with the plot command
    file = open(filepath)
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.xlsx',
                                    filetypes=[("xlsx file",".xlsx")])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

def Cut():
    print("you cut")
def Copy():
    print("you copy")
def Paste():
    print("you paste")

#######################################################################################################################
# make window
window = Tk()

# make menubar and add to window
menubar = Menu(master=window)
# set menu of the window = menubar
window.config(menu=menubar) # menu of window = menubar

#######################################################################################################################
# each menu tab we need to make a seperate menu and add it's to menu bar
# make file menu and add file manu to menubar
fileMenu = Menu(master=menubar,tearoff=0,font=("Mv Boli",15))
# make drop down of file menubar
menubar.add_cascade(label="File",menu=fileMenu)
# make click able options # we can import command and by make a class of that command for now let make functions
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator() # add line separator
fileMenu.add_command(label="Exit",command=quit)


#######################################################################################################################
# make Edit menu and add to menu bar
editMenu = Menu(master=menubar,tearoff=0,font=("Mv Boli",15))
# make drop down of edit menubar
menubar.add_cascade(label="Edit",menu=editMenu)
# add options
editMenu.add_command(label='Copy',command=Copy)
editMenu.add_command(label='Cut',command=Cut)
editMenu.add_command(label='Paste',command=Paste)

#######################################################################################################################
# text window for function savefile for now
text = Text(window)
text.pack()

# run
window.mainloop()




























