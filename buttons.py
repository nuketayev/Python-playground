from tkinter import *

window = Tk()

count = 0

def click():
    global count
    count +=1
    print("You clicked",count,"times")


photo = PhotoImage(file='r.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg='Red',
                bg='black',
                activebackground='black',
                activeforeground='red',
                image=photo,
                compound='bottom')


button.pack()

window.mainloop()