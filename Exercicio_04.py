numero = float(input("Informe um número:"))

if 0 <= numero:
    raiz_quadrada: float = numero ** 0.5
    quadrado: float = numero ** 2
    print(f"A raíz quadrada do número informado é {raiz_quadrada}.")
    print(f"O quadrado do número informado é {quadrado}.")
else:
    print("Não é um número positivo.")
