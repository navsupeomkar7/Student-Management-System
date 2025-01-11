from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call
import sqlite3
from tkinter import messagebox as ms

root=Tk()


root.title('Student Login')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

image1=Image.open('login.jpg')
image1=image1.resize((1520,1520),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

frame =Frame(root,bg='white',width=10000,height=120,bd=5)
frame.place(x=0,y=0)


email=tk.StringVar()
password=tk.StringVar()

def login():

      with sqlite3.connect('Student_Management.db') as db:
          c = db.cursor()

          find_entry = ('SELECT * FROM reg WHERE Email = ? and Password = ?')
          c.execute(find_entry, [(email.get()), (password.get())])
          result = c.fetchall()
          print(result)

          if result:
             msg = "login successfully"
             print(msg)
             ms.showinfo("messege", "LogIn sucessfully")

             root.destroy()
             
             from subprocess import call
             call(['python','studen.py'])
             
          else:
              ms.showerror('Oops','Email $ Password does not match')


image2=Image.open('login_s.jpg')
image2=image2.resize((100,100),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label=Label(frame,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

label=Label(frame,text='English Public School',font=('times',30),width=30,height=2,bg='white')
label.place(x=450,y=0)

logo_image = Image.open('login_f.jpg')
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(root, image=logo_photo, bg='skyblue')
logo_label.image = logo_photo
logo_label.place(x=1100, y=90)

login_frame = Frame(root, bg='skyblue')
login_frame.place(x=950, y=194)

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

button_log = Button(login_frame, text='Login', font=('times', 18), width=15, bd=2,command=login, bg='white', fg="black")
button_log.grid(row=3, column=0, columnspan=2, pady=10)




root.mainloop()