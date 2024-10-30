from tkinter import *
import time

WIDTH = 2000
HEIGHT = 1000

xVelocity=7
yVelocity=9

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
photo = PhotoImage(file="r.png")
my_image = canvas.create_image(0,0,image=photo, anchor=NW)

image_width = photo.width()
image_height = photo.width()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
        xVelocity *= -1
    if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
        yVelocity *= -1
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
