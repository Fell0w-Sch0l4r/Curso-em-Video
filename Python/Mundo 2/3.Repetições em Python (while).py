# Exercício 57
'''a=input("Digite o seu sexo [M/F]:")
while a not in "fmFM":
    a=input("Por favor, digite o seu sexo [M/F]:")'''

# Exercício 58
'''print("Adivinha o entre 0 a 10, o número que o computador escolhe!")
from random import randint
a=randint(0,10)
b=1
c=int(input("Digite o seu palpite:"))
while a!=c:
    if a<c:
        c = int(input("Tente outravés com um número menor:"))
        b += 1
    else:
        c=int(input("Tente outravés  com um número maior:"))
        b+=1
print("Parabens, acertaste.")
print(f"Acertaste na {b}º tentativa.")'''

# Exercício 59
'''a,b=int(input("Digite um número:")),int(input("Digite outro número:"))
print("[1] Somar\n"
      "[2] Multiplicar\n"
      "[3] O Maior\n"
      "[4] Digitar novos números\n"
      "[5] Sair do programa\n")
c=int(input("A sua escolha:"))
while c!=5:
    if c==1:
        print(f"A soma de {a} com {b} é {a+b}!\n")
    elif c==2:
        print(f"{a} X {b} = {a*b} !\n")
    elif c==3:
        if a>b:
            print(f"Entre {a} e {b}, o número {a} é o maior.\n")
        elif a<b:
            print(f"Entre {a} e {b}, o número {b} é o maior.\n")
        else:
            print("Os números digitados são iguais.")
    elif c==4:
        a, b = int(input("Digite um número:")), int(input("Digite outro número:"))
    else:
        print("Por favor, escolha uma opção.")
    print("[1] Somar\n"
          "[2] Multiplicar\n"
          "[3] O Maior\n"
          "[4] Digitar novos números\n"
          "[5] Sair do programa\n")
    c = int(input("A sua escolha:"))'''
# Exercício 60
# Com o for
'''a=int(input("Digite um número para fazer o seu fatorial:"))
print(f"{a}! =",end=" ")
for c in range(a,0,-1):
    if a==c:
        print(f"{c}",end=" ")
    else:
        print(f"x {c}",end=" ")
        a*=c
print(f"= {a}")'''
# Com o while
'''a=b=int(input("Digite um número para fazer o seu fatorial:"))
print(f"{a}!=",end=" ")
while b!=0:
    if a == b:
        print(f"{b}", end=" ")
    else:
        print(f"x {b}", end=" ")
        a *= b
    b-=1
print(f"= {a}")'''
# Exercício 61
'''print("Programa de progressão aritmética.")
a=int(input("Primiro termo:"))
b=int(input("Razão:"))
m=0
while m!=10:
    print(a,end=" -> ")
    a+=b
    m+=1
print("ACABOU")'''

# Exercício 62
'''print("Programa de progressão aritmética.")
a=int(input("Primiro termo:"))
b=int(input("Razão:"))
m=c=10
d=0
while m!=0:
    if d!=m:
        print(a,end=" -> ")
        a+=b
        d+=1
    else:
        print("PAUSA")
        m=int(input("Mais quantos termos?:"))
        c+=m
        d=0
print(f"Progressão aritmética finalizada com {c} termos.")'''
# Exercício 63
'''print("Sequência de Fibonacci")
n=int(input("Quantos números quer mostar?:"))
a=0
b=1
while n>0:
    print(a,end=" > ")
    a+=b
    n-=1
    if n!=0:
        print(b,end=" > ")
        b+=a
        n-=1
print("FIM")'''
# Exercício 64
'''a=int(input("digite um número:"))
q=s=0
while a!=999:
    s+=a
    q+=1
    a=int(input("Digite outro número:"))
print(f"Foram digitados {q} números e a soma deles é {s}!")'''
# Exercício 65
'''q=maior=menor=a=int(input("Digite um valor:"))
s=input("Quer continuar [S/N]:").lower().strip()
z=1
while s=="s":
    a=int(input("Digite outro valor:"))
    q+=a
    z+=1
    if a>maior:
        maior=a
    elif a<menor:
        menor=a
    s=input("Quer continuar?:")
print(f"Foram digitados {z} números com a média de {q/z}!")
print(f"O maior valor digitado foi {maior}.\n"
      f"O menor valor digitado foi {menor}.")'''