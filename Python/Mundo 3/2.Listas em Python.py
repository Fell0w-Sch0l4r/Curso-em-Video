# Exercício 78
'''num=[]
for c in range (0,5):
    num.append(int(input(f"Digite o valor para a Posição {c}:")))
print(f"Digitou os valores {num}.")
print(f"O maior valor digitado foi {max(num)}, nas posições:",end=" ")
for c,m in enumerate(num):
    if max(num)==m:
        print(f"{c:.<4}",end=" ")
print(f"\nO menor valor digitado foi {min(num)}, nas posições:",end=" ")
for c,m in enumerate(num):
    if min(num)==m:
        print(f"{c:.<4}",end=" ")'''
# Exercício 79
'''val=[]
while True:
    a=int(input("Digite um número:"))
    if a in val:
        print("Valor duplicado! Não vou adicionar...")
    else:
        val.append(a)
        print("Valor adicionado com sucesso.....")
    es=input("Quer continuar?:").lower().strip()
    while es not in "sn":
        es=input("Quer continuar?:")
    if es=="n":
        break
print("=-"*20)
print(f"Digitou os valores {sorted(val)}")'''

# Exercício 80
'''val=[]
for c in range(0,5):
    a=int(input("Digita um número:"))
    if len(val)==0 or a>val[-1]:#També pode ser if c==0
        val.append(a)
        print(f"Valor {a} adicionado na última posição.")
    else:
        for b,d in enumerate(val):
            if a<d:
                val.insert(b,a)
                print(f"Valor {a} adicionado na posição {b}.")
                break
print(val)'''
# Exercício 81
'''lista=[]
while True:
    lista.append(int(input("Digita um número:")))
    es=input("Quer continuar?:").lower().strip()
    while es not in "sn":
        es = input("Quer continuar?:").lower().strip()
    if es=="n":
        break
print(f"Foram digitados {len(lista)} números.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")
print("O valor 5 faz parte da lista." if 5 in lista
      else "O valor 5 não faz arte da lista.")'''
'''if 5 in lista:
    print("O valor 5 faz parte da lista e enconstra-se em posição:",end=" ")
    for c,m in enumerate(lista):
        if m==5:
            print(c,end=" ")
else:
    print("O valor 5 não faz arte da lista.")'''
# Exercício 82
'''lista=[]
par=[]
impar=[]
while True:
    lista.append(int(input("Digita um número:")))
    es=input("Quer continuar?:").lower().strip()
    while es not in "sn":
        es=input("Quer continuar?:").lower().strip()
    if es=="n":
        break
for c in lista:
    if c%2==0:
        par.append(c)
    else:
        impar.append(c)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")'''

# Exercício 83
'''i=input("Digite a expressão:")
lista=[]
if i.count("(")==i.count(")"):
    print("Espressão Válida.")
else:
    print("Expressão inválida.")'''

'''for c in i:
    lista.append(c)
if lista.count("(")==lista.count(")"):
    print("Expressão válida.")
else:
    print("Expressão inválida.")'''

# Exercício 84

pessoas=[]
tmp=[]
maior=menor=0
while True:
    tmp.append(input("Digite o nome da pessoa:").title())
    tmp.append(float(input("Digite o peso:")))
    if len(pessoas)==0:
        maior=menor=tmp[1]
    elif tmp[1]>maior:
        maior=tmp[1]
    elif tmp[1]<menor:
        menor=tmp[1]
    pessoas.append(tmp[:])
    tmp.clear()
    es=input("Quer continuar?:").lower().strip()
    if es=="n":
        break
print(pessoas)
print(f"Ao todo foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso foi {maior}Kg, que foi o peso de:",end=" ")
for c in pessoas:
    if c[1]==maior:
        print(c[0],end=" ")
print(f"\nO menor peso foi {menor}Kg, que foi o peso de:",end=" ")
for c in pessoas:
    if c[1]==menor:
        print(c[0],end=" ")
# Exercício 85
'''numeros=[[],[]]
for c in range(0,7):
    a=int(input(f"Digite o {c+1}º número:"))
    if a%2==0:
        numeros[0].append(a)
    else:
        numeros[1].append(a)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores pares digitados foram {numeros[0]}.")
print(f"Os valores ímpares digitados foram {numeros[1]}.")'''


# Exercício 86
'''matrix=[[],[],[]]
for t in range(0,3):
    for r in range(0,3):
        matrix[t].append(int(input(f"Digita um valor para [{t}, {r}]:")))
print(matrix)
print("=-"*20)
for e in matrix:
    for d,r in enumerate(e):
        if d == 2:
            print(f"[  {r}  ]")
        else:
            print(f"[  {r}  ]", end=" ")'''
# exercício 87
'''matrix = [[], [], []]
par=0
sc3=0
for t in range(0,3):
    for r in range(0,3):
        matrix[t].append(int(input(f"Digita um valor para [{t}, {r}]:")))
        if matrix[t][r]%2==0:
            par+=matrix[t][r]
    sc3 += matrix [t] [2]
print("=-"*20)
for e in matrix:
    for d,r in enumerate(e):
        if d == 2:
            print(f"[  {r}  ]")
        else:
            print(f"[  {r}  ]", end=" ")
print("=-"*20)
print(f"A soma dos valores pares é {par}.")
print(f"A soma dos valores da terceira coluna é {sc3}.")
print(f"O maior valor da segunda linha é {max(matrix[1])}.")'''
# Exercício 88
'''from time import sleep
from random import randint
from time import sleep
jogos=[]
print("-"*30)
print(f"{'EURO MILHÕES':^30}")
print("-"*30)
es=int(input("Quantos jogos quer que eu sorteie?:"))
print(f"{'SORTEANDO JOGOS':-^30}")
for c in range(0,es):
    jogos.append([])
    for d in range(0,6):
        a=randint(1,60)
        while a in jogos[c]:
            a=randint(1,60)
        jogos[c].append(a)
    print(f"Jogo {c+1}: {jogos[c]}")
    sleep(1)
print(f"{'BOA SORTE!':=^30}")'''
# Exercício 89
'''alunos=[]
n=0
while True:
    alunos.append([input("Nome:").title()])
    alunos[n].append([float(input("Nota 1:")),float(input("Nota 2:"))])
    es=input("Quer continuar?:").lower().strip()
    n+=1
    if es=="n":
        break
print(alunos)'''
'''print("No. NOME             MÉDIA")
print("-"*30)
for c in range(0, len(alunos)):
    print(c, end="   ")
    print(f"{alunos[c][0]:17}", end="")
    media=(alunos[c][1][0]+alunos[c][1][1])/2
    print(f"{media:.1f}")
while True:
    print("-"*40)
    a=int(input("Monstar as notas de que aluno?(999 para parar):"))
    if a ==999:
        break
    print(f"As notas de {alunos[a][0]} são: {alunos[a][1]}")'''

'''print("-"*40)
a=int(input("Monstar as notas de que aluno?(999 para parar):"))
while a!=999:
    print(f"As notas de {alunos[a][0]} são: {alunos[a][1]}")
    print("-"*40)
    a = int(input("Monstar as notas de que aluno?(999 para parar):"))
print("FINALIZADO \n<<< VOLTE SEMPRE >>>")'''