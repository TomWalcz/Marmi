from tkinter import *


def scalex(x, c):
    if c is True:
        if x <= 1000:
            x = x+1
        elif x > 1000 and x <= 1410:
            x = x+2
        elif x > 1410 and x <= 1800:
            x = x+3
    elif c is False:
        if x <= 610:
            x = x+1
        elif x > 610 and x <= 1000:
            x = x+2
        elif x > 1000 and x <= 1411:
            x = x+3
        elif x > 1411 and x <= 1800:
            x = x+4
    return (x)


def scaley(y):
    y = (y*1.007) + 1
    return (y)


def scalez(z):
    z = z*1.007
    return (z)


def scaler(num, numscale):
    scale = numscale/num
    return(scale)

def printdata(xprint, yprint, zprint):
    x = (xprint.get())
    y = (yprint.get())
    z = (zprint.get())
    print(x)
    print(y)
    print(z)
   


if __name__ == '__main__':

    root = Tk()
    root.geometry("400x200")

    titleframe = Frame(root)
    titleframe.pack(side = TOP)

    frame = Frame(root)
    frame.pack()

    CheckVar1 = BooleanVar()
    x = DoubleVar()
    y = DoubleVar()
    z = DoubleVar()
    labeltitle = Label(titleframe, text = "Konfigurator Umywalek", relief=FLAT, anchor=CENTER, font = "Helvetica 16 bold italic").grid(row=0)
    labelx = Label(frame, text = "Podaj X" ).grid(row=1)
    labely = Label(frame, text = "Podaj Y" ).grid(row=2)
    labelz = Label(frame, text = "Podaj Z" ).grid(row=3)
    labelc = Label(frame, text = "Cieńkoblaciastość").grid(row=4)
    entryx = Entry(frame, textvariable=x, width = 20)
    entryx.grid(row=1, column=1)
    entryy = Entry(frame, textvariable=y, width = 20)
    entryy.grid(row=2, column=1)
    entryz = Entry(frame, textvariable=z, width = 20)
    entryz.grid(row=3, column=1)
    c = Checkbutton(frame, variable=CheckVar1)
    c.grid(row=4, column=1)
    submit = Button(frame, text = "Submit", width = 20, command = lambda: printdata(x,y,z)).grid(row=5)

    root.mainloop()