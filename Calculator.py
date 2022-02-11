from tkinter import *

root = Tk()
root.title("Vtorriv Calculator")

entryTextBox = Entry(root, width=30, borderwidth=5)
entryTextBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonMinus():
    firstNumber = entryTextBox.get()
    global fNum
    global math
    math = "subtraction"
    fNum = int(firstNumber)
    entryTextBox.delete(0, END)

def buttonMultiply():
    firstNumber = entryTextBox.get()
    global fNum
    global math
    math = "multication"
    fNum = int(firstNumber)
    entryTextBox.delete(0, END)

def buttonDivide():
    firstNumber = entryTextBox.get()
    global fNum
    global math
    math = "division"
    fNum = int(firstNumber)
    entryTextBox.delete(0, END)

def buttonClick(number):
    #delete what is in the box
    #entryTextBox.delete(0,END)
    global current
    current=entryTextBox.get()
    entryTextBox.delete(0, END)
    #insert what we want
    entryTextBox.insert(0, str(current)+str(number))

def buttonClear():
    entryTextBox.delete(0, END)
    fNum=0

def buttonAdd():
    firstNumber = entryTextBox.get()
    global fNum
    global math
    math = "addition"
    fNum = int(firstNumber)
    entryTextBox.delete(0, END)

def buttonEqual():
    secondNumber = entryTextBox.get()
    entryTextBox.delete(0, END)
    if math == "addition":
        entryTextBox.insert(0, fNum + int(secondNumber))
    if math == "subtraction":
        entryTextBox.insert(0, fNum - int(secondNumber))
    if math == "multication":
        entryTextBox.insert(0, fNum * int(secondNumber))
    if math == "division":
        entryTextBox.insert(0, fNum / int(secondNumber))


#define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

buttonPlus = Button(root, text="+", padx=40, pady=20, command=buttonAdd)
buttonMinus = Button(root, text="-", padx=40, pady=20, command=buttonMinus)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=buttonDivide)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=buttonMultiply)
buttonEqual = Button(root, text="=", padx=40, pady=20, command=buttonEqual)
buttonClear = Button(root, text="Clear", padx=100, pady=20, command=buttonClear)

#put buttons on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

buttonPlus.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonMinus.grid(row=4, column=2)

buttonMultiply.grid(row=5,column=0)
buttonEqual.grid(row=5, column=1)
buttonDivide.grid(row=5, column=2)

buttonClear.grid(row=6,column=0, columnspan=3)




root.mainloop()