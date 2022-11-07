from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')

def open():
    global my_img
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
    # lbl=Label(top,text='Hello World').pack()
    my_img = ImageTk.PhotoImage(Image.open('C:/Users/Praksa/cats/images for GUI/poodles.jpg'))
    my_label = Label(top, image=my_img).pack()
    btn2=Button(top,text='close window',command=top.destroy).pack()

btn=Button(root,text='Open Second Window',command=open).pack()




mainloop()