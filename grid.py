from tkinter import *

#grid system - imagine columns and rows, my program is a grid
root = Tk()

#you can spit tasks: create -> put on the screen
myLabel1 = Label(root, text="Hello Python")
myLabel2 = Label(root, text="I'm Wiki")
#in brackets im telling how i want position my label
myLabel1.grid(row=0, column=3)
myLabel2.grid(row=1, column=0)

#or becasue is object oriented, make it in one line
myLabel3=Label(root, text="         ").grid(row=1, column=1)

root.mainloop()
