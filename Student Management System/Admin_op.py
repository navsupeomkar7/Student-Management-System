from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call
root=Tk()

root.title('Admin Page')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

root.configure(bg='skyblue')

frame =Frame(root,bg='white',width=10000,height=120,bd=5)
frame.place(x=0,y=0)

image2=Image.open('login_s.jpg')
image2=image2.resize((100,100),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label=Label(frame,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)


image2=Image.open('icon.png')
image2=image2.resize((100,100),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label=Label(frame,image=background_image)
background_label.image=background_image
background_label.place(x=1400,y=0)

label=Label(frame,text='English Public School',font=('times',30),width=30,height=2,bg='white')
label.place(x=450,y=0)

def Add():
    call(['python','Admission_form.py'])
    
def Update():
    call(['python','Update_student.py'])
    
def Delete():
    call(['python','Delete_student.py'])
    
def View():
    call(['python','View_student.py'])
    


button1=Button(root, text='Add Student', bg='white', fg='black', font=('times', 18),bd=5, width=15,command=Add, height=1)
button1.place(x=150, y=540)

button2=Button(root, text='Update Student', bg='white', fg='black', font=('times', 18),bd=5, width=15,command=Update, height=1)
button2.place(x=400, y=540)

button3=Button(root, text='Delete Student', bg='white', fg='black', font=('times', 18),bd=5, width=15,command=Delete, height=1)
button3.place(x=650, y=540)

button4=Button(root, text='View All', bg='white', fg='black', font=('times', 18),bd=5, width=15,command=View, height=1)
button4.place(x=900, y=540)


root.mainloop()


