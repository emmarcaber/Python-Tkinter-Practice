from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='sample_image.png')

label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='#00FFFF', bg='black',
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
# initializes the label with different attributes
# text = text to display in label
# font = font of the label
# fg = color of the label
# relief = border style
# bd = border size
# padx = padding x
# pady = padding y
# image = image of the label
# compound = arrangement of the image and label

label.pack()
#label.place(x = 0, y = 0)

window.mainloop()