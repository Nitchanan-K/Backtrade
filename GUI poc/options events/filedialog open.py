from tkinter import *
from tkinter import filedialog

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



# make window
window = Tk()

button = Button(text="Open",
                command=openFile

                )
button.pack()

# run window
window.mainloop()














