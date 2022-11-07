from tkinter import *

root=Tk()
root.title('Codemy.com-Learn To Code')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('400x400')

class Elder:

    def __init__(self,master):
        myFrame=Frame(master)#master is the root
        myFrame.pack()

        self.myButton=Button(master,text='Click me',command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print('Look at you...you cicked a button')


e=Elder(root)#we are passing in our root window

root.mainloop()