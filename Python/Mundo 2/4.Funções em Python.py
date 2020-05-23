# Exercício 96
'''def área(a,b):
    print(f"A área do terreno {comprimento}x{largura} é de {a*b}m².")


print("  Controlo de Terrenos")
print("-"*25)
largura=float(input("LARGURA (m):"))
comprimento=float(input("COMPRIMENTO (m):"))
área(comprimento,largura)'''

# Exercício 97
'''def escreva(x):
    tam=len(x)+4
    print("~"*tam)
    print(f"  {x}")
    print("~"*tam)


escreva("Ângel Cagiza")
escreva("no")
escreva("Ângel Rodolfo Gomes Cagiza")'''

# Exercício 98
'''def contador(i,f,p):
    from time import sleep
    print("=-"*25)
    sleep(1)
    if p==0:
        p=1
    if i<f:
        print(f"Contagem de {i} até {f} de {p} em {p}.")
        for c in range(i,f+1,p):
            print(c,end=" ",flush=True)
            sleep(.5)
        print("FIM!")
    else:
        if p<0:p=-p
        print(f"Contagem de {i} até {f} de {p} em {p}.")
        for c in range(i,f-1,-p):
            print(c,end=" ",flush=True)
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
'''def maior(*x):
    from time import sleep
    print("=-"*35)
    print("Analisando os valores processados...")
    for c in x:
        print(c,end=" ",flush=True)
        sleep(1)
    print(f"Foram informados {len(x)} valores ao todo.")
    if len(x)>0:
        print(f"O maior valor informado foi {max(x)}.")


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()'''

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