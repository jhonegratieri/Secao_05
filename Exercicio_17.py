base_maior = float(input("Informe o tamanho da base maior do trapézio em metros:"))

if base_maior <= 0:
    print("Número inválido. Informe um número maior que 0.")
else:
    base_menor = float(input("Informe o tamanho da base menor do trapézio em metros:"))
    if base_menor <= 0:
        print("Número inválido. Informe um número maior que 0.")
    else:
        altura = float(input("Informe o tamanho da altura do trapézio em metros:"))
        if altura <= 0:
            print("Número inválido. Informe um número maior que 0.")
        else:
            area = (base_menor + base_maior) * altura * 0.5
            print(f"A área do trapézio é {area} m².")
