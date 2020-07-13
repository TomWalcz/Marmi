import tkinter as tk

fields = ('Wymair X', 'Wymiar Y', 'Wymiar Z', 'Cien')

def scaley(entries):
    y =  float(entries['Wymiar Y'].get())
    y = (y*1.007) + 1
    print(y)

def scalez(entries):
    y =  float(entries['Wymiar Z'].get())
    z = z*1.007
    return (z)

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
        command=(lambda e=ents: scaley(e))),
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Wyczysc')
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()