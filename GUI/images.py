from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')

#tkinter supports only 2 types of images, gif and pnm (probably), so to use real images like jpg and png files we have to import a whole other module
#we need to import pil-python image library but cause it's old it doesnt really work anymore
#there a new one called pillow which we ll use it

my_img=ImageTk.PhotoImage(Image.open('C:/Users/Praksa/cats/poodles.jpg'))
my_label=Label(image=my_img)
my_label.pack()


button_quit=Button(root,text='Exit Program',command=root.quit)
button_quit.pack()

root.mainloop()