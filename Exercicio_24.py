estado = input("Estados com envio disponível:\n"
               "Minas Gerais (MG)\n"
               "São Paulo (SP)\n"
               "Rio de Janeiro (RJ)\n"
               "Mato Grosso do Sul (MS)\n\n"
               "Informe o UF do estado destino do produto:").upper()

if estado == "MG" or estado == "SP" or estado == "RJ" or estado == "MS":
    valor = float(input("Informe o valor inicial do produto em reais:"))
    match estado:
        case "MG":
            print(f"Valor final do produto é {valor * 1.07} reais.")
        case "SP":
            print(f"Valor final do produto é {valor * 1.12} reais.")
        case "RJ":
            print(f"Valor final do produto é {valor * 1.15} reais.")
        case _:
            print(f"Valor final do produto é {valor * 1.08} reais.")
else:
    print("Enviamos apenas para os estados informados.")
