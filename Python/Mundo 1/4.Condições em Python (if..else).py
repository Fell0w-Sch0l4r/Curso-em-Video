# Exercício 28
'''from random import randint
a=randint(0,5)
b=int(input("Digita um número entre 0 à 5 e vê se será o mesmo do PC:"))
if a==b:
    print(f"Vencente, tanto o PC como tu digitaram o número {a}!")
else:
    print(f"Que pena, o PC digitou o número {a} e tu o {b}")'''

# Rxercício 29
'''a=int(input("Escreva a velocidade do carro:"))
if a>80:
    print(f"Foste multado e terás de pagar R${(a-80)*7}!")'''

# Exercício 30
'''a=int(input("Digita um número:"))
if a%2==0:
    print(f"O número {a} é PAR.")
else:
    print(f"O número {a} é IMPAR!")'''

# Exercício 31
'''a=int(input("Digita a distância da viagem:"))
if a<200:
    print(f"A viagem custará R${a*0.5}")
else:
    print(f"A viagem custará R${a*0.45}")'''

# Exercício 32
a=int(input("Digita um ano:"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print(f"O ano {a} é bisssexto.")
        else:
            print(f"O ano {a} não é bisssexto.")
    else:
        print(f"O ano {a} é bisssexto.")
else:
    print(f"O ano {a} não é bisssexto.")

# Exercício 33
'''a=int(input("Digita o primeiro número:"))
b=int(input("Digita o segundo número:"))
c=int(input("Digita o terceiro número:"))
if a>b>c or a>c>b
if b>a>c or b>c>a
if c>a>b or c>b>a'''
# Exercício 34
'''a=int(input("Digita o valor do seu salário:"))
if a>1250:
    print(f"Receberá um aumento de 10%, passando a ser R${a+a*0.1:.2f}")
else:
    print(f"Receberá um aumento de 15%, passando a ser R${a+a*0.1:.2f}")'''

# Exercício 35
'''a=int(input("Digita o comprimento da primeira linha:"))
b=int(input("Digita o comprimento da segunda linha:"))
c=int(input("Digita o comprimento da terceia linha:"))
if a+b>c and a+c>b and c+b>a:
    print("As três linhas podem formar um triângulo.")
else:
    print("As linhas não podem formar um trângulo.")
'''