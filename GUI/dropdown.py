from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Codemy.com-Learn to Code')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('400x400')

#Drop Down Boxes

def show():
    myLabel=Label(root,text=clicked.get()).pack()

options=[
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'

]

clicked=StringVar()
clicked.set(options[0])

drop=OptionMenu(root,clicked,*options)#there will be cases when we will have so many options so in that case it's the best to use a list
drop.pack()

myButton=Button(root,text='Show Selection',command=show).pack()

root.mainloop()