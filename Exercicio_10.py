print("Para que seu peso ideal seja exibido, por favor informe sua altura e sexo biológico.")
altura = float(input("Altura em metros:"))
sexo = input("Sexo:\n")

if sexo.title() == "Masculino":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal} quilogramas.")
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal} quilogramas.")
