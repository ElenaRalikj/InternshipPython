import threading
import time
import queue
import tkinter as tk
from tkinter import font as tkfont

global root
global q

def thread():
    for i in range(20):
        if i==0:
            x=0
            q.put(x)
            x+=1
        else:
            q.put(x)
            time.sleep(0.1)
            x+=1

def elapsed():
    while True:
        try:
            v=q.get(timeout=0.1)
        except:
            break
        a.set("value=%d\n" % v)
    root.after(100,elapsed)

root=tk.Tk()
q=queue.Queue(maxsize=0)
f=tkfont.Font(family='Courier New',size=12)
a=tk.StringVar()
mylabel=tk.Label(root,textvariable=a).pack()
th=threading.Thread(target=thread)
th.start()
root.after(100,elapsed)
root.mainloop()
th.join()

