from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title('Update Student')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))
root.configure(bg='skyblue')

emails = StringVar()
address = StringVar()
phoneno = StringVar()
password = StringVar()


def search_student():
    email = emails.get()
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reg WHERE Email=?", (email,))
    student = cursor.fetchone()
    conn.close()
    if student:
        name_entry.delete(0, END)
        name_entry.insert(0, student[1])
        address_entry.delete(0, END)
        address_entry.insert(0, student[3])
        phone_entry.delete(0, END)
        phone_entry.insert(0, student[4])
        password_entry.delete(0, END)
        password_entry.insert(0, student[6])
    else:
        messagebox.showerror("Error", "Student not found")

def update_student():
    email = email_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE reg SET Name=?, Address=?, Phone_No=?, Password=? WHERE Email=?",
                   (name,address, phone, password, email))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student updated successfully")

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

email_entry = Entry(root, font=('times', 15), bd=2, width=30, textvariable=emails)
email_entry.place(x=200, y=180)

button = Button(root, text='Search', bg='white', fg='black', font=('times', 18), bd=1, width=15, command=search_student, height=1)
button.place(x=600, y=180)

label = Label(root, text='Name:', font=('times', 15), width=15, height=1, bg='skyblue')
label.place(x=50, y=240)

name_entry = Entry(root, font=('times', 15), bd=2, width=30)
name_entry.place(x=200, y=240)

label = Label(root, text='Gender:', font=('times', 15), width=15, height=1, bg='skyblue')
label.place(x=50, y=300)

r1 = Radiobutton(root, text="Male", value="Male", font=('times', 15), bg='skyblue')
r1.place(x=210, y=300)
r2 = Radiobutton(root, text="Female", value="Female", font=('times', 15), bg='skyblue')
r2.place(x=310, y=300)

label = Label(root, text='Address:', font=('times', 15), width=15, height=1, bg='skyblue')
label.place(x=50, y=360)

address_entry = Entry(root, font=('times', 15), bd=2, width=30, textvariable=address)
address_entry.place(x=200, y=360)

label = Label(root, text='Phone No:', font=('times', 15), width=15, height=1, bg='skyblue')
label.place(x=50, y=420)

phone_entry = Entry(root, font=('times', 15), bd=2, width=30, textvariable=phoneno)
phone_entry.place(x=200, y=420)

label = Label(root, text='Password:', font=('times', 15), width=15, height=1, bg='skyblue')
label.place(x=50, y=480)

password_entry = Entry(root, font=('times', 15), bd=2, width=30, show='*', textvariable=password)
password_entry.place(x=200, y=480)

button = Button(root, text='UPDATE', bg='white', fg='black', font=('times', 18), bd=5, width=15, command=update_student, height=1)
button.place(x=200, y=540)

root.mainloop()
