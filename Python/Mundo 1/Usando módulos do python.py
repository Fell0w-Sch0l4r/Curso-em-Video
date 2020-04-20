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
