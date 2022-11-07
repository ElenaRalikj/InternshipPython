import tkinter as tk
from tkcalendar import DateEntry

root=tk.Tk()
root.geometry('500x500')

cal=DateEntry(root,selectmode='day')
cal.grid(row=8,column=6,padx=15)

root.mainloop()

