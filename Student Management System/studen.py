from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

responses = {
    "hi": "Welcome to English Public School......,How can i help you??",
    "result date": "Result yet not Published--Result declred within 2-3 days",
    "my roll no": "Updating Soon.....",
    "school fee": "Contact to Account section call on:1234567890",
    "admission start date":"1/07/2024",
    "admission end date":"15/07/2024"
}

def initialize_chat():
    chat_log.config(state='normal')
    chat_log.insert(tk.END, 'BOT: HI, HOW CAN I HELP YOU?\n\n')
    chat_log.config(state='disabled')
    
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I don't understand, sorry 'contact on 1234567890'")

def send_message():
    user_message = user_input.get()
    if user_message:
        chat_log.config(state='normal')
        chat_log.insert(tk.END, 'YOU: ' + user_message + "\n")
        bot_response = get_response(user_message)
        chat_log.insert(tk.END, 'BOT: ' + bot_response + '\n\n')
        chat_log.config(state='disabled')
        user_input.delete(0, tk.END)

def clear_chat():
    chat_log.config(state='normal')
    chat_log.delete(1.0, tk.END)
    chat_log.config(state='disabled')

root=Tk()

root.title('Welcome Student Page')
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



chat_log = tk.Text(root, width=50, height=20, state='disabled', bd=5, relief='solid')
chat_log.place(x=600, y=200)

user_input = tk.Entry(root, font=('times', 15), bd=5, width=40)
user_input.place(x=600, y=550)

send_button = tk.Button(root, text='Send', bg='black', fg='white', font=('times', 18), bd=5, width=15,command=send_message, height=1)
send_button.place(x=550, y=600)

clear_button = tk.Button(root, text='Clear Chat', bg='black', fg='white', font=('times', 18), bd=5, width=15,command=clear_chat, height=1)
clear_button.place(x=850, y=600)


initialize_chat()

root.mainloop()