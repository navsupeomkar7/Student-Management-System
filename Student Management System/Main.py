from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call
root=Tk()

root.title('Main Page')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))


frame =Frame(root,bg='white',width=10000,height=120,bd=5)
frame.place(x=0,y=0)

image2=Image.open('login_s.jpg')
image2=image2.resize((100,100),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label=Label(frame,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

label=Label(frame,text='English Public School',font=('times',30),width=30,height=2,bg='white')
label.place(x=450,y=0)

frame2 =Frame(root,bg='skyblue',width=10000,height=120,bd=5)
frame2.place(x=0,y=110)

def StudentReg():
    call(['python','Admission_form.py'])
    
def StudentLog():
    call(['python','Student_login.py'])
    
def AdminReg():
    call(['python','Admin_form.py'])
    
def AdminLog():
    call(['python','Admin_login.py'])

def About():
    call(['python','About.py'])
    
def Contact():
    call(['python','contact.py'])

button=Button(frame2, text='About Us', bg='white', fg='black', font=('times', 18),bd=0, width=15,command=About, height=1)
button.place(x=50, y=30)

button=Button(frame2, text='Stutent Registartion', bg='white', fg='black', font=('times', 18),bd=0, width=15, command=StudentReg , height=1)
button.place(x=290, y=30)

button=Button(frame2, text='Student Login', bg='white', fg='black', font=('times', 18),bd=0, width=15,command=StudentLog, height=1)
button.place(x=520, y=30)

button=Button(frame2, text='Admin Registartion', bg='white', fg='black', font=('times', 18),bd=0, width=15,command=AdminReg, height=1)
button.place(x=740, y=30)

button=Button(frame2, text='Admin Login', bg='white', fg='black', font=('times', 18),bd=0, width=15,command=AdminLog, height=1)
button.place(x=970, y=30)

button=Button(frame2, text='Contact', bg='white', fg='black', font=('times', 18),bd=0, width=15,command=Contact, height=1)
button.place(x=1190, y=30)

image4=Image.open('Main_photo.jpg')
image4=image4.resize((1525,600),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image4)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=228)


root.mainloop()


