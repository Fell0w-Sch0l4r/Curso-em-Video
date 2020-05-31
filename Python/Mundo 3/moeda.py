def moeda(x, moeda="€"):
    return f"{moeda}{x:.2f}".replace(".", ",")


def metade(x, show=False, moed="€"):
    if show:
        return moeda(x*2, moed)
    else:
        return x/2


def dobro(x, show=False, moed="€"):
    if show:
        return moeda(2*x, moed)
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


def resumo(x ,au=10, rd=5):
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
    print(f"Preço analisado: \t{moeda(x)}")
    print(f"Dobro do preço: \t{moeda(x*2)}")
    print(f"Metade do preço: \t{moeda(x/2)}")
    print(f"{au}% de aumento: \t{aumentar(x,au,True)}")
    print(f"{rd}% de redução: \t\t{diminuir(x,rd,True)}")


