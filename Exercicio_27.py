idade = int(input("Informe sua idade, será retornado em qual categoria você se enquadra:"))

if 5 <= idade <= 7:
    print("Categoria: Infantil A.")
elif 8 <= idade <= 10:
    print("Categoria: Infantil B.")
elif 11 <= idade <= 13:
    print("Categoria: Juvenil A.")
elif 17 <= idade <= 17:
    print("Categoria: Juvenil B.")
else:
    print("Categoria: Sênior.")
