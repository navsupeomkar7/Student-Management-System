from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("About")

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

label=Label(frame,text='English Public School',font=('times',30),width=30,height=2,bg='white')
label.place(x=450,y=0)

about_frame = Frame(root, bg='white', width=800, height=200, bd=5)
about_frame.place(x=300, y=200)

about_text = """
About Us

Welcome to English Public School's Student Management System.\n
Our system streamlines student registration, login, and administrative tasks, ensuring a seamless experience for students and staff.\n
At English Public School, we prioritize academic excellence and efficient management to support our educational mission.
"""

about_label = Label(about_frame, text=about_text, font=('times', 20), bg='white', justify=LEFT, wraplength=750)
about_label.pack(padx=20, pady=20)

root.mainloop()