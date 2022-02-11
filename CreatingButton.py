from tkinter import *

root = Tk()
#state - we can disable button
#text - what can be the text of button
#root - where will be this button

def myClick():
    myLabel=Label(root, text="Look! I clicked the button")
    myLabel.pack()

myButton=Button(root, text="Click me", command=myClick(), fg="blue", bg="red")
myButton.pack()

root.mainloop()