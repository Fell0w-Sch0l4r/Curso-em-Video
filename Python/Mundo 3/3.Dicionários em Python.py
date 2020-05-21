# Exercício 90

"""aluno={"Nome":input("Nome:").title().strip()}
aluno["Média"]=float(input(f"Média de {aluno['Nome']}:"))
if aluno["Média"]<5:
    aluno["Situação"]="Reprovado"
else:
    aluno["Situação"]="Aprovado"
for k,v in aluno.items():
    print(f"{k} é igual a {v}.")"""
# Exercício 91
"""from random import randint
from operator import itemgetter
from time import sleep
jogo={}
for c in range(1,5):
    jogo[f"jogador{c}"]=randint(1,6)
print("Valores sorteados:")
for k,v in jogo.items():
    print(f"    O {k} tirou {v}")
    sleep(1)
rank=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print("=-"*30)
print("  == RANKING DOS JOGADORES ==")
for l in rank:
    print(f"{rank.index(l)+1:>5}º lugar: {l[0]} com {l[1]}")
    sleep(1)"""

# Exercício 92
"""from datetime import date
informa={"Nome":input("Nome:").title().strip(),
         "Idade":date.today().year-int(input("Ano de Nascimento:")),
         "CT":int(input("Carteira de Trabalho (0 se não tiver):"))}
if informa["CT"]!=0:
    informa["Ano de contratação"]=int(input("Qual foi o ano de contratação?:"))
    informa["Salário"]=f"{input('Salário R$:')}R$"
    informa["Aposentadoria"]=(informa["Ano de contratação"]+35)-date.today().year-informa["Idade"]
for k,v in informa.items():
    print(f"{k} tem o valor {v}.")"""
# Exercício 93

"""jogador = {"Jogador": input("Nome do Jogador:"),"gols": [],"total":0}
for c in range(1,int(input(f"Quantas prtidas {jogador['Jogador']} jogou?:"))+1):
    jogador["gols"].append(int(input(f"Quantos gols na {c}º partida?: ")))
    jogador["total"] += jogador["gols"][c-1]
print("=-"*30)
print(jogador)
print("=-"*30)
for k,v in jogador.items():
    print(f"O campo {k} tem valor {v}.")
print("=-"*30)
print(f"O jogador {jogador['Jogador']} jogou {len(jogador['gols'])} partidas")
for e,n in enumerate(jogador["gols"]):
    print(f"{'=>':>5}Na {e+1}º partida, fez {n} gols. ")
print(f"Foi um total de {jogador['total']} gols.")"""

# Exercício 94
'''pessoas=[]
media=0
cont=0
while True:
    pessoas.append({"nome":input("Nome:").title().strip()})
    pessoas[cont]["sexo"]=input("Sexo [F/M]:").upper().strip()
    while pessoas[cont]["sexo"] not in "FM":
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoas[cont]["sexo"]=input("Sexo [F/M]:").upper().strip()
    pessoas[cont]["idade"]=int(input("Idade:"))
    media+=pessoas[cont]["idade"]
    cont+=1
    es=input("Quer continuar?[S/N]:").strip()
    while es not in "snSN":
        print("ERRO! Responda apenas S ou N.")
        es=input("Quer continuar?[S/N]:").strip()
    if es == "n":
        break
media/=len(pessoas)
print("=-"*35)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
print(f"B) A média de idade é de {media} anos..")
print("C) As mulheres cadstrads foram:",end=" ")
for c in pessoas:
    if c["sexo"]=="F":
        print(c["nome"],end=" ")
print()
print("D) Lista de pessoas com a idade acima da média:")
for c in pessoas:
    if c["idade"]>media:
        for k,v in c.items():
            print(f"{k:>8} = {v:<14}",end="")
        print()
print("<< ENCERRADO >>")'''


# Exercício 95
jogador,jo=[],{}
while True:
    print("-"*40)
    jo={"Jogador": input("Nome do Jogador:").title(),"gols": [],"total":0}
    for c in range(0,int(input(f"Quantas prtidas {jo['Jogador']} jogou?:"))):
        jo["gols"].append(int(input(f"Quantos gols na {c+1}º partida?: ")))
        jo["total"] += jo["gols"][c]
    jogador.append(jo.copy())
    es=input("Quer continuar?:").strip()
    if es in "Nn":
        break
print("=-"*40)
print(f"cod {'nome':<18}{'gols':<30}total")
print("-"*80)
for d,c in enumerate(jogador):
    print(f"{d:>3}",end=" ")
    for k,v in c.items():
        if k=="gols":
            print(f"{str(v):<30}", end="")
        else:
            print(f"{v:<18}",end="")
    print()
while True:
    print("-"*50)
    num=int(input("Mostrar dados de que jogador?(999 para parar):"))
    if num==999:
        break
    if num>len(jogador):
        print(f"ERRO! Não existe jogador com código {num}! Tente novamente.")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogador[num]['Jogador']}")
        for e,n in enumerate(jogador[num]["gols"]):
            print(f"{'=>':>5}No {e+1}º jogo, fez {n} gols. ")
print("<< VOLTE SEMPRE >>")
