# Exercício 107
'''import moeda

p = float(input("Digite o preço: €"))
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p,10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p,13)}")'''

# Exercício 108
'''import moeda

p = float(input("Digite o preço: €"))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}")'''

# Exercicio 109
p = float(input("Digite o preço: €"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}")