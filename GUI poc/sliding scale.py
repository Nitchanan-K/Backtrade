from tkinter import *


# make func for button summit
def submit():
    print(f"value is : {scale.get()}.")




window = Tk()


# convert image after window
maxImage = PhotoImage(file='maximum.png')
maxLabel = Label(image=maxImage)
# place maxlabel
maxLabel.pack()



# make scale slide
scale = Scale(master=window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, # or orientation of scale
              font=("Consolas",20),
              tickinterval=10,
              showvalue= True, # False is not show value
              resolution= 5, # increment if slider
              troughcolor= '#69EAFF',
              fg='red',
              background='black'

              )


# make button for submit value
button = Button(master=window, text='submit', command= submit )

# set default scale value
# scale.set(50)
# or use this format to set scale to middle what ever of value is
scale.set(((scale['from']-scale['to'])/2) + scale['to'])


# place
scale.pack()

# place Image min before button
minImage = PhotoImage(file='minimun.png')
minLabel = Label(image=minImage)
minLabel.pack()

# place button
button.pack()


window.mainloop()