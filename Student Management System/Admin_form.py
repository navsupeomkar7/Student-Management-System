from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
root=Tk()

root.title('Admin Registration Form')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))
root.configure(bg='blue')
image1=Image.open('clerk.jpg')
image1=image1.resize((800,800),Image.ANTIALIAS)


background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

frame =Frame(root,bg='blue',width=600,height=800,bd=0)
frame.place(x=850,y=0)

logo_image = Image.open('icon.png')
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(frame, image=logo_photo, bg='blue')
logo_label.image = logo_photo
logo_label.place(x=200, y=20)

logo_image = Image.open('alo.png')
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(frame, image=logo_photo, bg='blue')
logo_label.image = logo_photo
logo_label.place(x=320, y=20)

adname=tk.StringVar()
adaddress=tk.StringVar()
adphoneno=tk.StringVar()
ademail=tk.StringVar()
adpassword=tk.StringVar()
adcpassword=tk.StringVar()

def insert2():
    
    nm=adname.get()
    ad=adaddress.get()
    ph=adphoneno.get()
    em=ademail.get()
    pw=adpassword.get()
    cp=adcpassword.get()

    
    #check validation
    with sqlite3.connect('Student_Management.db') as db:
        c=db.cursor()
    find_user=('SELECT * FROM adreg WHERE Name = ?')
    c.execute(find_user, [(adname.get())])
    
    import re
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,em)):
        a=True 
    else:
        a=False   
        
    if c.fetchall():
        print('try different username')
        ms.showerror('ERROR!!','username taken try differnt one.')
    elif (nm=="") or (nm.isdigit()):
        ms.showerror('ERROR!!','PLEASE ENTER NAME')
    elif ph=="":
        ms.showerror('ERROR!!','PLEASE ENTER PHONE NO')
    elif ad=="":
        ms.showerror('ERROR!!','PLEASE ENTER ADDRESS')
    elif em=="" or (a==False):
        ms.showerror('ERROR!!','PLEASE ENTER EMAIL')
    elif pw=="":
        ms.showerror('ERROR!!','PLEASE ENTER PASSWORD')
    elif (cp=="") or (pw!=cp):
        ms.showerror('ERROR!!','PLEASE ENTER CONFIRM PASSWORD')
    else:
        print('insert data in database')
        conn=sqlite3.connect('Student_Management.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute(
                'INSERT INTO adreg(Name,Address,Phone_No,Email,Password,Confirm_Password) VALUES(?,?,?,?,?,?)',
                (nm,ad,ph,em,pw,cp))
            conn.commit()
            conn.close()
            ms.showinfo('SUCCESS','ADMIN REGISTARATION SUCCESFULLY')
            window.destroy()
    
    

title=tk.Label(frame,text="Admin Registartion Form",font=("times",25),fg="black",bg='blue')
title.place(x=150,y=120)

label=Label(frame, text='Name:', font=('times', 15), width=15, height=1,bg='blue')
label.place(x=50, y=180)

entry=Entry(frame, font=('times', 15),bd=2, width=30,textvariable=adname)
entry.place(x=250, y=180)

label=Label(frame, text='Address:', font=('times', 15), width=15, height=1,bg='blue')
label.place(x=50, y=240)

entry=Entry(frame, font=('times', 15),bd=2, width=30,textvariable=adaddress)
entry.place(x=250, y=240)

label=Label(frame, text='Phone No:', font=('times', 15), width=15, height=1,bg='blue')
label.place(x=50, y=300)

entry=Entry(frame, font=('times', 15),bd=2, width=30,textvariable=adphoneno)
entry.place(x=250, y=300)

label=Label(frame, text='Email:', font=('times', 15), width=15, height=1,bg='blue')
label.place(x=50, y=360)

entry=Entry(frame, font=('times', 15),bd=2, width=30,textvariable=ademail)
entry.place(x=250, y=360)

label=Label(frame, text='Password:', font=('times', 15), width=15, height=1,bg='blue')
label.place(x=50, y=420)

entry=Entry(frame, font=('times', 15),bd=2, width=30,show='*',textvariable=adpassword)
entry.place(x=250, y=420)

label=Label(frame, text='Confirm Password:', font=('times', 15), width=15, height=1,bg='blue')
label.place(x=50, y=480)

entry=Entry(frame, font=('times', 15),bd=2, width=30,show='*',textvariable=adcpassword)
entry.place(x=250, y=480)


button=Button(frame, text='SUBMIT', bg='white', fg='black', font=('times', 18),bd=5, width=15, height=1,command=insert2)
button.place(x=200, y=540)





root.mainloop()