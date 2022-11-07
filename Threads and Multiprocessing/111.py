import threading
import time
import queue
import tkinter as tk
from tkinter import constants as const
from tkinter import scrolledtext as stext
from tkinter import font as tkfont

global root
global q
global scrText

def thread_proc():

    for i in range(20):
        if i==0:
            x=0
            q.put(x)
            x+=1
        else:
            q.put(x)
            time.sleep(0.1)
            x += 1

def on_after_elapsed():
    while True:
        try:
            v = q.get(timeout=0.1)
        except:
            break
        scrText.insert(const.END, "value=%d\n" % v)
        scrText.see(const.END)
        scrText.update()
    root.after(100, on_after_elapsed)

root= tk.Tk()
q= queue.Queue(maxsize=0)
f= tkfont.Font(family='Courier New', size=12)
scrText = stext.ScrolledText(master=root, height=20, width=120, font=f)
scrText.pack(fill=const.BOTH, side=const.LEFT, padx=15, pady=15, expand=True)
th = threading.Thread(target=thread_proc)
th.start()
root.after(100, on_after_elapsed)
root.mainloop()
th.join()
## end of file #################################################################