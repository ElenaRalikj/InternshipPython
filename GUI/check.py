from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('400x400')#designing the dimensions of the box

def show():
    myLabel = Label(root, text=var.get()).pack()

#var=IntVar()#it needs  to be int because the value that we assign behind this variable is either 1 or 0
var=StringVar()

c=Checkbutton(root,text='Would you like to SuperSize your order? Check Here',variable=var,onvalue='SuperSize',offvalue='RegularSize')
c.deselect()#it starts with checkbutton not selected and is working well when we click the button Show Selection
c.pack()



myButton=Button(root,text='Show Selection',command=show).pack()

root.mainloop()