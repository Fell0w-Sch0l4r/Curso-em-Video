def moeda(x):
    b=""
    for c in str(x):
        if c==".":
            b+=","
        else:
            b+=c
    return f"€{b}"


def metade(x,show=False):
    if show:
        return moeda(x*2)
    else:
        return x/2


def dobro(x,show=False):
    if show:
        return moeda(2*x)
    else:
        return 2 * x


def aumentar(x, y,show=False):
    if show:
        return moeda(x + x*(y/100))
    else:
        return x + x*(y/100)


def diminuir(x, y,show=False):
    if show:
        return moeda(x-x*(y/100))
    else:
        return x - x * (y / 100)


def resumo(x,au,rd):
    print("-"*35)
    print("         RESUMO DO VALOR")
    print("-"*35)
    print(f"{'Preço analisado:':<20}{moeda(x)}")
    print(f"{'Dobro do preço:':<20}{moeda(x*2)}")
    print(f"{'Metade do preço:':<20}{moeda(x/2)}")
    print(f"{au}{'% de aumento:':<17} {aumentar(x,au,True)}")
    print(f"{rd}{'% de redução:':<17} {diminuir(x,rd,True)}")
    print("-"*35)


