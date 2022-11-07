from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root=Tk()
root.title('Codemy.com-Learn To Code')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('400x400')

#Databases

#Create a database or connect to one already existing
conn=sqlite3.connect('address_book.db')#not created yet, it does not exist yet so this command will create it for us
#this database that we will create is going to be saved in the same directory in which we are working

#Create cursor
c=conn.cursor()

#Create a table
#c.execute('''CREATE TABLE addresses(
 #   first_name text,
 #    last_name text,
 #    address text,
  #   city text,
  #   state text,
   #  zipcode integer
  #   )''')
#commenting out the table just because we dont want to recreate the table everytime we run it

#Create Edit Function to Update a Record
def update():
    # Create a database or connect to one already existing
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id=delete_box.get()

    c.execute('''UPDATE addresses SET
        first_name=:first,
        last_name=:last,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode
        
        WHERE oid=:oid''',
        {'first':f_name_editor.get(),
         'last':l_name_editor.get(),
         'address':address_editor.get(),
         'city':city_editor.get(),
         'state':state_editor.get(),
         'zipcode':zipcode_editor.get(),

         'oid':record_id
         })
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close

    editor.destroy()



def edit():
    global editor
    editor = Tk()
    editor.title('Update a Record')
    editor.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
    editor.geometry('400x200')

    # Create a database or connect to one already existing
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id=delete_box.get()
    # Query the database
    c.execute('SELECT * FROM addresses WHERE oid='+record_id)  # oid is the primary key
    records = c.fetchall()  # fetches all of the records; fetchone=catchesh the first record,fetchmany(50)-fetchesh the 50 records
    # print(c.fetchall())#normally we can do this but tkinter doesnt really work good with print
    # print(records)#printing a python list in which there is a python tuple inside with things that we can access by their index number

    # Loop Through Results
    print_records = ''

    #Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor



    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)


    # Create Text Box Labels
    f_name_label = Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a Save Button to Save Edited Record
    save_btn = Button(editor, text='Save Record', command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)




#Create Function to Delete a Record
def delete():
    # Create a database or connect to one already existing
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Delete a record
    c.execute('DELETE from addresses WHERE oid='+delete_box.get())#instead of oid we can put f_name='John' but this will delete every John we have in our database not the one we specifically want to be deleted

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close


#Create Submit Function for Database
def submit():
    # Create a database or connect to one already existing
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute('INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)',
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
            })
    # naming them the same as or widgets(ALWAYS
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close

    #Clear the Text Boxes
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create Query Functon
def query():
    # Create a database or connect to one already existing
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Query the database
    c.execute('SELECT *,oid FROM addresses') #oid is the primary key
    records=c.fetchall()#fetches all of the records; fetchone=catchesh the first record,fetchmany(50)-fetchesh the 50 records
    #print(c.fetchall())#normally we can do this but tkinter doesnt really work good with print
    #print(records)#printing a python list in which there is a python tuple inside with things that we can access by their index number

    #Loop Through Results
    print_records=''

    for record in records:
        print_records +=str(record[0])+' '+str(record[1])+' '+'\t'+str(record[6])+'\n'

    query_label=Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close

#Create Text Boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

#Create Text Box Labels
f_name_label=Label(root,text='First Name')
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text='Last Name')
l_name_label.grid(row=1,column=0)

address_label=Label(root,text='Address')
address_label.grid(row=2,column=0)

city_label=Label(root,text='City')
city_label.grid(row=3,column=0)

state_label=Label(root,text='State')
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text='Zipcode')
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text='Select ID')
delete_box_label.grid(row=9,column=0,pady=5)

#Creat Submit Buttons
submit_btn=Button(root,text='Add Record to Database',command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100) #ipadx=100->streching the button

#Create a Query Button
query_btn=Button(root,text='Show Records',command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=128)

#Create a Delete Button
delete_btn=Button(root,text='Delete Record',command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=128)

#Create an Update Button
edit_btn=Button(root,text='Edit Record',command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=132)

#Commit Changes
conn.commit()

#Close Connection
conn.close


root.mainloop()