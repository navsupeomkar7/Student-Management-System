from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from subprocess import call
from tkinter import messagebox as ms
root=Tk()

root.title('Admin Login')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

image1=Image.open('alo.png')
image1=image1.resize((900,900),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=250,y=0)

email=tk.StringVar()
password=tk.StringVar()

def login2():

      with sqlite3.connect('Student_Management.db') as db:
          c = db.cursor()

          find_entry = ('SELECT * FROM adreg WHERE Email = ? and Password = ?')
          c.execute(find_entry, [(email.get()), (password.get())])
          result = c.fetchall()
          print(result)

          if result:
             msg = "login successfully"
             print(msg)
             ms.showinfo("messege", "LogIn sucessfully")

             root.destroy()
             
             from subprocess import call
             call(['python','Admin_op.py'])
             
          else:
              ms.showerror('Oops','Email $ Password does not match')
    
frame =Frame(root,bg='white',width=10000,height=120,bd=5)
frame.place(x=0,y=0)

label=Label(frame,text='English Public School',font=('times',30),width=30,height=2,bg='white')
label.place(x=450,y=0)

image2=Image.open('login_s.jpg')
image2=image2.resize((100,100),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label=Label(frame,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

login_frame = Frame(root, bg='skyblue')
login_frame.place(x=1080, y=120)

welcome_label = Label(login_frame, text='Welcome! Please login to continue.', bg='skyblue', font=('times', 20))
welcome_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)  


email_label = Label(login_frame, text="E-mail:", bg='skyblue', font=('times', 20))
email_label.grid(row=1, column=0, padx=20, pady=10)
email_entry = Entry(login_frame, font=('times', 15), bd=2,textvariable=email)
email_entry.grid(row=1, column=1, padx=20, pady=10)


password_label = Label(login_frame, text="Password:", bg='skyblue', font=('times', 20))
password_label.grid(row=2, column=0, padx=20, pady=10)
password_entry = Entry(login_frame, font=('times', 15), bd=2, show='*',textvariable=password)
password_entry.grid(row=2, column=1, padx=20, pady=10)

button_log = Button(login_frame, text='Login', font=('times', 18), width=15,command=login2, bd=2, bg='white', fg="black")
button_log.grid(row=3, column=0, columnspan=2, pady=10)



root.mainloop()