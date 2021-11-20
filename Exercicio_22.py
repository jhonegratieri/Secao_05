print("Para sabe se está apto a se aposentar, informe sua idade e e quantos anos de trabalho possui:")
idade = int(input("Informe quantos anos de idade possui:"))
tempo_trab = int(input("Informe quantos anos de trabalho possui:"))

if idade >= 65 or tempo_trab >= 30 or (idade >= 60 and tempo_trab >= 25):
    print("Você já pode se aposentar.")
else:
    print("Você ainda não pode se aposentar.")
