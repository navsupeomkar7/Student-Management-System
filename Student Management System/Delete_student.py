from tkinter import *
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3
from subprocess import call

root = Tk()
root.title('Delete Student')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

root.configure(bg='skyblue')

email = StringVar()

def delete_student():
    with sqlite3.connect('Student_Management.db') as db:
        c = db.cursor()

        find_entry = 'SELECT * FROM reg WHERE Email = ?'
        c.execute(find_entry, [email.get()])
        result = c.fetchall()
        if result:
            delete_query = 'DELETE FROM reg WHERE Email = ?'
            c.execute(delete_query, [email.get()])
            db.commit()
            ms.showinfo("Message", "Student deleted successfully")
            root.destroy()
            call(['python', 'Admin_op.py'])
        else:
            ms.showerror('Oops', 'Email does not match')

frame = Frame(root, bg='white', width=10000, height=120, bd=5)
frame.place(x=0, y=0)

image2 = Image.open('login_s.jpg')
image2 = image2.resize((100, 100), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)
background_label = Label(frame, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

label = Label(frame, text='English Public School', font=('times', 30), width=30, height=2, bg='white')
label.place(x=450, y=0)

label = Label(root, text='Email:', font=('times', 15), width=15, height=1, bg='skyblue')
label.place(x=50, y=180)

entry = Entry(root, font=('times', 15), bd=2, width=30, textvariable=email)
entry.place(x=200, y=180)

button = Button(root, text='DELETE', bg='white', fg='black', font=('times', 18), bd=1, width=15, command=delete_student, height=1)
button.place(x=200, y=280)

root.mainloop()
