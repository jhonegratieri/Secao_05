print("Informe uma data. Use o formato DD/MM/AAAA:")
dia, mes, ano = input().split("/")

if (mes == "04" or mes == "06" or mes == "09" or mes == "11") and (1 <= int(dia) <= 30):
    print("A data é válida.")

elif (mes == "01" or mes == "03" or mes == "05" or mes == "07" or mes == "08" or
      mes == "10" or mes == "11") and (1 <= int(dia) <= 31):
    print("A data é válida.")

elif (int(ano) % 400 == 0 or (int(ano) % 4 == 0 and int(ano) % 100 != 0)) and (1 <= int(dia) <= 29):
    print("A data é válida.")

elif not (int(ano) % 400 == 0 or (int(ano) % 4 == 0 and int(ano) % 100 != 0)) and (1 <= int(dia) <= 28):
    print("A data é válida.")

else:
    print("A data não é válida.")
