from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms

root = Tk()
root.title("Contact")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

root.configure(bg='skyblue')

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

Name = StringVar()
Email = StringVar()
Message = StringVar()

def insert():
    nam = Name.get()
    emai = Email.get()
    mess = message_text.get("1.0", "end-1c")
    if not nam.strip() or not emai.strip() or not mess.strip():
        ms.showinfo("Error!", "Name, email, and message cannot be blank")
        return
    db = sqlite3.connect('Student_Management.db')
    cursor = db.cursor()
    find_user = 'SELECT * FROM reg WHERE Name=? AND Email=?'
    cursor.execute(find_user, [(Name.get()), (Email.get())])
    result = cursor.fetchall()
    if not result:
        ms.showinfo("Error!", "Name and email could not be matched")
        return
    else:
        insert_query = 'INSERT INTO contactus(Name, Email, Message) VALUES(?, ?, ?);'
        user_data = (nam, emai, mess)
        cursor.execute(insert_query, user_data)
        db.commit()
        db.close()
        ms.showinfo("Success", "Message submitted successfully")

sub_label = Label(root, text="Contact Us", bg="skyblue", width=20, height=2, fg="Black", font=("times", 30))
sub_label.place(x=40, y=120)

name1_label = Label(root, text="Name", bg="skyblue", width=15, height=1, fg="black", font=("times", 15))
name1_label.place(x=40, y=230)

name1entry = Entry(root, bg="white", width=30, font=("times", 15), textvariable=Name)
name1entry.place(x=250, y=230)

email1_label = Label(root, text="Email", bg="skyblue", width=15, height=1, fg="black", font=("times", 15))
email1_label.place(x=40, y=290)

email1entry = Entry(root, bg="white", width=30, font=("times", 15), textvariable=Email)
email1entry.place(x=250, y=290)

message1_label = Label(root, text="Message", bg="skyblue", width=15, height=1, fg="black", font=("times", 15))
message1_label.place(x=40, y=350)

message_text = Text(root, bg="white", height=8, width=55, font=("times", 15))
message_text.place(x=250, y=350)

button = Button(root, text="Send Message", bg="white", width=15, height=1, fg="black", font=("times", 15), command=insert)
button.place(x=250, y=600)

root.mainloop()
