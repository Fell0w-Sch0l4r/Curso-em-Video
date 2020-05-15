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