from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420") # set the size of the window
window.title("Emmar First Code GUI Program") # set the title of the window

icon = PhotoImage(file='logo.png') # initialize the icon to be used
window.iconphoto(True, icon) # set the icon of the window
window.config(background='#00FFFF') # set the background color

window.mainloop() # place window on computer screen, listen for events