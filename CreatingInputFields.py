from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name")

def myClick():
    hello = "Hello "+e.get()
    #myLabel = Label(root, text="Hello "+e.get())
    myLabel = Label(root, text=hello)
    myButton = Button(root, text="Click", padx=40, pady=40)
    myButton.pack()
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()