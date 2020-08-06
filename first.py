from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('vipin')
root.iconbitmap('C:/Users/vipin/Desktop/tkinter/image1.ico')
root.geometry('400x400')

con1 = sqlite3.connect('vipin.db')

c =con1.cursor()

'''
c.execute("""CREATE TABLE kabir (
           firstname text,
           lastname text,
           address text,
           city text,
           state text,
           zipcode integer
           )""")

'''

def update():
    con1 = sqlite3.connect('vipin.db')

    c = con1.cursor()
    recordid = deletebox.get()

    c.execute("""UPDATE kabir SET
        firstname = :first,
        lastname = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",

        {'first':fname2.get(),
         'last':lname2.get(),
         'address':address2.get(),
         'city':city2.get(),
         'state':state2.get(),
         'zipcode':zipcode2.get(),
         'oid': recordid

         })

    con1.commit()
    con1.close()

    editor.destroy()
    
def edit():
    global editor
    editor = Tk()
    editor.title('vipin')
    editor.iconbitmap('C:/Users/vipin/Desktop/tkinter/image1.ico')
    editor.geometry('400x400')

    con1 = sqlite3.connect('vipin.db')

    c = con1.cursor()

    recordid = deletebox.get()

    c.execute("SELECT *,oid FROM kabir WHERE oid = " + recordid) #if user do not enter in the idnumber entry then he will get error for this line
    rec1 = c.fetchall()
 
    global fname2
    global lname2
    global address2
    global city2
    global state2
    global zipcode2

    fname2 = Entry(editor, width=30)
    fname2.grid(row=0, column=1, padx=20, pady=(10, 0))

    lname2 = Entry(editor, width=30)
    lname2.grid(row=1, column=1, padx=20)

    address2 = Entry(editor, width=30)
    address2.grid(row=2, column=1, padx=20)

    city2 = Entry(editor, width=30)
    city2.grid(row=3, column=1, padx=20)

    state2 = Entry(editor, width=30)
    state2.grid(row=4, column=1, padx=20)

    zipcode2 = Entry(editor, width=30)
    zipcode2.grid(row=5, column=1, padx=20)

    deletebox2 = Entry(editor, width=30)
    deletebox2.grid(row=9, column=1)

    fname1 = Label(editor, text='first name')
    fname1.grid(row=0, column=0, pady=(10, 0))

    lname1 = Label(editor, text='lname')
    lname1.grid(row=1, column=0)

    address1 = Label(editor, text='address')
    address1 .grid(row=2, column=0)

    city1 = Label(editor, text='city')
    city1.grid(row=3, column=0)

    state1 = Label(editor, text='state')
    state1.grid(row=4, column=0)

    zipcode1 = Label(editor, text='zipcode')
    zipcode1.grid(row=5, column=0)

    #loop through records
    for rec in rec1:
              fname2.insert(0, rec[0])
              lname2.insert(0, rec[1])
              address2.insert(0, rec[2])
              city2.insert(0, rec[3])
              state2.insert(0, rec[4])
              zipcode2.insert(0, rec[5])

    editbtn = Button(editor, text='save records', command=update)
    editbtn.grid(row=6, column=1, columnspan=2, padx=10, pady=10, ipadx=100)


    
#create a function to delete a record
def delete():
    con1 = sqlite3.connect('vipin.db')

    c = con1.cursor()

    #delete a record
    c.execute('DELETE from kabir WHERE oid = ' + deletebox.get())
    deletebox.delete(0, END)
    
    con1.commit()

    con1.close()

def submit():
    con1 = sqlite3.connect('vipin.db')

    c = con1.cursor()

    c.execute('INSERT INTO kabir VALUES (:fname, :lname, :address, :city, :state, :zipcode)',
              {
                  'fname': fname.get(),
                  'lname': lname.get(),
                  'address' : address.get(),
                  'city' : city.get(),
                  'state' : state.get(),
                  'zipcode': zipcode.get()
                  
                  })
    con1.commit()

    con1.close()


    
    fname.delete(0, END)
    lname.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    con1 = sqlite3.connect('vipin.db')

    c = con1.cursor()

    c.execute("SELECT *, oid FROM kabir")
    rec1 = c.fetchall()
    #print(rec1)

    printR = ''

    for rec in rec1:
        printR += str(rec[0]) +' ' +str(rec[1]) +' ' +str(rec[2]) +' ' +str(rec[3]) +' '+ str(rec[4]) +' ' +str(rec[5]) +'\t' +str(rec[6]) +'\n'
    
    man = Label(root, text=printR)
    man.grid(row=12, column=0, columnspan=2)
    
    con1.commit()

    con1.close()

fname = Entry(root, width=30)
fname.grid(row=0, column=1, padx=20, pady=(10, 0))

lname = Entry(root, width=30)
lname.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

deletebox = Entry(root, width=30)
deletebox.grid(row=9, column=1)

fname1 = Label(root, text='first name')
fname1.grid(row=0, column=0, pady=(10, 0))

lname1 = Label(root, text='lname')
lname1.grid(row=1, column=0)

address1 = Label(root, text='address')
address1 .grid(row=2, column=0)

city1 = Label(root, text='city')
city1.grid(row=3, column=0)

state1 = Label(root, text='state')
state1.grid(row=4, column=0)

zipcode1 = Label(root, text='zipcode')
zipcode1.grid(row=5, column=0)

deletebox1 = Label(root, text='ID number')
deletebox1.grid(row=9, column=0) 

submitbtn = Button(root, text='add record to database', command=submit)
submitbtn.grid(row=6, column=1, columnspan=2, padx=10, pady=10, ipadx=100)

querybtn = Button(root, text='show records', command=query)
querybtn.grid(row=7, column=1, columnspan=2, padx=10, pady=10, ipadx=100)


deletebtn = Button(root, text='delete records', command=delete)
deletebtn.grid(row=10, column=1, columnspan=2, padx=10, pady=10, ipadx=100)

editbtn = Button(root, text='edit records', command=edit)
editbtn.grid(row=11, column=1, columnspan=2, padx=10, pady=10, ipadx=100)


con1.commit()
con1.close()
                           
root.mainloop()
