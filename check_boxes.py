from tkinter import *

window = Tk()

x = IntVar()

photo = PhotoImage(file='r.png')

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree!")

check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='GReen',
                           bg='Black',
                           activebackground='Black',
                           activeforeground='Green',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')

check_button.pack()

window.mainloop()