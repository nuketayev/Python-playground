from tkinter import *

def submit():
    tempeture = scale.get()
    print("Current temperature is:",tempeture,"degrees C")


window = Tk()

scale = Scale(window, 
              from_=100,
              to=75,
              length=600,
              fg='Red',
              bg='Black',
              troughcolor="Blue",
              font=("Arial",30),
              tickinterval=5,
              showvalue=1,)
scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

button = Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()