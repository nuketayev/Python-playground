from tkinter import *
from tkinter import messagebox

window = Tk()

def click():
    messagebox.showerror(title='Error',message='Small pipi detected')
    # if messagebox.askyesno(title='Honest question',message='You agree?'):
    #     print("damn, appreacite your honesty")
    # else:
    #     print("lier")
    answer = messagebox.askyesnocancel(title='Honest question',message='You agree?')
    if (answer == True):
        print("damn, appreacite your honesty")
    elif (answer == False):
        print("lier")
    else:
        print("Answer the question puta madre!")


button = Button(window,command=click,text="Click me")
button.pack()


window.mainloop()