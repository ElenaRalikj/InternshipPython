from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')

frame=LabelFrame(root,padx=50,pady=50)#puts padding inside of the frame
frame.pack(padx=10,pady=10)#puts padding outside of the frame

b=Button(frame,text='Dont Click Here')
b2=Button(frame,text='....or here')
b.grid(row=0,column=0)
b2.grid(row=1,column=1)



root.mainloop()