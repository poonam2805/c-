
import mysql.connector
from tkinter import *
from tkinter import messagebox

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bcasem5"
)

def insert_data():
    snm = txtsnm.get().strip()
    result = txtres.get().strip()
    mycursor = mydb.cursor()
    sql = "Insert Into stud(snm, result) values(%s, %s)"
    val = (snm, result)
    mycursor.execute(sql, val)
    mydb.commit()
    count = mycursor.rowcount
    mycursor.close()  # Close cursor after execution
    if count == 1:
        messagebox.showinfo("CRUD", "Record inserted")
        txtsnm.delete(0, END)
        txtres.delete(0, END)
    else:
        messagebox.showerror("CRUD", "No record inserted")
    txtsnm.focus()

def update_data():
    id = txtid.get().strip()
    snm = txtsnm.get().strip()
    result = txtres.get().strip()
    mycursor = mydb.cursor()
    sql = "UPDATE stud SET snm = %s, result = %s WHERE id = %s"
    val = (snm, result, id)
    mycursor.execute(sql, val)
    mydb.commit()
    count = mycursor.rowcount
    mycursor.close()  # Close cursor after execution
    if count > 0:
        messagebox.showinfo("CRUD", "Record updated")
        txtsnm.delete(0,END)
        txtres.delete(0,END)
        txtid.delete(0,END)
    else:
        messagebox.showerror("CRUD", "No record updated")
    txtsnm.focus()

def delete_data():
    id = txtid.get().strip()
    mycursor = mydb.cursor()
    sql = "DELETE FROM stud WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    count = mycursor.rowcount
    mycursor.close()  # Close cursor after execution
    if count > 0:
        messagebox.showinfo("CRUD", "Record deleted")
        txtsnm.delete(0, END)
        txtres.delete(0, END)
        txtid.delete(0, END)
    else:
        messagebox.showerror("CRUD", "No record deleted")
    txtsnm.focus()

def selectid():
    id = txtid.get().strip()
    if not id:
        messagebox.showerror("CRUD", "ID cannot be empty")
        return
    mycursor = mydb.cursor()
    sql = "SELECT * FROM stud WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    mycursor.close()  # Close cursor after execution
    if len(myresult) == 1:
        for x in myresult:
            txtsnm.delete(0, END)
            txtres.delete(0, END)
            txtsnm.insert(0, x[1])
            txtres.insert(0, x[2])
    else:
        messagebox.showerror("CRUD", "No record found")
    txtsnm.focus()

# Tkinter GUI
root = Tk()
Label(root, text="Enter ID").pack()
txtid = Entry(root)
txtid.pack()

Button(root, text="Search", command=selectid).pack()

Label(root, text="Enter Name").pack()
txtsnm = Entry(root)
txtsnm.pack()

Label(root, text="Enter Result").pack()
txtres = Entry(root)
txtres.pack()

Button(root, text="Add", command=insert_data).pack()
Button(root, text="Update", command=update_data).pack()
Button(root, text="Delete", command=delete_data).pack()

root.mainloop()
