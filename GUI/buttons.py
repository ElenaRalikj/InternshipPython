from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text='Look! I click a Button')
    myLabel.pack()

myButton=Button(root,text='Click me',pady=50, command=myClick,fg='blue',bg='#000000')#fg=foreground color, bg=background color
myButton.pack()

root.mainloop()
