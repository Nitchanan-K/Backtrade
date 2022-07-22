from tkinter import*
from tkinter import  filedialog
import xlsxwriter

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.xlsx',
                                    filetypes=[("xlsx file",".xlsx")])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
button_save = Button(text='save',command=saveFile)
button_save.pack()
text = Text(window)
text.pack()
window.mainloop()