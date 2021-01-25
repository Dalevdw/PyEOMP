import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
def verify():
    users = Username.get()
    passs = Password.get()
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()
def logged():
    messagebox.showinfo("Successful", "You have successfully logged")
    import second
    root.destroy()

#if login details are incorrect
def failed():
    messagebox.showerror("Error", "try again")
    Username.delete(0, END)
    Password.delete(0, END)


def register():
    import RegisterFile
    RegisterFile.mainloop()

#Design the login form
root = tk.Tk()
root.geometry("400x400")
root.title("Login Page")
root.configure(bg="coral")
lbluser = tk.Label(root, text="Please enter username", )
lbluser.place(x=50, y=20)
lbluser.configure(bg="coral")

Username = tk.Entry(root, width=45)
Username.place(x=250, y=20, width=100)
lblpassword = tk.Label(root, text="Please enter password ")
lblpassword.place(x=50, y=50)
lblpassword.configure(bg="coral")
Password = tk.Entry(root, width=35)
Password.place(x=250, y=50, width=100)

Loginbtn = tk.Button(root, text="Login", bg='purple', fg='white', command=verify)
Loginbtn.place(x=150, y=135, width=55)

Registerbtn = tk.Button(root, text="Register new user", bg='Purple', fg='white', command=register)
Registerbtn.place(x=250, y=135, width=150)

root.mainloop()
