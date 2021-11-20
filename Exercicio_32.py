print("COMANDA:")
codigo = int(input("Informe o códgio do produto:"))

if 100 <= codigo <= 106:
    quantidade = int(input("Informe a quantidade:"))

    match codigo:
        case 100:
            print(f"Valor total: R$ {1.2 * quantidade}")
        case 101:
            print(f"Valor total: R$ {1.3 * quantidade}")
        case 102:
            print(f"Valor total: R$ {1.5 * quantidade}")
        case 103:
            print(f"Valor total: R$ {1.2 * quantidade}")
        case 104:
            print(f"Valor total: R$ {1.7 * quantidade}")
        case 105:
            print(f"Valor total: R$ {2.2 * quantidade}")
        case _:
            print(f"Valor total: R$ {quantidade}")

else:
    print("Código inválido!")
