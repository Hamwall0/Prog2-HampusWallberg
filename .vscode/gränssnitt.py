from tkinter import *
import random

hval = 0
dval = 0
root = Tk()
val = ["sten", "sax", "påse"]
sten = Button(root, text="Sten")
papper = Button(root, text="Papper")
sax = Button(root, text="Sax")
sten.place(x=0, y=25)
sax.place(x=100, y=25)
papper.place(x=200, y=25)


def sten_handler(self):
    global hval
    hval = "sten"
    run()


def sax_handler(self):
    global hval
    hval = "sax"
    run()


def papper_handler(self):
    global hval
    hval = "papper"
    run()


sten.bind("<Button-1>", sten_handler)
sax.bind("<Button-1>", sax_handler)
papper.bind("<Button-1>", papper_handler)


def run():
    dval = random.choice(val)
    print(hval, dval)
    if hval == dval:
        print("lika")
    elif hval == "sten" and dval == "sax":
        print("du vann")
    elif hval == "papper" and dval == "sten":
        print("du vann")
    elif hval == "sax" and dval == "papper":
        print("du vann")
    else:
        print("du förlorade")


root.mainloop()
