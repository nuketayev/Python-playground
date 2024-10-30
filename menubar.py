from tkinter import *

def openfile():
    print("File has been opened!")


def savefile():
    print("File has been saved!")

def Undo():
    print("You undo")


def Redo():
    print("You redo!")



window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openfile)
fileMenu.add_command(label='Save',command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)


editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu = editMenu)
editMenu.add_command(label="Undo",command=Undo)
editMenu.add_command(label="Redo",command=Redo)


window.mainloop()