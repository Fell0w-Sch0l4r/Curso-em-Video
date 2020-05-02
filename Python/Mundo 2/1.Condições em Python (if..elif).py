# Exercício 36
'''print(f"\033[4:35m{'Fazes empréstimos para comprar Casas':-^90}\033[m")
a=float(input("Digita o valor da casa: $"))
b=float(input("Digita o valor do teu salário:"))
c=a/(int(input("Em quantos anos vais pagar a casa?:"))*12)
if c>b*0.3:
    print(f"O empréstimo foi negado visto que a prestação excede mais de 30% do seu salário, sendo ela {c:.2f} euros.")
else:
    print(f"Nós faremos um empréstimo de 500000 euros e o Sr pagará {c:.2f} euros por mês.")'''

# Exercício 37
'''a=int(input("Digita o número:"))
print("[1] Binário\n"
      "[2] Octal\n"
      "[3] Hexadecimal.")
b=int(input("A sua opção:"))
if b==1:
    print(f"{a} convertido para binário é {bin(a)[2:]}")
elif b==2:
    print(f"{a} convertido para octal é {oct(a)[2:]}")
elif b==3:
    print(f"{a} convertido para hexadecimal é {hex(a)[2:].upper()}")
else:
    print("Opção inválida, tente novamente.")'''
# Exercício 38
'''a,b=int(input("Digita o primeirp número:")),int(input("Digita o segundo número:"))
if a>b:
    print("O primeiro número é o maior.")
elif a<b:
    print("O segundo número é o maior.")
else:
    print("Os dois números são iguais.")'''

# Exercício 39
'''from datetime import date
print("\033[4:31mCalculamos o seu tempo para o alistamento militar!\033[m")
q=input("O seu sexo [F] ou [M]:").lower().strip()
if q=="m":
    a=int(input("Digita o seu ano de nascimento:"))
    b=date.today().year-a
    print(f"Quem nasceu em {a} tem {b} anos em {date.today().year}")
    if b<18:
        print(f"Vai ter de se alistar daqui a {18-b} ano(s) em {date.today().year+(18-b)}.")
    elif b==18:
        print("Vai ter de se alistar agora.")
    else:
        print(f"O seu alistamento já passou e foi à {b-18} ano(s) em {date.today().year-(b-18)}.")
else:
    print("Sendo o seu sexo feminino, não precisa fazer o alistamento militar.")'''
# Exercício 40
'''a=(float(input("Digita a primeira nota:"))+float(input("Digita a segunda nota:")))/2
if a<5:
    print(f"Reprovado, a sua média foi {a:.1f}!")
elif 5<=a<=6.9:
    print(f"Precisas de recuperação visto que a sua média foi {a:.1f}!")
else:
    print(f"Foi aprovado com uma média de {a:.1f}!")'''
# Exercício 41
'''from datetime import date
a=date.today().year-int(input("Digite o ano de nascimento do atleta:"))
if a<=9:
    print(f"O atleta de {a} anos faz parte da categoria MIRIM!")
elif 9<a<=14:
    print(f"O atleta de {a} anos faz parte da categoria INFANTIL!")
elif 14<a<=19:
    print(f"O atleta de {a} anos faz parte da categoria JUNIOR!")
elif 19<a<=25:
    print(f"O atleta de {a} anos faz parte da categoria SENIOR!")
else:
    print(f"O atleta de {a} anos faz parte da categoria MASTER!")'''

# Exercício 42
'''a=int(input("Digita o comprimento da primeira linha:"))
b=int(input("Digita o comprimento da segunda linha:"))
c=int(input("Digita o comprimento da terceia linha:"))
if a+b>c and a+c>b and c+b>a:
    print("As três linhas podem formar um triângulo.")
    if a==b==c:
        print("O triângulo formado é equilátero.")
    elif a==b or a==c or b==c:
        print("O triângulo formado é isóceles.")
    else:
        print("O triângulo formado é escaleno.")
else:
    print("As linhas não podem formar um trângulo.")'''

# Exercício 43
'''a=float(input("Digita o seu peso:(kg)"))/(float(input("Digita a sua altura:(m)"))**2)
print(f"O IMC dessa pessoa é de {a:.1f}")
if a<18.5:
    print("A pessoa está abaixo do peso.")
elif 18.5<=a<=25:
    print("A pessoa está com um peso ideal.")
elif 25<a<=30:
    print("A pessoa está com sobrepeso.")
elif 30<a<=40:
    print("A pessoa está com obsidade Obesidade.")
else:
    print("A pessoa está com obesidade mórbida")'''

# Exercício 44
'''a=int(input("Digita o preço do produto:"))
print("\033[1:32mSelecione a condição de pagamento:\033[m\n"
      "[0] À vista dinheiro/cheque.\n"
      "[1] À vista no cartão.\n"
      "[2] Em até 2x no cartão.\n"
      "[3] 3x ou mais no cartão.")
b=int(input("Condição de pagamento:"))
if b==0:
    print(f"Pagará o produto com 10% de desconto por {a-a*0.1} euros.")
elif b==1:
    print(f"Pagará o produto com 5% de desconto por {a-a*0.05} euros.")
elif b==2:
    print(f"Pagará com o preço normal por {a} euros em {a/2} por mês.")
elif b==3:
    p=int(input("Quantas parcelas:"))
    print(f"A sua compra será parcelada em {p}X de {(a+a*0.20)/p} por mês.")
    print(f"Pagará com 20% de juro por {a+a*0.20} euros.")
else:
    print("\033[1:31mOpção inválida, tente novamente.\033[ m")'''

# Exercício 45 "Jogo de pedra papel tesoura"
'''from random import choice
from time import sleep
a=choice(["pedra","papel","tesousa"])
print("[0] Pedra\n[1] Papel\n[2] Tesoura")
b=["pedra","papel","tesoura"][int(input("A sua opção:"))]
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
print(f"PC:{a}")
if a=="tesoura" and b=="papel" or a=="papel" and b=="pedra" or a=="pedra" and b=="tesoura":
    print(f"O computdor ganhou escolhendo {a}.")
elif a==b:
    print("Foi um empate.")
else:
    print(f"Você ganhou porque o computador escolheu {a}.")'''
