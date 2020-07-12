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

# Main =======================================


xraw = input('Podaj wymiar x: ')
x = float(xraw)
yraw = input('Podaj wymiar y: ')
y = float(yraw)
zraw = input('Podaj wymiar z: ')
z = float(zraw)
while True:
    c = input('Podaj cieńkoblaciastość T/N: ')
    if c == 't' or c == 'T':
        c = True
        break
    elif c == 'n' or c == 'N':
        c = False
        break

print(type(x))
xs = scalex(x, c)
print(format(xs, '.2f'))
print(type(xs))
# xscaler = scaler(x, xs)
ys = scaley(y)
print(ys)
# yscaler = scaler(y, ys)
zs = scaley(z)
print(zs)
# zscaler = scaler(z, zs)
