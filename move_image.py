from tkinter import *

# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-130)

# def move_left(event):
#     label.place(x=label.winfo_x()-130, y=label.winfo_y())

# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+130)

# def move_right(event):
#     label.place(x=label.winfo_x()+130, y=label.winfo_y())


# window = Tk()
# window.geometry("500x500")

# window.bind("<w>",move_up)
# window.bind("<a>",move_left)
# window.bind("<s>",move_down)
# window.bind("<d>",move_right)

# myImage = PhotoImage(file="t.png")
# label = Label(window,image=myImage,bg="Black")
# label.place(x=0,y=0)


# window.mainloop()


def move_up(event):
    canvas.place(x=canvas.winfo_x(), y=canvas.winfo_y()-130)

def move_left(event):
    canvas.place(x=canvas.winfo_x()-130, y=canvas.winfo_y())

def move_down(event):
    canvas.place(x=canvas.winfo_x(), y=canvas.winfo_y()+130)

def move_right(event):
    canvas.place(x=canvas.winfo_x()+130, y=canvas.winfo_y())


window = Tk()
canvas = Canvas(window, width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file="t.png")
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)


# label = Label(window,image=myImage,bg="Black")
# label.place(x=0,y=0)


window.mainloop()