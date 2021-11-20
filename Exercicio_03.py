numero = float(input("Informe um número real:"))

if numero >= 0:
    resultado = numero ** 0.5
    print(f"A raíz quadrada do número informado é {resultado}.")
else:
    resultado = numero ** 2
    print(f"O quadrado do número informado é {resultado}.")
