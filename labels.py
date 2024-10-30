from tkinter import *

window = Tk()

photo = PhotoImage(file='r.png')

window.geometry("500x500")
window.config(background="Black")
label = Label(window,text="Hello World", 
              font=('Arial',40,'bold'),
              fg='Green',
              bg='Red',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()

window.mainloop()