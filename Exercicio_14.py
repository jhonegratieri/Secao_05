nota_trabalho = float(input("Digite a nota do Trabalho de Laboratório: "))

if nota_trabalho < 0 or nota_trabalho > 10:
    print("Nota de Trabalho de Laboratório Inválida!")
else:
    nota_avaliacao = float(input("Digite a nota da Avaliação Semestral: "))
    if nota_avaliacao < 0 or nota_avaliacao > 10:
        print("Nota de Trabalho de Avaliação Simestral Inválida!")
    else:
        nota_exame = float(input("Digite a nota do Exame Final: "))
        if nota_exame < 0 or nota_exame > 10:
            print("Nota de Trabalho de Exame Final Inválida!")
        else:
            media_ponderada = ((nota_trabalho * 2) + (nota_avaliacao * 3) + (nota_exame * 5)) / 10
            if 0 <= media_ponderada <= 2.9:
                print(f"A sua média ponderada é {media_ponderada}. Que pena! Você foi reprovado.")
            elif 3 <= media_ponderada <= 4.9:
                print(f"A sua média ponderada é {media_ponderada}. Você está de recuperação!")
            else:
                print(f"A sua média ponderada é {media_ponderada}. Parabéns! Você está aprovado!")
