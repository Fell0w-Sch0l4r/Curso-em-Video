# Exercício 16
'''from math import floor
a=float(input("\033[4:32mDigita um número:\033[m"))
print(f'\033[1:31m{floor(a)}\033[m')'''

# Exercício 17
'''from math import hypot
hip=hypot(int(input('\033[4:34mCateto Adjacente:\033[m')),int(input('\033[4:32mCateto Oposto:\033[m')))
print(f"\033[1:33mO valor da hipotenusa é "
      f"{hip}\033[m")'''

# Exercício 18
# Essa função de trigonometria apenas lê em radianos e não em graus, logo tive de converter o ângulo digitado em radiano.
'''from math import sin,cos,tan,radians
a=radians(float(input("\033[0:31mDigita um ângulo:\033[m")))
print(f"\033[4:32mCosseno é: {cos(a):.1f} !\n\033[m"
      f"\033[4:33mSeno é {sin(a):.1f} !\n\033[m"
      f"\033[1:34mTangente é {tan(a):.1f} !\033[m")'''

# Exercício 19
'''from random import choice
print("\033[1:31mO aluno escolhido foi"
      "\033[m \033[4:32m{}\033[m!"
      .format(choice([input('\033[4:33mPrimeiro aluno:\033[m'),
                      input('\033[4:34mSegundo aluno:\033[m'),
                      input('\033[4:35mTerceiro aluno:\033[m'),
                      input('\033[4:36mQuarto aluno:\033[m')])))'''

# Exercício 20
'''from random import shuffle
a=[input("\033[4:32mPrimeiro aluno:\033[m"),
   input("\033[4:33mSegundo aluno:\033[m"),
   input("\033[4:34mTerceiro aluno:\033[m"),
   input("\033[4:35mQuarto aluno:\033[m")]
shuffle(a)# O shuffe tem de ser feito ((("SOZINHO"))).
print(a)'''

# Exercício 22
'''a=input("\033[4:31mDigita o teu nome completo:\033[m")
print(f"\033[1:32m{a.upper()}\033[m")
print(f"\033[1:33m{a.lower()}\033[m")
print(f"\033[1:34mO nome {a} tem {len(a)-a.count(' ')} letras.\033[m")
print(f"\033[1:35mO nome {a.split()[0]} tem {len(a.split()[0])} letras.\033[m")'''

# Exercício 23
'''a=int(input("\033[4:31mDigita um número de 0 a 9999:\033[m"))
print(f"\033[1:32mUnidade:{a%10}\n\033[m"
      f"\033[1:33mDezena:{a//10%10}\n\033[m"
      f"\033[1:34mCentena:{a//100%10}\n\033[m"
      f"\033[1:35mMilhar:{a//1000%10}\033[m")'''

# Exercício 24
'''a=input("\033[4:33mDigita o nome de uma cidade e descobriremos se começa com Santo:\033[m")
print(f"\033[1:31m{'santo' in a.lower().split()[0]}\033[m")'''

# Exercício 25
'''a=input("\033[4:32mDigita um nome e descobriremos se o nome leva silva:\033[m")
print(f"\033[1:31m{'silva' in a.lower()}\033[m")'''

# Exercício 26
'''a=input("\033[4:31mDigita uma Frase:\033[m").strip().lower()
print(f"\033[1:32mA letra (A) aparece {a.count('a')} vezes.\033[m")
print(f"\033[1:34mAparece pela primeira vez na posição {a.find('a')+1}\033[m")
print(f"\033[1:35mAparece pela ultima vez na posicção {a.rfind('a')+1}\033[m")'''

# Exercício 27
'''b=input("\033[4:31mDigita o teu nome completo:\033[m")
print(f"\033[1:34mPrimeiro nome:{b.split()[0]}.\n\033[m"
      f"\033[1:35mUltimo nome:{b.split()[-1]}.\033[m")'''