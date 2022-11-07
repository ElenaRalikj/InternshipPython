from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root=Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')

def open():

    global my_image
    root.filename = filedialog.askopenfilename(initialdir='/Users/Praksa/cats/images for GUI', title='Select a File',
                                               filetypes=(('jpg files', '*.jpg'), ('all files',
                                                                                   '*.* ')))  # this wont actually open a file, it ll just return the name of the file and the location of the file
    my_label = Label(root, text=root.filename).pack()  # returning the root.filename in this label
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn=Button(root,text='Open file',command=open).pack()


root.mainloop()