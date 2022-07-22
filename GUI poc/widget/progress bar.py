from tkinter import *
from tkinter import ttk
import time

# make func for progress bar
def start():
    GB = 50
    download = 0
    speed = 2
    # add delay
    while(download<GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        # set percent
        percent.set(str(int((download/GB)*100))+"%")
        # set task
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()


# make window
window = Tk()

# make percent as str value
percent = StringVar()
# make text label
text = StringVar()

# make progress bar
bar = ttk.Progressbar(master=window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

# percent label
percentLabel = Label(window,textvariable=percent).pack()

# make task label
taskLabel = Label(window,textvariable=text).pack()

# make download button
button = Button(master=window,text="download",command=start).pack()










# run window
window.mainloop()
