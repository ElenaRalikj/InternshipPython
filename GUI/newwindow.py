# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *


class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()

        self.b1 = Button(master, text='Next Frame')
        self.b1.grid(row=0, column=0)
        self.b2 = Button(master, text='Previous Frame')
        self.b2.grid(row=0, column=1)


# creates a Tk() object
master = Tk()

# sets the geometry of
# main root window
master.geometry("200x200")


label = Label(master, text="This is the main window")
label.pack(side=TOP, pady=10)

# a button widget which will
# open a new window on button click
btn = Button(master,
             text="Click to open a new window")

# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened
btn.bind("<Button>",
         lambda e: NewWindow(master))

btn.pack(pady=10)

frame1 = NewWindow(master)
frame1.pack(padx=10, pady=10)

# mainloop, runs infinitely
master.mainloop()
