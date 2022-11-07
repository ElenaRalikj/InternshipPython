import threading
import queue
import time
import tkinter as tk
from tkinter import constants as const
from tkinter import scrolledtext as stext
from tkinter import font as tkfont


global top
global q
global mylabel

def worker():
    item=1
    q.put(item)
    for item in range(5):
        q.put(item)
        time.sleep(1)
        item+=1
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()


def on_after_elapsed():
    while True:
        try:
            a = q.get(timeout=0.1)
        except:
            break
        scrText.insert(const.END, "value=%d\n" % a)
        scrText.see(const.END)
        scrText.update()
    top.after(100, on_after_elapsed)


top     = tk.Tk()
q=queue.Queue(maxsize=0)
f       = tkfont.Font(family='Courier New', size=12)
scrText = stext.ScrolledText(master=top, height=20, width=120, font=f)
scrText.pack(fill=const.BOTH, side=const.LEFT, padx=15, pady=15, expand=True)
# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()
top.after(100, on_after_elapsed)
top.mainloop()


# block until all tasks are done
q.join()
print('All work completed')