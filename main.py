from Tkinter import *
from PIL import Image, ImageTk

ms = 1

i = 0
def change():
    global i
    if i % 2 == 0:
        to = green
    else:
        to = red
    label.configure(image = to)
    label.bm = to
    top.after(ms, change)
    i += 1

top = Tk()
top.title("blink")
image = Image.open("red.png")
red = ImageTk.PhotoImage(image)

image = Image.open("green.png")
green = ImageTk.PhotoImage(image)

label = Label(top, image = red)
label.bm = red
label.pack()
change()
top.mainloop()
