from tkinter import *

window = Tk() # instantiate an instance of a window

# size
window.geometry("980x900")

#title
window.title("Bro Code first GUI program")


# convert png to pti
icon = PhotoImage(file="btlogo02.png")

# set logo
window.iconphoto(True,icon)

# backg color can use colour name or hex value
window.config(background="grey")

# run use mainloop
window.mainloop() # place window on computer screen. listen for events

