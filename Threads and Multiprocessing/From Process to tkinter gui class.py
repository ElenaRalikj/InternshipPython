import multiprocessing
import time
import queue
import tkinter as tk
from tkinter import font as tkfont

#global root
global q

def square(numbers,q):
    for n in numbers:
        q.put(n*n)
        time.sleep(1)

class GUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.title_font=tkfont.Font(family='Helvetica',size=18,weight='bold',slant='italic')
        self.a=tk.StringVar()
        #self.root=tk.Tk()
        self.mylabel=tk.Label(self, textvariable=self.a).pack()
        self.elapsed()


    def elapsed(self):
        while True:
            try:
                v=q.get(timeout=0.1)
            except:
                break
            self.a.set("value=%d\n" % v)
        self.after(100,self.elapsed)

if __name__=='__main__':
    numbers=[1,2,3,4,5,6,7,8,9,10]
    #root=tk.Tk()
    q=multiprocessing.Queue()
    #f=tkfont.Font(family='Courier New',size=12)
    #a=tk.StringVar()
    #mylabel=tk.Label(root,textvariable=a).pack()
    th=multiprocessing.Process(target=square,args=(numbers,q))
    th.start()
    #root.after(100,elapsed)
    app=GUI()
    #self.after(100,self.elapsed)
    app.mainloop()
    th.join()