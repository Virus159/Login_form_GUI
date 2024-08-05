import tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title = "Login Form"
root.geometry("450x450")
root.configure(bg='#333333')


frame = tkinter.Frame(bg='#333333')


def login():
    username = "Virus159"
    password = "159123"
    if username == username_entry.get() and password == pass_entry.get():
        messagebox.showinfo(title='Login success',message="You successfully logged in."
                                                          "")
    else:
        messagebox.showerror(title='Login error',message="Invalid username or password.")




login_label = Label(frame,text='Login', font=("inter", 30), fg="#1BFD9C", bg="#333333")



username_label = Label(frame,text='Username', font=("inter", 16), fg="#1BFD9C", bg="#333333")



username_entry = Entry(frame, font=("inter", 16))



pass_label = Label(frame, text="Password", font=("inter", 16), fg="#1BFD9C", bg="#333333")



pass_entry = Entry(frame, font=("inter", 16),show="*")



login_btn =  Button(frame, text="Login", bg="#1BFD9C", fg="#fff", font="inter,16",command=login)




login_label.grid(row=0, column=0, columnspan=2, pady=20)
username_label.grid(row=1, column=0, pady =20)
username_entry.grid(row=1, column=1)
pass_label.grid(row=2, column=0, pady=20)
pass_entry.grid(row=2, column=1)
login_btn.grid(row=3, column=0, columnspan=2, pady=20)



frame.pack()



root.mainloop()