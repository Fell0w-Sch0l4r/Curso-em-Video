# Exercício 72
'''numeros=("Zero","Um","Dois","três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez",
        "Onze","Doze","Treze","Catorze","Quinze","Dezasseis","Dezassete","Dezoito","Dezanove","Vinte")
while True:
    a = int(input("Digite um número entre 0 a 20:"))
    while a<a or a>20:
        a=int(input("Por favor, Digite um número entre 0 a 20:"))
    print(f"Digitaste o número {numeros[a]}.")
    escolha=input("Quer continuar?").lower().strip()
    while escolha not in "sn":
        escolha = input("Quer continuar?").lower().strip()
    if escolha=="n":
        break'''

# Exercício 73
'''brasileirao=("Flamengo","Santos","Palmeiras","Grêmio","Athletico-Pr","São Paulo","Internacional","Corithians","Fortaleza","Goiás",
             "Bahia","Vasco","Athlético-Mg","Fluminense","Botafogo","Ceará","Cruzeiro","Csa","Chapecoense","Avaí")
print(f"Lista das equipas do brasileirão:{brasileirao}")
print(f"OS primeiros 5 colocados foram: {brasileirao[:6]}")
print(f"Os últimos 4 são: {brasileirao[-4:]}")
print(f"As equipas em ordem alfabética:{sorted(brasileirao)}")
print(f"O Chapecoense está na {brasileirao.index('Chapecoense')}ª posição.")'''
# Exercício 74
'''from random import randint
numeros=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print("Os valores sorteados foram:",end=" ")
maior=menor=numeros[0]
for c in numeros:
    print(c,end=" ")
print(f"\nO maior número é o {max(numeros)} é o menor o {min(numeros)}.")'''
# Exercício 75
'''valores=(int(input("Primero vloer:")),int(input("Segundo vlor:")),
         int(input("Terceiro valor:")),int(input("Quarto valor:")))
print(valores)
print(f"O valor 9 apareceu {valores.count(9)} vezes.")
if 3 in valores:
    print(f"O valor 3 apareceu na {valores.index(3)+1}ª posição ")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print("Os vaalores pares digitados foram:",end=" ")
for c in valores:
    if c%2==0:
        print(c,end=" ")'''
# Exercício 76
'''listagem=("Lápis",1.76,
          "Borracha",2,
          "Caderno",15.90,
          "Estojo",25,
          "Transferidor",4.20,
          "Compasso",9.99,
          "Mochila",120.32,
          "Canetas",22.30,
          "Livro",34.90)
print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)
for c,m in enumerate(listagem):
    if c%2==0:
        print(f"{m:.<30}R$",end="")
    else:
        print(f"{m:>7.2f}") #MEMORIZA ISSO
print("-"*40)'''
# Exercício 77
'''palavras=("aprender","programar","Linguagem","Python",
          "Curso","Gratis","Estudar","Praticar",
          "Trabalhar","Mercado","Programador","Futuro")
for vogais in palavras:
    print(f"\nNa palavra {vogais} temos:",end=" ")
    for letras in vogais.lower():
        if letras in "aeiou":
            print(letras,end=" ")'''