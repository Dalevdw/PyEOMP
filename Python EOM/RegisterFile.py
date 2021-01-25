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
    val=('0',str(name.get()),str(surname.get()),str(date.get()),str(gender.get()),str(category.get()),str(username.get()),str(password.get()))

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

createbtn= tk.Button(root, text="Sign Employee In", bg='purple', fg="white", command=add_emplyees)
createbtn.place(x=135, y=300, width=150)

lbldate =tk.Label(root, text="Enter Date:")
lbldate.configure(bg="coral")
lbldate.place(x=50, y=80)

date =tk.Entry(root,width=35)
date.place(x=250,y=80,width=100)

lblgender = tk.Label(root, text="Enter Gender:")
lblgender.configure(bg="coral")
lblgender.place(x=50, y=110)

gender = tk.Entry(root,width=35)
gender.place(x=250, y=110, width=100)

lblcategory = tk.Label(root,text="Employee/Student/Visitor:")
lblcategory.configure(bg="coral")
lblcategory.place(x=50, y=140)

category = tk.Entry(root,width=35)
category.place(x=250,y=140,width =100)

lblusername= tk.Label(root,text=" Create Username:")
lblusername.configure(bg="coral")
lblusername.place(x=50, y=170)

username = tk.Entry(root,width=35)
username.place(x=250,y=170, width=100)

lblpassword = tk.Label(root,text="Enter Password:")
lblpassword.configure(bg="coral")
lblpassword.place(x=50, y=200)

password =tk.Entry(root,width=35)
password.place(x=250, y=200, width=100)

lbl = Label(root, font=('calibri', 15, 'bold'), background='purple', foreground='white')
lbl.configure(bg="coral")
lbl.place(x=135, y=355)
time()

root.mainloop()
