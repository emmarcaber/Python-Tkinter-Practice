from tkinter import *

# entry widgets = textbox that accepts a single line of user input

window = Tk()

def submit():
    username = entry.get()
    print("Hello, " + username)
    entry.config(state = DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) -1, END)

entry = Entry(
    window,
    font = ("Arial", 50),
    fg = "#00FF00",
    bg = "black",
    show = "*"
)
entry.insert(0, "Spongebob")
entry.pack(side=LEFT)

submit_button = Button(
    window, text = "Submit", command = submit
)
submit_button.pack(side=RIGHT)

delete_button = Button(
    window, text = "Delete", command = delete
)
delete_button.pack(side=RIGHT)

backspace_button = Button(
    window, text = "Backspace", command = backspace
)
backspace_button.pack(side=RIGHT)

window.mainloop()