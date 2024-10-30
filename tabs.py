from tkinter import *
from tkinter import ttk


window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab1")
notebook.add(tab2, text="Tab2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is tab1", width=50,height=25).pack()
Label(tab2, text="Hello, this is tab2", width=50,height=25).pack()

window.mainloop()