from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title('Vezhba za GUI')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('1000x1000')

#Creating Frame1 with 2 buttons and a place for writing a text
def insert():
    return

def next():
    return

def previous():
    return

frame1=LabelFrame(root,padx=50,pady=50)
frame1.pack(padx=10,pady=10)

b1=Button(frame1,text='Next Frame',command=next)
b1.grid(row=4,column=3,pady=50)
b2=Button(frame1,text='Previous Frame',command=previous)
b2.grid(row=4,column=0,pady=50)


text=Entry(frame1,width=50)
text.grid(row=0,column=1)
text.insert(0,'Insert text')


#inserttextButton=Button(frame1,text='Insert text here',command=insert)
#inserttextButton.grid(row=1,column=1,stick=W+E+N+S)

#Open a picture from a folder in frame2

frame2=LabelFrame(root,padx=50,pady=50)
frame2.pack(padx=10,pady=10)

def open():

    global my_image
    frame2.filename = filedialog.askopenfilename(initialdir='/Users/Praksa/cats/images for GUI', title='Select a File',
                                               filetypes=(('jpg files', '*.jpg'), ('all files',
                                                                                   '*.* ')))  # this wont actually open a file, it ll just return the name of the file and the location of the file
    my_label = Label(frame2, text=frame2.filename).pack()  # returning the root.filename in this label
    my_image = ImageTk.PhotoImage(Image.open(frame2.filename))
    my_image_label = Label(image=my_image).pack()


my_btn=Button(frame2,text='Open file',command=open).pack()

#Creating a Drop Down Menu in Frame3
frame3=LabelFrame(root,padx=50,pady=50)
frame3.pack(padx=10,pady=10)



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

drop=OptionMenu(frame3,clicked,*options)
drop.pack()



#Creating Frame4 and showing the selected value from Frame3

frame4=LabelFrame(root,padx=50,pady=50)
frame4.pack(padx=10,pady=10)

def show():
    myLabel=Label(frame4,text=clicked.get()).pack()

myButton = Button(frame4, text='Show Selection', command=show).pack()

#Creating frame 5 with the text from frame1

frame5=LabelFrame(root,padx=50,pady=50)
frame5.pack(padx=10,pady=10)

def myClick():
    typed=text.get()
    myLabel=Label(frame5,text=typed)
    myLabel.pack()

b3=Button(frame5,text='You have typed: ',command=myClick)
b3.pack()



root.mainloop()