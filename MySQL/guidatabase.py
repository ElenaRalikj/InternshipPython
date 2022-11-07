import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime

from datetime import datetime



#libdb = mysql.connector.connect(
#    host='localhost',
#    user='elena',
#    password='elena',
#    database='librarytest',
#)

#my_cursor = libdb.cursor()
#my_cursor.execute('CREATE TABLE books (firstname VARCHAR(255),lastname VARCHAR(255),bookname VARCHAR(255),datewhentaken DATETIME, datewhenreturned DATETIME,user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')
#my_cursor.execute('SHOW TABLES')



class library(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.title_font=tkfont.Font(family='Helvetica',size=18,weight='bold',slant='italic')
        self.geometry('2100x1000')
        self.config(bg='light blue')
        myframe=tk.Frame(self)
        #myframe.pack(side='top',fill='both',expand=True)
        self.libdb = mysql.connector.connect(
            host='localhost',
            user='elena',
            password='elena',
            database='librarytest',
        )

        self.my_cursor = self.libdb.cursor()
        myframe.grid_rowconfigure(0,weight=1)
        myframe.grid_columnconfigure(0,weight=1)
        mylabel=tk.Label(self, text='Library')
        mylabel.grid(row=2,column=0,columnspan=5,pady=50)
        self.e1=tk.Entry(self,width=50)
        self.e1.grid(row=4,column=0,padx=10,ipadx=20)
        self.e1.insert

        self.e1label=tk.Label(self,text='Enter your first name: ')
        self.e1label.grid(row=3,column=0)

        self.e2 = tk.Entry(self, width=50)
        self.e2.grid(row=4,column=1,padx=10,ipadx=20)
        self.e2.insert

        self.e2label = tk.Label(self, text='Enter your last name: ')
        self.e2label.grid(row=3, column=1)

        self.e3 = tk.Entry(self, width=50)
        self.e3.grid(row=4,column=2,padx=10,ipadx=20)


        self.e3label = tk.Label(self, text='Enter the name of the book: ')
        self.e3label.grid(row=3, column=2)

        #self.e4=tk.Label(self,width=50)
        #self.e4.grid(row=5,column=3,padx=10,ipadx=20)


        #self.e4=(self,text=('{n},{m},':',{l},':',{o}'))

        #self.e4 = tk.Entry(self, width=50)
        #self.e4.grid(row=4,column=3,padx=10,ipadx=20)
        #self.e4.insert(0, 'Enter the date and time when the book was taken: ')

        #self.e5 = tk.Entry(self, width=50)
        #self.e5.grid(row=4,column=4,padx=10,ipadx=20)
        #self.e5.insert(0, 'Enter the date and time when the book was returned: ')
        self.hey=tk.StringVar()


        self.b1=tk.Button(self,text='Insert',command=lambda:self.Insert())
        self.b1.grid(row=6,column=1,padx=40,pady=60,ipadx=60,ipady=60)

        self.b2 = tk.Button(self, text='Update',command=lambda:self.Update())
        self.b2.grid(row=6, column=2, padx=40,pady=60,ipadx=60,ipady=60)

        self.b3 = tk.Button(self, text='Delete',command=lambda:self.Delete())
        self.b3.grid(row=6, column=3, padx=40,pady=60,ipadx=60,ipady=60)

        self.d = tk.Entry(self, width=50,textvariable=self.hey)
        self.d.grid(row=8, column=3, padx=10, ipadx=20)

        #self.d.insert(self,textvariable=self.hey)
        #self.label=tk.Label(self,textvariable=self.hey)
        #self.label.grid(row=8, column=3, padx=40, pady=60, ipadx=60, ipady=60)

        #self.z=timeanddate()

        self.b4 = tk.Button(self, text='Choose Date When Taken/Returned', command=lambda:self.pokazi())
        self.b4.grid(row=4, column=3, padx=10, pady=10, ipadx=30, ipady=30)

        #self.b5 = tk.Button(self, text='Choose Date When Returned', command=lambda: self.pokazi())
        #self.b5.grid(row=4, column=4, padx=10, pady=10, ipadx=30, ipady=30)

        #self.b5 = tk.Button(self, text='Choose Date When Returned', command=timeanddate())
        #self.b5.grid(row=4, column=4, padx=10, pady=10, ipadx=30, ipady=30)

        #Table Treeview
        scroll_y=tk.Scrollbar(self,orient='vertical')

        self.user_records=ttk.Treeview(self,height=12,columns=('fn','ln','bn','dwt','dwr','uid'),yscrollcommand=scroll_y.set)

        scroll_y.grid(row=7,column=3)

        self.user_records.heading('fn',text='Firstname')
        self.user_records.heading('ln', text='Lastname')
        self.user_records.heading('bn', text='Bookname')
        self.user_records.heading('dwt', text='DateWhenTaken')
        self.user_records.heading('dwr', text='DateWhenReturned')
        self.user_records.heading('uid', text='UserID')

        self.user_records['show']='headings'

        self.user_records.column('fn',width=60)
        self.user_records.column('ln', width=60)
        self.user_records.column('bn', width=85)
        self.user_records.column('dwt', width=110)
        self.user_records.column('dwr', width=110)
        self.user_records.column('uid', width=30)

        self.user_records.grid(row=7,column=2)

        self.elena()
    def pokazi(self):
        self.z=timeanddate()





        #self.click()
    def prikazi(self,*args):
        #print("HELOOOOO")
        print(args)
        #self.Firstname=tk.StringVar()
        #self.Lastname=tk.StringVar()
        #self.Bookname = tk.StringVar()
        #self.DateWhenTaken = tk.StringVar()
        #self.DateWhenReturned = tk.StringVar()
        #self.StudentID = tk.StringVar()
        #self.testing()


    def elena(self):

        self.my_cursor.execute("SELECT * FROM librarytest.books;")
        result = self.my_cursor.fetchall()
        if len(result) != 0:
            self.user_records.delete(*self.user_records.get_children())
            for row in result:
                self.user_records.insert('', tk.END, values=row)
        self.after(1000,self.elena)

    def Insert(self):
        self.a=self.e1.get()
        self.b=self.e2.get()
        self.c=self.e3.get()
        self.k=self.d.get()
        #n,m,l,o=self.z.send_to_clas()
        self.hey.set(self.z.send_to_clas())
        self.aka=str(self.hey.get())
        #self.hey.strftime('%HH:%MM:%SS')
        #print(n,m,l,o)

        print(self.k)
        #date_time_str =self.k

        #date_time_obj = datetime.strptime(date_time_str,'%y-%m-%d %H:%M:%S')

        #print(date_time_obj)

        self.my_cursor.execute('INSERT INTO books (firstname,lastname,bookname,datewhentaken) VALUES (%s,%s,%s,%s)',(
        self.a,
        self.b,
        self.c,
        self.hey.get(), #mora da se zeme so get(go zima stringot) inaku bez get go zima kako object ili instanca
        ))
        self.libdb.commit()


    #def click(self):
        #viewInfo=self.user_records.focus()
        #learnerData=self.user_records.item(viewInfo)
        #row=learnerData['values']
        #self.a.set(row=[0])
        #self.b.set(row=[1])
        #self.c.set(row=[2])
        #self.d.set(row=[3])
        #self.e.set(row=[4])



    def Update(self):
        print(self.hey.get())
        print(self.e3.get())
        self.l = self.d.get()
        self.hey.set(self.z.send_to_clas())
        #self.my_cursor.execute("SELECT * FROM books WHERE bookname='%s'",self.e3.get())

        #row=self.my_cursor.fetchall()

        #self.e5.set()
        try:
            self.my_cursor.execute("""Update books set datewhenreturned = %s where bookname=%s""",(
            self.hey.get(),
            self.e3.get(),
            ))

            self.libdb.commit()
            tk.messagebox.showinfo('Data Entry Form', 'Record Updated Successfully')
        except:

            tk.messagebox.showinfo("ERROR")



    def Delete(self):
        self.my_cursor.execute("""Delete from books where bookname=%s""", (
            self.e3.get(),
        ))

        self.libdb.commit()
        tk.messagebox.showinfo('Data Entry Form', 'Record Deleted Successfully')

class timeanddate(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Time and Date Picker")
        self.geometry("500x400")
        self.config(bg="#cd950c")

        self.hour_string = tk.StringVar()
        self.min_string = tk.StringVar()
        self.last_value_sec=""
        self.last_value=""
        self.f=('Times',20)
        self.fone = tk.Frame(self)
        self.ftwo = tk.Frame(self)

        self.fone.pack(pady=10)
        self.ftwo.pack(pady=10)
        self.cal = Calendar(
            self.fone,
            selectmode="day",
            year=2021,
            month=2,
            day=3,
            date_pattern='yyyy-mm-dd'
        )
        self.cal.pack()



        self.min_sb = tk.Spinbox(
            self.ftwo,
            from_=0,
            to=23,
            wrap=True,
            textvariable=self.hour_string,
            width=2,
            state="readonly",
            font=self.f,
            justify=tk.CENTER,
            format="%02.0f"

        )


        self.sec_hour = tk.Spinbox(
            self.ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.min_string,
            font=self.f,
            width=2,
            justify=tk.CENTER,
            format ="%02.0f"
        )

        self.sec = tk.Spinbox(
            self.ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.sec_hour,
            width=2,
            font=self.f,
            justify=tk.CENTER,
            format="%02.0f"
        )

        self.min_sb.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.sec_hour.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.sec.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.msg = tk.Label(
            self,
            text="Hour  Minute  Seconds",
            font=("Times", 12),
            bg="#cd950c"
        )
        self.msg.pack(side=tk.TOP)

        self.actionBtn = tk.Button(
            self,
            text="Book Appointment",
            padx=10,
            pady=10,
            command=lambda: self. send_to_clas()
        )
        self.actionBtn.pack(pady=10)

        self.msg_display = tk.Label(
            self,
            text="",
            bg="#cd950c"
        )
        self.msg_display.pack(pady=10)

    def send_to_clas(self):
        self.g=self.cal.get_date()
        self.h =self.sec.get()
        self.i=self.min_sb.get()
        self.j=self.sec_hour.get()
        #self.i.lstrip()
        #self.i.rstrip()
        dateobject=self.g +' '+ self.i+':'+self.j+':'+self.h
        print(dateobject)
        #date_time_obj = datetime.strptime(dateobject, '%y-%m-%d %H:%M:%S')
        return  dateobject

    def display_msg(self):
        self.date = self.cal.get_date()
        self.m = self.min_sb.get()
        self.h = self.sec_hour.get()
        self.s = self.sec.get()
        self.t = f"Your appointment is booked for {self.date} at {self.m}:{self.h}:{self.s}."
        self.msg_display.config(text=self.t)

        if self.last_value =="59" and self.min_string.get() =="0":
            self.hour_string.set(int(self.hour_string.get()) + 1 if self.hour_string.get() != "23" else 0)
            self.last_value =self.min_string.get()

        if self.last_value_sec =="59" and self.sec_hour.get() =="0":
            self.min_string.set(int(self.min_string.get()) + 1 if self.min_string.get() != "59" else 0)
        if self.last_value =="59":
            self.hour_string.set(int(self.hour_string.get()) + 1 if self.hour_string.get() != "23" else 0)
            self.last_value_sec = self.sec_hour.get()



if __name__=='__main__':
    app=library()
    app.mainloop()
    #appp=timeanddate()
    #appp.mainloop()