from tkinter import *

root=Tk()

e=Entry(root,width=50)
e.pack()
e.insert(0,'Enter your name: ')#index zero cause it s only one box, the zero index box

def myClick():
    hello='Hello ' +e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()

myButton=Button(root,text='Enter Your Stock Quote',command=myClick)
myButton.pack()






root.mainloop()

