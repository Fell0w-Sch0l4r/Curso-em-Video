# Exercício 36
'''print(f"\033[4:35m{'Fazes empréstimos para comprar Casas':-^90}\033[m")
a=int(input("Digita o valor da casa:"))
b=int(input("Digita o valor do teu salário:"))
c=a/(int(input("Em quantos anos vais pagar a casa?:"))*12)
d=a/c
if c>b*0.3:
    print("O empréstimo foi negado visto que a prestação do pagamento da casa excede 30% do seu salário.")
else:
    print(f"Nós faremos um empréstimo de 500000 euros e o Sr pagará {c} euros por mês.")'''

# Exercício 37
# Exercício 38
a,b=int(input("Digita o primeirp número:")),int(input("Digita o segundo número:"))
if a>b:
    print("O primeiro número é o maior.")
elif a<b:
    print("O segundo número é o maior.")
else:
    print("Os dois números são iguais.")