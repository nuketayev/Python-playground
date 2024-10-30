from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(title='Open file')
    file = open(filepath,'r')
    print(file)
    print(file.read())
    file.close()

def writetext():
    text.pack()
    Savetextbutton.pack()

def savetext():
    file = filedialog.asksaveasfile(initialdir="",
                                    defaultextension='.txt',
                                    filetypes=[("Text file",".txt"),
                                               ("HTML",".html"),
                                               ("All files",".*")])
    written = text.get("1.0",END)
    file.write(written)
    file.close()


window = Tk()

button = Button(window,text="Open a file",command=openfile)
button.pack()

textbutton = Button(window,text="Write text", command=writetext)
textbutton.pack()

Savetextbutton = Button(window, text="Save text to file",command=savetext)


text = Text(window,
            bg="Black",
            fg="Green",
            font=("Arial",25),
            height=10,
            width=20,
            padx=25,
            pady=25)

window.mainloop()