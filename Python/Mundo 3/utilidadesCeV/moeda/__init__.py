def moeda(x):
    return f"€{x:.2f}".replace(".", ",")


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
    '''
    Criei, escrevi, fszi.
    :param x: Valor monetário
    :param au: Aumento em percentagem
    :param rd: Redução em Percentagem
    :return:
    '''
    print("-"*35)
    print("         RESUMO DO VALOR")
    print("-"*35)
    print(f"{'Preço analisado:':<20}{moeda(x)}")
    print(f"{'Dobro do preço:':<20}{moeda(x*2)}")
    print(f"{'Metade do preço:':<20}{moeda(x/2)}")
    print(f"{au}{'% de aumento:':<17} {aumentar(x,au,True)}")
    print(f"{rd}{'% de redução:':<17} {diminuir(x,rd,True)}")

def leiaDinheiro(texto):
    a = input(texto)

    while not a.isdecimal():
        print(f"\033[31mERRO: {a} é um preço inválido!\033[m")
        a = input(texto)
    return a