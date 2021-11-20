print("MENU DE OPÇÕES\n"
      "Soma (+): 1\n"
      "Subtração (-): 2\n"
      "Multiplicação (*): 3\n"
      "Divisão (/): 4\n")

operador_matematico = int(input("Informe o número referente a opção desejada:"))

if 1 <= operador_matematico <= 4:
    numero_1 = float(input("Informe o primeiro número no qual deseja utilizar na operação selecionada"))
    numero_2 = float(input("Agora informe o segundo número:"))

    match operador_matematico:
        case 1:
            print(f"A soma dos números é {numero_1 + numero_2}")
        case 2:
            print(f"A subtração do maior valor digitado pelo menor é {(numero_1 - numero_2).__abs__()}")
        case 3:
            print(f"A multiplicação dos valores inseridos tem como resultado {numero_1 * numero_2}")
        case _:
            print(f"A divisão do primeiro número inserido pelo segundo tem como resultado {numero_1 / numero_2}")
else:
    print("Opção inválida, tente novamente!")
