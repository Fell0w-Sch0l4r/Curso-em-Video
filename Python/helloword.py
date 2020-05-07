a,b=int(input("Digite um número:")),int(input("Digite outro número:"))
print("[1] Somar\n"
      "[2] Multiplicar\n"
      "[3] O Maior\n"
      "[4] Digitar novos números\n"
      "[5] Sair do programa\n")
c=int(input("A sua escolha:"))
while c!=5:
    if c==1:
        print(f"A soma de {a} com {b} é {a+b}!\n")
    elif c==2:
        print(f"{a} X {b} = {a*b} !\n")
    elif c==3:
        if a>b:
            print(f"Entre {a} e {b}, o número {a} é o maior.\n")
        elif a<b:
            print(f"Entre {a} e {b}, o número {b} é o maior.\n")
        else:
            print("Os números digitados são iguais.")
    elif c==4:
        a, b = int(input("Digite um número:")), int(input("Digite outro número:"))
    else:
        print("Por favor, escolha uma opção.")
    print("[1] Somar\n"
          "[2] Multiplicar\n"
          "[3] O Maior\n"
          "[4] Digitar novos números\n"
          "[5] Sair do programa\n")
    c = int(input("A sua escolha:"))