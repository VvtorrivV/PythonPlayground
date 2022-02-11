#Biblioteka ze wszelkikmi przdatnymi rzeczami do GUI
#przyciski, slidery i inne

from tkinter import *

#bazowe okno gui
root = Tk()

#creating labale to show sth
myLabel = Label(root, text="Hello Python")

#first option to display sth is packing - shows on the screen
myLabel.pack()

#event loop - it says whats going on
root.mainloop()
