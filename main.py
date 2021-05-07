
from tkinter import *


root = Tk()
root.geometry("800x500")
root.title("Temperature Convertor")


def activate_2():
    entry3.place(x=60, y=70)


def activate_1():
    entry2.place(x=60, y=70)


#  defining a function that will clear all the text in an entry
def clear():
    entry.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


#  defining a function that will destroy the program
def exit():
    return root.destroy()


#  defining a function that converts Celsius to Fahrenheit and visa vesa
def convertor():
    if len(entry2.get()) > 0:
        answer = float(entry2.get()) * 9/5 + 32
        #  inserting the value from the 1nd entry(from LabelFrame) to the last entry on the root
        entry.insert(0, round(answer, 2))
    else:
        answer = (float(entry3.get())-32) * 5/9
        #  inserting the value from the 2nd entry(from LabelFrame) to the last entry on the root
        entry.insert(0, round(answer, 2))


# Creating and displaying a label on top middle of the root
label1 = Label(root, text="Temperature Convert Web Service", font="times 16")
label1.pack()

# Creating and positioning the LabelFrames on the root
lbframe = LabelFrame(root, text="Celsius to Fahrenheit", width=300, height=150)
lbframe.place(x=100, y=40)
lbframe1 = LabelFrame(root, text=" Fahrenheit to Celsius", width=300, height=150)
lbframe1.place(x=450, y=40)

# Creating and positioning the entry at the bottom of the root
entry = Entry(root, bg="green", font="100")
entry.place(x=330, y=300,  width=200, height=100)

# Creating an entry on the 1st labelFrame
entry2 = Entry(lbframe, width=20)


# Creating an entry on the 1st labelFrame
entry3 = Entry(lbframe1, width=20)


# Creating and positioning the Clear button
button1 = Button(root, text="Clear", command=clear)
button1.place(x=200, y=350)

# Creating and positioning the Exit Program button
button2 = Button(root, text="Exit Program", command=exit)
button2.place(x=350, y=450)

# Creating and positioning the Activate F to C button
button3 = Button(root, text="Activate:Fahrenheit to Celsius", command=activate_1)
button3.place(x=130, y=220)

# Creating and positioning the Activate C to F button
button4 = Button(root, text="Activate:Celsius to Fahrenheit", command=activate_2)
button4.place(x=480, y=220)


# Creating and positioning the Calculate Conversion button
button5 = Button(root, text="Calculate Conversion", command=convertor)
button5.place(x=150, y=300)

root.mainloop()




