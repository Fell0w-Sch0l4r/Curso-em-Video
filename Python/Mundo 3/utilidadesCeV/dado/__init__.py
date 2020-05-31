def leiaDinheiro(texto):
    '''while True:
        a = input(texto).replace(",",".").strip()
        if a.isalpha() or a=="" or a.isalnum():
            print(f"\033[31mERRO: \"{a}\" é um preço inválido!\033[m")
        else:
            return float(a)'''
    a = input(texto).replace(",", ".").strip()
    while a.isalpha() or a=="" or a.isalnum():
        print(f"\033[31mERRO: \"{a}\" é um preço inválido!\033[m")
        a = input(texto).replace(",", ".").strip()
    return float(a)