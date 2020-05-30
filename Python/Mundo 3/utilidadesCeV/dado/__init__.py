def leiaDinheiro(texto):
    a = input(texto)
    if "," in a:
        b=""
        for c in a:
            if c == ",":
                b += "."
            else:
                b+=c

    while not a.isdecimal():
        print(f"\033[31mERRO: {a} é um preço inválido!\033[m")
        a = input(texto)
    return a