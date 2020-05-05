# Exercício 57
'''a=input("Digite o seu sexo [M/F]:")
while a not in "fmFM":
    a=input("Por favor, digite o seu sexo [M/F]:")'''

# Exercício 58
'''print("Adivinha o entre 1 a 10, o número que o computador escolhe!")
from random import randint
a=randint(1,10)
b=1
c=int(input("Digite o seu palpite:"))
while a!=c:
    c=int(input("Tente outravés:"))
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
            print(f"O número {a} é o maior.\n")
        else:
            print(f"O número {b} é o maior.\n")
    elif c==4:
        a, b = int(input("Digite um número:")), int(input("Digite outro número:"))
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
m=10
d=0
while m!=0:
    if d!=m:
        print(a,end=" -> ")
        a+=b
        d+=1
    else:
        print("ACABOU")
        m=int(input("Mais quantos termos?:"))
        d=0
print("ACABOU")'''
# Exercício 63
'''n=int(input("Números da sequência:"))
a=0
b=1
z=0
while z<n:
    print(a,end=" ")
    a+=b
    z+=1
    if z<n:
        print(b,end=" ")
        b+=a
        z+=1'''
# Exercício 64
'''a=int(input("digite um número:"))
q=0
s=0
while a!=999:
    s+=a
    q+=1
    a=int(input("Digite outro número:"))
print(f"Foram digitados {q} números e a soma deles é {s}!")'''

# Exercício 65
q=maior=menor=a=int(input("Digite um valor:"))
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
print(f"A média dos valores digiados foi {q/z}!")
print(f"O maior valor digitado foi {maior}.\n"
      f"O menor valor digitado foi {menor}.")