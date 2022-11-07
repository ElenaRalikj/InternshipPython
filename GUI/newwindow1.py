import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame1, text = 'Next Frame', width = 25, command = self.new_window)
        self.button1.grid(row=2,column=0)
        self.button2=tk.Button(self.frame1,text='Previous Frame',width=25,command=self.new_window)
        self.button2.grid(row=2,column=1)
        self.frame1.pack()
        self.text=tk.Entry(self.frame1,width=50)
        self.text.grid(row=0,column=0,columnspan=2)
        self.text.insert(0,'Insert text')



    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)



class Demo2(Demo1):
    def __init__(self, master,button1,button2,frame2,button3):
        super().__init__(button1,button2)
        #self.master = master
        self.frame2 = tk.Frame(self.master)
        self.button3 = tk.Button(self.frame2, text = 'Open Picture', width = 25, command=lambda:self.open)
        self.button3.grid(row=0,column=0,columnspan=2)
        self.frame2.pack()
        self.frame2.filename = filedialog.askopenfilename(initialdir='/Users/Praksa/cats/images for GUI',
                                                          title='Select a File',
                                                          filetypes=(('jpg files', '*.jpg'), ('all files', '*.* ')))

    def open(self):
        global my_image
        #self.frame2.filename = filedialog.askopenfilename(initialdir='/Users/Praksa/cats/images for GUI',title='Select a File',filetypes=(('jpg files', '*.jpg'), ('all files','*.* ')))
        self.my_label = tk.Label(self.frame2, text=self.frame2.filename).pack()
        self.my_image = tk.ImageTk.PhotoImage(Image.open(self.frame2.filename))
        self.my_image_label = tk.Label(image=self.my_image).pack()



    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

print(help(Demo2))
print(issubclass(Demo2,Demo1))
def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()



