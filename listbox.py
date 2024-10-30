from tkinter import *

window = Tk()

def Submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ", end="")
    for index in food:
        print(index, end=" ")
    print("")
    # print(listbox.get(listbox.curselection()))
    

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())



listbox = Listbox(window, 
                  bg = "Black",
                  font=("Constantia",35),
                  width=12,
                  fg="White",
                  selectmode=MULTIPLE)
listbox.pack()


listbox.insert(1, "Pizza")
listbox.insert(2, "Sushi")
listbox.insert(3, "Pie")
listbox.insert(4, "Hamburger")
listbox.insert(5, "Hotdog")
listbox.insert(6, "Fries")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="Submit", command=Submit)
submitButton.pack()

deleteButton = Button(window,text="Delete", command=delete)
deleteButton.pack()

addButton = Button(window,text="Add", command=add)
addButton.pack()


window.mainloop()