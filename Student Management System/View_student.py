from tkinter import *
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title('View All Students')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

def view_all_students():
    with sqlite3.connect('Student_Management.db') as db:
        c = db.cursor()
        find_entry = "SELECT * FROM reg"
        result = c.fetchall()
        print(result)
        db.commit()
        db.close()

root.configure(bg='skyblue')

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


student_list = Listbox(root, width=100, height=20)
student_list.place(x=450,y=200)


view_button = Button(root, text="View All",bg='white',fg='black',font=('times', 18),bd=1, width=15, command=view_all_students, height=1)
view_button.place(x=650,y=600)

root.mainloop()
