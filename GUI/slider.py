from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('400x400')#designing the dimensions of the box

vertical=Scale(root,from_=0,to=200)#the scale widget is for creating the slider widget
#we can not pack it on it's own line because it will screw some things later
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+ 'x'+str(vertical.get()))

horizontal=Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

my_label=Label(root,text=horizontal.get()).pack()#only like this it does not change automatically, we slide the horizontal slider but the number is not chaning, that s why we need to create a function


my_btn=Button(root,text='Click me',command=slide).pack()


root.mainloop()