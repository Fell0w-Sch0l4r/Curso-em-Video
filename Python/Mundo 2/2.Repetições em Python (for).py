# Exercício 46
'''from time import sleep
sleep(1)
for c in range(10,-1,-1):
    print(c,end=" ")
    sleep(1)
print("")
print("BOOOOOOOOOOOOOOOOOOOOOOOOOOM")'''

# Exercício 47
'''for c in range(2,51,2):
    print(c)'''

# Exercício 48
'''a=0
cont=0
for c in range (3,501,3):
    if c%2!=0:
        cont+=1
        a+=c
print(f"A soma dos {cont} valores é {a}")'''

# Exercício 49
'''a=int(input("Digita um número:"))
for c in range (1,13):
    print(f"{a} X {c} = {a*c}")'''

# Exercício 50
'''a=0
b=0
for c in range(1,7):
    x=int(input("Digita um número:"))
    if x%2==0:
        b+=1
        a+=x
print(f"Digitou {b} números pares e a sua soma é {a}")'''

# Exercício 51
'''print("Programa de progressão aritmética.")
a=int(input("Primiro termo:"))
b=int(input("Razão:"))
m=a+10*b
for c in range(a,m,b):
    print(c,end=" -> ")
print("ACABOU")'''

# Exercício 52
'''a=int(input("Digita um número:"))
v=0
for c in range(a,0,-1):
    if a%c==0:
        v+=1
        print(f"\033[1:32m{c}\033[m",end=" ")
    else:
        print(f"\033[1:31m{c}\033[m",end=" ")
if v==2:
    print("\nO número é primo.")
else:
    print("\nO número é composto.")'''

# Exercício 53
'''a=input("Digita uma frase:").lower().split()
v="".join(a)
print(f"o inverso de {v} é {v[::-1]}")
if v==v[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo.")'''

#Exercício 54
'''from datetime import date
a=0
b=0
for c in range(1,8):
    o=date.today().year-int(input(f"Digita o ano de nascimento da {c}º pessoa:"))
    if o>=18:
        a+=1
    else:
        b+=1
print(f"{a} pessoas são adultas.")
print(f"{b} pessoas são menor de idade")'''
# Exercício 55  Fiz de uma forma diferente, mas ao mesmo tempo eficiente no commit anteriior
maior=menor=0
for c in range(1,6):
    a=float(input(f"O peso da {c}º pessoa (kg):"))
    if c==1:
        maior=menor=a
    elif a>maior:
        maior=a
    elif a<menor:
        menor=a
print(f"A pessoa mais leve pesa {menor}Kg.")
print(f"A pessoa mais cheinha pesa {maior}Kg.")
# Exercício 56
'''q=0
maior=0
mais=""
p=0
for c in range(1,6):
    print(f"{c}º PESSOA")
    a=input("Digita o seu nome:").strip().title()
    b=int(input("Digita a sua idade:"))
    q+=b
    d=input("Digita o seu sexo [F]ou[M]:").lower()
    if b>maior and d=="m":
        mais=a
        maior=b
    if d=="f" and b<20:
        p+=1
print(f"A média de idade do grupo é de {q/4}")
print(f"O homem mais velho é o {mais} que possui {maior} anos.")
print(f"O grupo possui {p} mulheres com menos de 20 anos.")'''

