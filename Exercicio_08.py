print("Informe duas notas de um aluno. Lembre-se: notas válidas estão em um intervalo de 0 a 10 pontos.")
nota_1 = float(input("Informe a primeira nota do aluno:"))
nota_2 = float(input("Informe a segunda nota do aluno:"))

if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
    media = (nota_1 + nota_2) / 2
    print(f"A média das notas é {media} pontos.")
elif not (0 <= nota_1 <= 10) and not (0 <= nota_2 <= 10):
    print("Ambas as notas não são válidas.")
elif not (0 <= nota_1 <= 10):
    print("A primeira nota não é válida.")
else:
    print("A segunda nota não é válida.")
