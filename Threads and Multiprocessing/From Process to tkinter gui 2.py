#import multiprocessing
#import time
#import queue
#import tkinter as tk
#from tkinter import font as tkfont

#def square(numbers,q)
#    for n in numbers:
#        q.put(n*n)
#
#if __name__=='__main__':
#    numbers=[1,2,3,4,5,6,7,8,9,10]
#    q=multiprocessing.Queue()
#    p=multiprocessing.Process(target=square,args=(numbers,q))
#
#    p.start()
#    p.join()

import multiprocessing
import time
import queue
import tkinter as tk
from tkinter import font as tkfont

global root
global q

def square(numbers,q):
    for n in numbers:
        q.put(n*n)
        time.sleep(1)



def elapsed():
    while True:
        try:
            v=q.get(timeout=0.1)
        except:
            break
        a.set("value=%d\n" % v)
    root.after(100,elapsed)

if __name__=='__main__':
    numbers=[1,2,3,4,5,6,7,8,9,10]
    root=tk.Tk()
    q=multiprocessing.Queue()
    f=tkfont.Font(family='Courier New',size=12)
    a=tk.StringVar()
    mylabel=tk.Label(root,textvariable=a).pack()
    th=multiprocessing.Process(target=square,args=(numbers,q))
    th.start()
    root.after(100,elapsed)
    root.mainloop()
    th.join()