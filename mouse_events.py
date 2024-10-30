from tkinter import *

def doSomething(event):
    print("You clicked at: "+str(event.x)+","+str(event.y))

window = Tk()

# window.bind("<Button-1>",doSomething)
window.bind("<Motion>",doSomething)

window.mainloop()