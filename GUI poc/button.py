from tkinter import *

# bottom = click do stuff

window = Tk()

# make func for button
count = 0
def click():
    global count
    count += 1
    print(f"You clicked the button {count} times.")


# size
window.geometry("800x800")

# convert png to pti
icon = PhotoImage(file="google img.png")


# add button
button = Button(master=window,
                text="click me!",
                command=click,
                font=('Comic Sans',30),
                foreground="#00FF00",
                background="black",
                activeforeground="#00FF00",
                activebackground="black",
                state = ACTIVE, # can be DISABLE
                image=icon,
                compound='top'
                )
# place
button.pack()


window.mainloop()