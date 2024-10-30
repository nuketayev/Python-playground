from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event2):
    widget = event2.widget
    x = widget.winfo_x() - widget.startX + event2.x
    y = widget.winfo_y() - widget.startY + event2.y
    widget.place(x=x,y=y)



window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()