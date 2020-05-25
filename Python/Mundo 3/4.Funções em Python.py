# Exercício 96
'''def área(a,b):
    print(f"A área do terreno {comprimento}x{largura} é de {a*b}m².")


print("  Controlo de Terrenos")
print("-"*25)
largura=float(input("LARGURA (m):"))
comprimento=float(input("COMPRIMENTO (m):"))
área(comprimento,largura)'''

# Exercício 97
def escreva(x):
    tam=len(x)+4
    print("~"*tam)
    print(f"  {x}")
    print("~"*tam)


# Exercício 98
'''def contador(i, f, p):
    from time import sleep
    print("=-"*25)
    sleep(1)
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}.")
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=" ", flush=True)
            sleep(.5)
    else:
        for c in range(i, f-1, -p):
            print(c, end=" ", flush=True)
            sleep(.5)
    print("FIM!")


contador(1,10,1)
contador(10,0,2)
print("=-"*25)
print("Agora é a sua vez de personalisar a contagem.")
inicio=int(input("Início:"))
fim=int(input("Fim:"))
passo=int(input("Passo:"))
contador(inicio,fim,passo)'''
# Exercício 99
def maior(*x):
    from time import sleep
    print("=-"*35)
    print("Analisando os valores processados...")
    for c in x:
        print(c,end=" ",flush=True)
        sleep(1)
    print(f"Foram informados {len(x)} valores ao todo.")
    if len(x)>0:
        print(f"O maior valor informado foi {max(x)}.")



# Exercício 100
'''def sorteia(x):
    from random import randint
    from time import sleep
    print("Sorteando 5 valores da lista:",end=" ")
    for c in range(0,5):
        x.append(randint(1,10))
        print(x[c],end=" ")
        sleep(.5)
    print("PRONTO!")


def soma_par(x):
    soma=0
    for c in x:
        if c%2==0:
            soma+=c
    print(f"Somando os valores pares de {x}, temos {soma}.")


valores=[]
sorteia(valores)
soma_par(valores)'''



# Exercício 101

'''def voto(ano_nas):
    from datetime import date
    idade = date.today().year-ano_nas
    if 65> idade >= 18:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    elif idade < 18:
        return f"Com {idade} anos: NÃO VOTA"
    else:
        return f"Com {idade} anos: VOTO OPCIONAL"


print("-"*35)
print(voto(int(input("Em que ano nasceste?:"))))'''

# Exercício 102
def factorial(n, show = False):
    '''
    -> Calcula o factorial de um número.
    :param n: O número a ser calculado.
    :param show: (OPCIONAL) Mosrar ou não a conta.
    :return: O valor do factorial de um número n.
    '''
    print("-"*30)
    resp = 1
    conta = ""
    for c in range(n, 0, -1):
        resp *= c
        conta += f"{c} x " if c > 1 else f"{c} = {resp}"
    if show:
        return conta
    else:
        return resp


# Exercício 103
'''def ficha(nome="<desconhecido>",golos=0):
    if nome=="":
        nome="<desconhecido>"
    if golos=="":
        golos=0
    print(f"O jogador {nome} fez {golos} golo(s) no campeonato.")


nome=input("Nome do jogador:")
golo=input("Número de Golos:")
if golo != "":
    golo=int(golo)
ficha(nome,golo)'''

# Exercício 104
def leiaint(texto):
    a=input(texto)
    while not a.isnumeric():
        print("\033[31mERRO! Digite um número inteiro válido.\033[m")
        a=input(texto)
    return a


'''n = leiaint("Digite um número:")
print(f"Digitou o número {n}.")'''

# Exercício 105
def notas(*n,sit=False):
    '''
    →Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas e situações de vários alunos.
    :param sit: (OPCIONAL), indica se deve ou não adicionar a situação.
    :return: Dicionárrio com várias informções sobre a situação da turma.
    '''
    dic={"total":len(n),"maior":max(n),"menor":min(n),"média":0}
    for c in n:
        dic["média"]+=c
    dic["média"]/=len(n)
    if sit:
        if dic["média"]>15:
            dic["situação"]="BOA"
        elif 10<=dic["média"]<15:
            dic["situação"]="SUFICIENTE"
        else:
            dic["situação"]="MÁ"
    return dic


'''resp=notas(20,19,16.5,20,17,14)
print(resp)'''

# Exercício 106
from time import sleep
while True:
    print("\033[33m~"*27)
    print("  SISTEMA DE AJUDA PyHELP")
    print("\033[33m~\033[m"*27)
    a=input("Função ou Biblioteca > ").strip().lower()
    if a == "fim":
        break
    sleep(0.5)
    print("\033[34m~"*(34+len(a)))
    print(f"  Acessamdo o manual do comando {a}")
    print("\033[34m~\033[m"*(34+len(a)))
    sleep(0.5)
    print("\033[32m")
    help(a)
    print("\033[m")
sleep(0.5)
print("\033[31m~"*12)
print("  ATÉ LOGO")
print("\033[31m~\033[m"*12)
