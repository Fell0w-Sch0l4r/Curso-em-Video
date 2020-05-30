def moeda(x,moeda="€"):
    return f"{moeda}{x:.2f}".replace(".", ",")


def metade(x,show=False,moed="€"):
    if show:
        return moeda(x*2,moed)
    else:
        return x/2


def dobro(x,show=False,moed="€"):
    if show:
        return moeda(2*x,moed)
    else:
        return 2 * x


def aumentar(x, y,show=False,moed="€"):
    if show:
        return moeda(x + x*(y/100),moed)
    else:
        return x + x*(y/100)


def diminuir(x, y,show=False,moed="€"):
    if show:
        return moeda(x-x*(y/100),moed)
    else:
        return x - x * (y / 100)


def resumo(x,au,rd):
    '''
    Criei, escrevi, fazi.
    :param x: Valor monetário
    :param au: Aumento em percentagem
    :param rd: Redução em Percentagem
    :return: Não retorna nenhum valor
    '''
    print("-"*35)
    print(f"{'RESUMO DO VALOR':^35}")
    print("-"*35)
    print(f"{'Preço analisado:':<20}{moeda(x)}")
    print(f"{'Dobro do preço:':<20}{moeda(x*2)}")
    print(f"{'Metade do preço:':<20}{moeda(x/2)}")
    print(f"{au}{'% de aumento:':<17} {aumentar(x,au,True)}")
    print(f"{rd}{'% de redução:':<17} {diminuir(x,rd,True)}")


def leiaDinheiro(texto):
    while True:
        a = input(texto)
        if a.isnumeric():
            break
        print(f"\033[31mERRO: {a} é um preço inválido!\033[m")

    return a


