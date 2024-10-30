from tkinter import *

def submit():
    ttext = text.get("1.0",END)
    print(ttext)


window = Tk()

text = Text(window,
            bg="Black",
            fg="green",
            font=("Arial",25),
            height=8,
            width=20,
            padx=20,
            pady=20)
text.pack()

button = Button(window, text="Submit",command=submit)
button.pack()
window.mainloop()