print("Escolha uma opção:\n"
      "1 - Soma de dois números\n"
      "2 - Diferença entre dois números (maior pelo menor)\n"
      "3 - Produto entre dois números\n"
      "4 - Divisão entre dois números (o denominador deve ser diferente de zero)")
opcao = int(input("Opção: "))

if 1 <= opcao <= 4:
    numero_1 = float(input("Número 1:"))
    numero_2 = float(input("Número 2:"))
    match opcao:
        case 1:
            print(f"Resultado da operação é {numero_1 + numero_2}")
        case 2:
            print(f"Resultado da operação é {(numero_1 - numero_2).__abs__()}")
        case 3:
            print(f"Resultado da operação é {numero_1 * numero_2}")
        case _:
            if numero_2 != 0:
                print(f"Resultado da operação é {numero_1 / numero_2}.")
            else:
                print("O denominador deve ser diferente de zero!")
else:
    print("Opção inválida!")
