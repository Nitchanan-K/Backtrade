# frame = rectangular container to group and hold widgets

from tkinter import *

# make window
window = Tk()

# make frame and add frame to window
frame = Frame(master=window,bg="pink",border=5,relief=SUNKEN)
frame.pack(side=BOTTOM) # or use .place(x=..,y=00)

# make button
button_w = Button(master=frame,text="W",font=("Comsolas",25),width=3)
button_w.pack(side=TOP)
button_A = Button(master=frame,text="A",font=("Comsolas",25),width=3)
button_A.pack(side=LEFT)
button_S = Button(master=frame,text="S",font=("Comsolas",25),width=3)
button_S.pack(side=LEFT)
button_D = Button(master=frame,text="D",font=("Comsolas",25),width=3)
button_D.pack(side=LEFT)


window.mainloop()
