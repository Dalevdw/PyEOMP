from tkinter import *
import mysql.connector


def sigin():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                   host='127.0.0.1', database='lifechoicesonline',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()

    sql = "insert into Users values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ('0', str(nameEnt.get()), str(surnameEnt.get()), str(genderEnt.get()),str(dateEnt.get()), str(roleEnt.get()), usernameEnt.get(), passwordEnt.get())

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, 'record inserted')
    x = mycursor.execute("select * from Users")
    for i in mycursor:
        print(i)


root = Tk()
root.geometry("450x300")
root.title("Student")
root.configure(background="teal")

namelbl = Label(root, text="Name:")
namelbl.place(x=50, y=20)
namelbl.configure(background="teal")

nameEnt = Entry(root, width=45)
nameEnt.place(x=200, y=20)

surnamelbl = Label(root, text='Surname:')
surnamelbl.configure(background="teal")
surnamelbl.place(x=50, y=50)

surnameEnt = Entry(root, width=45)
surnameEnt.place(x=200, y=50)

genderlbl = Label(root, text="Gender:")
genderlbl.place(x=50, y=80)
genderlbl.configure(background="teal")

genderEnt = Entry(root, width=45)
genderEnt.place(x=200, y=80)

rolelbl = Label(root, text="Role:")
rolelbl.place(x=50, y=120)
rolelbl.configure(background="teal")

roleEnt = Entry(root, width=45)
roleEnt.place(x=200, y=120)

datelbl = Label(root, text="Date:")
datelbl.place(x=50, y=160)
datelbl.configure(background="teal")

dateEnt = Entry(root, width=45)
dateEnt.place(x=200, y=160)

usernamelbl = Label(root, text="Username:")
usernamelbl.place(x=50, y=190)
usernamelbl.configure(background="teal")

usernameEnt = Entry(root, width=45)
usernameEnt.place(x=200, y=190)

passwordlbl = Label(root, text="Password:")
passwordlbl.place(x=50, y=240)
passwordlbl.configure(background="teal")

passwordEnt = Entry(root, width=45)
passwordEnt.place(x=200, y=240)


signbtn = Button(root, text="Sign in", command=sigin)
signbtn.place(x=50, y=290)

root.mainloop()
