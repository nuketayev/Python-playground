from tkinter import *

food = ["pizza","hamburger","hotdog"]


def order():
    if (x.get()==0):
        print("You chose pizza")
    elif (x.get()==1):
        print("You chose hamburger")
    else:
        print("You chose hotdog")

window = Tk()

x =IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index],
                              variable=x, 
                              value=index,
                              padx=25,
                              font=('Arial',50),
                              indicatoron=0,
                              width = 15,
                              command=order)
    radiobutton.config()
    radiobutton.pack(anchor=W)

window.mainloop()