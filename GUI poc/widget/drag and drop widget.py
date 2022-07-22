from tkinter import *


# def func drag_start
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

# make drag_motion
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

# make window
window = Tk()

# make widget
label = Label(master=window,bg="red",width=10,height=5)
label.place(x=0,y=0)

# make second widget
label2 = Label(master=window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

# bind widget
label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

# bind second widget
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)


# run window
window.mainloop()