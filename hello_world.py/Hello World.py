# Hello World
# made by @carsoncomputer on GitHub

from tkinter import *

def button_command():
    print("Hello World!")
    Toplevel()

window= Toplevel()
window.geometry("200x200")
window.title("hello world")
icon = PhotoImage(file='Image3.gif')
window.iconphoto(True,icon)
window.config(background=("#28d6fc"))
label = Label(window,
              text="made by someone",
              font=('Arial',40,'bold'),
              fg='#28d6fc',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              compound='bottom')
label.pack()

Button(window,text="hello world",command=button_command).pack()

window.mainloop()
