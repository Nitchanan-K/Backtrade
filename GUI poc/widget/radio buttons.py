from tkinter import *

# radio button
# select one from a group
food = ["pizza","hamburger","hotdog"]

# set functions
def order():
    if (x.get()) == 0:
        print("you order Pizza")
    elif (x.get()) == 1:
        print("you ordered Hamberger")
    elif (x.get()) == 2:
        print("you ordered hotdog")


window = Tk()

# set x variable after make window Tk
# hold int object
x = IntVar()

# set image
pizzaImage = PhotoImage(file='../pizza.png')
hamImage = PhotoImage(file='../hamberger.png')
hotdogImage = PhotoImage(file='../hotdog.png')
# list of image
foodImage = [pizzaImage,hamImage,hotdogImage]

# put in for loop
for index in range(len(food)):
    radiobutton = Radiobutton(master=window,
                              text=food[index], # add text to radio buttons
                              variable=x, # groups radiobuttons if they shere variable
                              value=index, # assigns each radiobuttons a dif value
                              padx=25,
                              font=('Impact',50),
                              image=foodImage[index], # add image to radio button
                              compound='left',
                              indicatoron= False, # eliminate circle indicators
                              width= 1000, # set width of radio button
                              command=order
                              )

    radiobutton.pack(anchor=W) # place inside loop


window.mainloop()


