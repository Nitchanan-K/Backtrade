from tkinter import *
from tkinter import messagebox

# func for click button
def click ():
    messagebox.showinfo(title='This is an info massage box',message='you are a person')
    #while(True): # will open this forever
    #messagebox.showwarning(title='warning', message='you have a virus')
    #messagebox.showerror(title='error',message='something went wrong')

    '''
    # ask user input
    # will return Ture or False
    if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing'):
        print("you did a thing!")
    else:
        print("you canceled a thing!")
    '''

    '''
    # ask retrycancel
    if messagebox.askretrycancel(title='ask retry cancel',message='Do you want to retry the thing'):
        print("you retry a thing!")
    else:
        print("you canceled a thing!")
    '''

    '''
    # ask yes no # return True or False answer
    if messagebox.askyesno(title='ask yes or no',message='Do you like cake'):
        print('You liked cake')
    else:
        print('You dont like cake')
    '''

    '''
    # ask question # return str of (yes) or (no)
    answer = messagebox.askquestion(title='ask question:',message='Do you like pie?')
    if (answer == 'yes'):
        print('I like pie too')
    else:
        print('Why do you not like pie')
    '''

    '''
    # ask yes no cancel
    # yes return = True
    # no return = False
    # cancel return = None
    a = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?',icon ='info')
    if (a == True):
        print('You like to code')
    elif(a == False):
        print('Why are you not like to code')
    else:
        print('You have Dodged the question')
    '''

window = Tk()

# make button
button = Button(master=window,
                command=click,
                text = 'click me '
                )
# place button
button.pack()


window.mainloop()
