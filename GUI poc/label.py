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
window.config(background="white")

# add photo
# convert to ph image
photo = PhotoImage(file='google img.png')


# label / area of widget that hold text and image within a window
label = Label(master=window,
              text='Hello World',
              font=('Arial',40,'bold'),
              foreground='#00FF00',
              background='black',
              relief=RAISED,
              border=10,
              padx=20,         # space between front and border
              pady=20,
              image=photo,
              compound='bottom' # add text and image on same window (top ,left or right)
              )
label_2 = Label(master=window,text="label_2")
# add label to window use pack
label.pack()
label_2.place(x=100,y=100)

# run use mainloop
window.mainloop() # place window on computer screen. listen for events

