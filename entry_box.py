from tkinter import *

window = Tk()


def Submit():
    username = entry.get()
    if username:
        print("Hello "+username)
        delete()
        # entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)


def backspace():
    entry.delete(len(entry.get())-1,END)

entry = Entry(window,
              font=('Arial',50),
              fg="Green",
              bg="Black",
              show="*")

# entry.insert(0,"Spongebob")
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="Submit",
                       font=("Arial",30),
                       command=Submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       font=("Arial",30),
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="Backspace",
                       font=("Arial",30),
                       command=backspace)
backspace_button.pack(side=RIGHT)




window.mainloop()