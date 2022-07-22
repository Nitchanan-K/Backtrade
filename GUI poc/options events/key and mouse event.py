from tkinter import *

# make def for bind
def doSomething(event):
    print(f"You pressed: " + event.keysym)
    label.config(text=event.keysym)


# make def for mouse event
def bind_mouse(event):
    print("mouse coordinates" + str(event.x)+","+str(event.y))


# make window
window = Tk()

# make bind key =  <..>  any key inside
window.bind("<Key>",doSomething)

# make bind mouse
window.bind("<Button-1>",bind_mouse) # Button-3 left mouse
window.bind("<Button-2>",bind_mouse) # Button-2 = scroll wheel
window.bind("<Button-3>",bind_mouse) # Button-3 right mouse
window.bind("<ButtonRelease>",bind_mouse)
window.bind("<Enter>",bind_mouse)
window.bind("<Leave>",bind_mouse)
window.bind("<Motion>",bind_mouse) # when the mouse move

# make label to see what key we pressed on GUI
label = Label(master=window,font=("Helvetica",100))
label.pack()

# run window
window.mainloop()



########################################################################################################################











