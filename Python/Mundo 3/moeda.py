def metade(x,show=False):
    if show:
        c=x/2
        b=""
        for v in str(c):
            if v==".":
                b+=","
            else:
                b+=v
        return f"€{b}"
    else:
        return x/2


def dobro(x):
    return 2 * x


def aumentar(x, y):
    return x + x*(y/100)


def diminuir(x, y):

    return x - x * (y / 100)


def moeda(x):
    b=""
    for c in str(x):
        if c==".":
            b+=","
        else:
            b+=c
    return f"€{b}"

def leiaDinheiro(texto):
    a = input(texto)
    if "," in a:
        b=""
        for c in a:
            if c == ",":
                b += "."
            else:
                b+=c

    while not a.isdecimal():
        print(f"\033[31mERRO: {a} é um preço inválido!\033[m")
        a = input(texto)
    return a


'''p=float(input("Digita o preço mnb:"))
print(f"Digitou {moeda(p)}")'''