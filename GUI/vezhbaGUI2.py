from typing import Dict

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from PIL import ImageTk, Image
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #dict od tuka vlecnje ili drugiot nachin
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.dict={}
        print(self.dict)


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()







class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        self.text = tk.Entry(self, width=50)
        self.text.pack()
        self.text.insert(0, 'Insert text')

        button3=tk.Button(self,text='Show the Text',command=lambda:self.showtext())
        button3.pack()

    def showtext(self):
        b = self.text.get()
        self.controller.dict['Enteredtext'] = b

        print(self.controller.dict['Enteredtext'])
        self.myLabel = tk.Label(self, text=self.controller.dict['Enteredtext']).pack()



class PageTwo(tk.Frame):




    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        # create label so self.

        #self.my_image.filename = filedialog.askopenfilename(initialdir='/Users/Praksa/cats/images for GUI',
        #                                                   title='Select a File',
        #                                                   filetypes=(('jpg files', '*.jpg'), ('all files',
        #                                                                                       '*.* ')))
        self.w = tk.Canvas(self,
                   width=500,
                   height=500)
        self.w.pack()

        #
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page One",
                           command=lambda: controller.show_frame("PageOne"))
        button2.pack()

        button3 = tk.Button(self, text="Open a picture from a folder",
                            command=lambda: self.open1())
        button3.pack()

        button4 = tk.Button(self, text="Go to Page Three",
                            command=lambda: controller.show_frame("PageThree"))
        button4.pack()

    def open1(self):
         self.kakosi= filedialog.askopenfilename(initialdir='/Users/Praksa/cats/images for GUI',
                                                      title='Select a File',
                                                      filetypes=(('jpg files', '*.jpg'), ('all files',
                                                                                          '*.* ')))
         self.image = ImageTk.PhotoImage(Image.open(self.kakosi))
         self.w.create_image(50, 10, image=self.image, anchor=tk.NW)
         #self.newLabel = ImageTk.PhotoImage(Image.open(PageTwo.filename))

         #self.lable()
         print("HEHEHEHHE")

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.c=tk.StringVar(self)
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        button3 = tk.Button(self, text="Go to Page Four",
                            command=lambda: controller.show_frame("PageFour"))
        button3.pack()

        self.myButton = tk.Button(self, text='Show Selection', command=lambda:self.show11()).pack()

        self.options =[
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday'

        ]
        #drop-value :   Monday
        #entry text :  HDSHHDSJj

        self.clicked = tk.StringVar(self)
        self.clicked.set(self.options[0])

        self.drop = tk.OptionMenu(self, self.clicked, *self.options)
        self.drop.pack()

        choice=self.clicked.get()
        print(choice)

    def show11(self):
        a=self.clicked.get()
        self.controller.dict['DropValue']=a
        #print(a)
        print(self.controller.dict['DropValue'])
        self.myLabel = tk.Label(self, text=self.controller.dict['DropValue']).pack()

        #self.myLabel = tk.Label(self, text=lambda:self.clicked.get())
        #self.myLabel.pack()






    #def show1(self):
    #    print('asgasgasgag')
    #    c=self.clicked.get()
    #    print(c)
    #    return c


#instance=PageThree.show1



#PageThree_instance=PageThree()
#PageThree_instance.show()
#b_instance=PageThree(self.show1)
class PageFour(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kk=tk.StringVar(self)
        label = tk.Label(self, text="This is page 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page Three",
                            command=lambda: controller.show_frame("PageThree"))
        button2.pack()

        button3 = tk.Button(self, text="Go to Page Five",
                            command=lambda: controller.show_frame("PageFive"))
        button3.pack()
        # napravi label za da pokazes vrednost
        labelb=tk.Label(self,text='Show selection:',font=controller.title_font)
        labelb.pack(side='top',fill='x',pady=10)

        self.labelc = tk.Label(self, textvariable=self.kk, font=controller.title_font)
        self.labelc.pack(side='top', fill='x', pady=30)
        #PageThree_instance=PageThree()
        #self.PageThree_instance=PageThree

        button4 = tk.Button(self, text='Show Selection', command=lambda: self.pokazi())

        button4.pack()


    def pokazi(self):
        print(self.controller.dict['DropValue'])
        self.labelc=tk.Label(self,text=self.controller.dict['DropValue']).pack()



#page4_inst = PageFour(parent, controller, PageThree_inst)
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 5", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Page Four",
                            command=lambda: controller.show_frame("PageFour"))
        button2.pack()

        button3=tk.Button(self,text="Show the Text Entered in Frame1",command=lambda: self.pokazitext())
        button3.pack()
    def pokazitext(self):
        print(self.controller.dict['Enteredtext'])
        self.labeld = tk.Label(self, text=self.controller.dict['Enteredtext']).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()