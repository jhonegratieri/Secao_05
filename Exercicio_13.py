print("Informe as três notas do aluno.")
nota_1 = float(input("Informe a primeira nota:"))
nota_2 = float(input("Informe a segunda nota:"))
nota_3 = float(input("Informe a terceira nota:"))

nota_final = nota_1 + nota_2 + 2 * nota_3

print(f"A média ponderada das notas do aluno é {nota_final / 4} pontos.")

if nota_final >= 60:
    print(f"O aluno foi aprovado com {nota_final} pontos.")
else:
    print(f"O aluno foi reprovado com {nota_final} pontos.")
