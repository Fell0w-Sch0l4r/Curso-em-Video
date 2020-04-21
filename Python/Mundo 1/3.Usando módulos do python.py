# Exercício 16
'''from math import floor
print(floor(float(input("Digita um número:"))))'''

# Exercício 17
'''from math import hypot
print(f"O valor da hipotenusa é "
      f"{hypot(int(input('Cateto Adjacente:')),int(input('Cateto Oposto:')))}")'''

# Exercício 18
# Essa função de trigonometria apenas lê em radianos e não em graus, logo tive de converter o ângulo digitado em radiano.
'''from math import sin,cos,tan,radians
a=radians(float(input("Digita um ângulo:")))
print(f"Cosseno é: {cos(a):.1f} !\n"
      f"Seno é {sin(a):.1f} !\n"
      f"Tangente é {tan(a):.1f} !")'''

# Exercício 19
'''from random import choice
print(f"O aluno escolhido foi {choice([input('Primeiro aluno:'),input('Segundo aluno:'),input('Terceiro aluno:'),input('Quarto aluno:')])}!")
'''
# Exercício 20
'''from random import shuffle
a=[input("Primeiro aluno:"),input("Segundo aluno:"),input("Terceiro aluno:"),input("Quarto aluno:")]
shuffle(a)# O shuffe tem de ser feito SOZINHO.
print(a)'''

# Exercício 22
'''a=input("Digita o teu nome completo:")
print(a.upper())
print(a.lower())
print(f"O nome {a} tem {len(a)-a.count(' ')} letras.")
print(f"O nome {a.split()[0]} tem {len(a.split()[0])} letras.")'''

# Exercício 23
'''a=int(input("Digita um número de 0 a 9999:"))
print(f"Unidade:{a%10}\n"
      f"Dezena:{a//10%10}\n"
      f"Centena:{a//100%10}\n"
      f"Milhar:{a//1000%10}")'''

# Exercício 24
'''a=input("Digita o nome de uma cidade e descobriremos se começa com Santo:")
print("santo" in a.lower().split()[0])'''

# Exercício 25
'''a=input("Digita um nome e descobriremos se o nome leva silva:")
print("silva" in a.lower())'''

# Exercício 26
'''a=input("Digita uma frase:").strip().lower()
print(f"A letra (A) aparece {a.count('a')} vezes.")
print(f"Aparece pela primeira vez na posição {a.find('a')+1}")
print(f"Aparece pela ultima vez na posicção {a.rfind('a')+1}")
'''
# Exercício 27
'''b=input("Digita o teu nome completo:")
print(f"Primeiro nome:{b.split()[0]}.\nUltimo nome:{b.split()[-1]}.")'''