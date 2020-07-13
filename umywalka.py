import tkinter as tk

fields = ('Wymair X', 'Wymiar Y', 'Wymiar Z', 'Cien')

def scalex(entries):
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


def scaley(entries):
    y = (y*1.007) + 1
    return (y)


def scalez(entries):
    z = z*1.007
    return (z)


def scaler(num, numscale):
    scale = numscale/num
    return(scale)

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field, anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries


if __name__ == '__main__':

    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Oblicz',
       command=(lambda e=ents: scalex(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Wyczysc')
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    # xraw = input('Podaj wymiar x: ')
    # x = (float(entries['Wymiar X'].get()))
    # yraw = input('Podaj wymiar y: ')
    # y = (float(entries['Wymiar Y'].get()))
    # zraw = input('Podaj wymiar z: ')
    # z = (float(entries['Wymiar Z'].get()))
    while True:
        c = input('Podaj cieńkoblaciastość T/N: ')
        if c == 't' or c == 'T':
            c = True
            break
        elif c == 'n' or c == 'N':
            c = False
            break

    # xs = scalex(x, c)
    # print(format(xs, '.2f'))
    # xscaler = scaler(x, xs)
    # print(xscaler)
    # ys = scaley(y)
    # print(format(ys, '.2f'))
    # yscaler = scaler(y, ys)
    # print(yscaler)
    # zs = scalez(z)
    # print(format(zs, '.2f'))
    # zscaler = scaler(z, zs)
    # print(zscaler)

    master.mainloop()
