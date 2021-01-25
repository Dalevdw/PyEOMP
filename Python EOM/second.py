import mysql.connector
from tkinter import *
from tkinter import messagebox
from time import strftime
from tkinter import *
import tkinter as tk
import mysql.connector


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def add_emplyees():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                   host='127.0.0.1', database='lifechoicesonline',
                                   auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    sql="insert into Users values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=('0',str(name.get()),str(surname.get()))

    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inserted')
    xy = mycursor.execute("select * from user")
    for i in mycursor:
        print(i)




root = tk.Tk()
root.geometry("400x400")
root.title("Registor Employees")
root.configure(bg="coral")


lblname = tk.Label(root, text="Full name:", )
lblname.place(x=50, y=20)
lblname.configure(bg="coral")

name = tk.Entry(root, width=45)
name.place(x=250, y=20, width=100)

lblsurname = tk.Label(root, text="Full surname:")
lblsurname.configure(bg="coral")
lblsurname.place(x=50, y=50)

surname = tk.Entry(root, width=35)
surname.place(x=250, y=50, width=100)

createbtn= tk.Button(root, text="Sign In", bg='purple', fg="white", command=add_emplyees)
createbtn.place(x=135, y=300, width=150)


lbl = Label(root, font=('calibri', 15, 'bold'), background='purple', foreground='white')
lbl.configure(bg="coral")
lbl.place(x=135, y=355)
time()

root.mainloop()
