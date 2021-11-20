print("TARIFA DE ESTACIONAMENTO")
hora_entrada, minuto_entrada = input("Informe o horário de entrada (formato HH:MM):").split(":")
hora_saida, minuto_saida = input("Informe o horário de saída (formato HH:MM):").split(":")

hora_entrada = int(hora_entrada)
minuto_entrada = int(minuto_entrada)
hora_saida = int(hora_saida)
minuto_saida = int(minuto_saida)

minutos_totais_entrada = minuto_entrada + hora_entrada * 60
minutos_totais_saida = minuto_saida + hora_saida * 60
horas_estacionados = 0

if minutos_totais_entrada < minutos_totais_saida:
    minutos_estacionados = minutos_totais_saida - minutos_totais_entrada
    horas_estacionados = minutos_estacionados // 60
    if minutos_estacionados % 60 != 0:
        horas_estacionados += 1

else:
    minutos_estacionados = 24 * 60 + minutos_totais_saida - minutos_totais_entrada
    horas_estacionados = minutos_estacionados // 60
    if minutos_estacionados % 60 != 0:
        horas_estacionados += 1

if horas_estacionados <= 2:
    print(f"Valor do estacionamento: R$ {horas_estacionados * 1}")
elif 3 <= horas_estacionados <= 4:
    print(f"Valor do estacionamento: R$ {horas_estacionados * 1.4}")
else:
    print(f"Valor do estacionamento: R$ {horas_estacionados * 2}")
