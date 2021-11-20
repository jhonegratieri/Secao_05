numero_1 = int(input("Informe um número inteiro:"))
numero_2 = int(input("Informe outro número inteiro:"))

if numero_1 > numero_2:
    print(f"O número {numero_1} é o maior.")
    diferenca = (numero_1 - numero_2)
    print(f"A diferença entre os números é {diferenca}.")
elif numero_2 > numero_1:
    print(f"O número {numero_2} é o maior.")
    diferenca = (numero_2 - numero_1)
    print(f"A diferença entre os números é {diferenca}.")
else:
    print("Os dois números são iguais.")
