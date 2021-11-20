import math

numero = int(input("Informe um número inteiro:"))

if numero > 0:
    logaritmo = math.log(numero)
    print(f"O logaritmo do número é {logaritmo}.")
else:
    print("Número inválido.")
