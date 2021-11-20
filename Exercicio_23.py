ano = int(input("Informe um ano, retornaremos se é bissexto ou não:"))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano informado é bissexto.")
else:
    print("O ano informado não é bissexto.")
