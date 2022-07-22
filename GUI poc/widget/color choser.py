from tkinter import *
from tkinter import  colorchooser

# make func for color chose
def click_color():
    color = colorchooser.askcolor()
    print(color) # return RGB and HEX number
    colorHex = color[1]
    print(colorHex)

    # SET BG by colorHex
    window.config(bg=colorHex) # get color from the colorchooser.askcolor


# make window
window = Tk()
# set size
window.geometry("420x420")
# make button
button = Button(text='click me!',
                command=click_color

                )
button.pack()

# run window
window.mainloop()









