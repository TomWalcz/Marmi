import tkinter as tk
import subprocess



x = 0.0
y = 0.0
z = 0.0

def scalex(xraw, c):
    global x
    xraw = (xraw.get())
    if c is True:
        print(True)
        if xraw <= 1000:
            xraw = xraw+1
        elif xraw > 1000 and xraw <= 1410:
            xraw = xraw+2
        elif xraw > 1410 and xraw <= 1800:
            xraw = xraw+3
    elif c is False:
        print(False)
        if xraw <= 610:
            xraw = xraw+1
        elif xraw > 610 and xraw <= 1000:
            xraw = xraw+2
        elif xraw > 1000 and xraw <= 1411:
            xraw = xraw+3
        elif xraw > 1411 and xraw <= 1800:
            xraw = xraw+4
    x = xraw
    return(x)


def scaley(yraw):
    global y
    yraw = (yraw.get())
    y = (yraw*1.007) + 1
    return (y)


def scalez(zraw):
    global z
    zraw = (zraw.get())
    z = zraw*1.007
    return (z)


def scaler(raw, *c, yraw, zraw):
    # print(xraw.get(), yraw.get(), zraw.get())
    print(scalex(xraw, c))
    print(scaley(yraw))
    print(scalez(zraw))
    xscaler = scalex(xraw, c)/xraw.get()
    print(xscaler)
    return()


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("400x200")

    titleframe = tk.Frame(root)
    titleframe.pack(side=tk.TOP)

    frame = tk.Frame(root)
    frame.pack()

    CheckVar1 = tk.BooleanVar()
    xraw = tk.DoubleVar()
    yraw = tk.DoubleVar()
    zraw = tk.DoubleVar()
    labeltitle = tk.Label(titleframe, text="Konfigurator Umywalek", relief=tk.FLAT, anchor=tk.CENTER, font="Helvetica 16 bold italic").grid(row=0)
    labelx = tk.Label(frame, text="Podaj X").grid(row=1)
    labely = tk.Label(frame, text="Podaj Y").grid(row=2)
    labelz = tk.Label(frame, text="Podaj Z").grid(row=3)
    labelc = tk.Label(frame, text="Cieńkoblaciastość").grid(row=4)
    entryx = tk.Entry(frame, textvariable=xraw, width=20)
    entryx.grid(row=1, column=1)
    entryy = tk.Entry(frame, textvariable=yraw, width=20)
    entryy.grid(row=2, column=1)
    entryz = tk.Entry(frame, textvariable=zraw, width=20)
    entryz.grid(row=3, column=1)
    c = tk.Checkbutton(frame, variable=CheckVar1)
    c.grid(row=4, column=1)
    # submit = tk.Button(frame, text="Submit", width=20, command=lambda: [scalex(xraw,CheckVar1.get()), scaley(yraw), scalez(zraw)]).grid(row=5)
    submit = tk.Button(frame, text="Submit", width=20, command=lambda: [scaler(xraw, CheckVar1.get(), yraw, zraw)]).grid(row=5, columnspan =2)


    text_box = tk.Label(frame, text = "txt")
    text_box.grid(row = 8, column = 0)
    root.mainloop()