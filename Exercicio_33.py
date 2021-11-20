print("ATUALIZAÇÃO DE PREÇOS")
preco = float(input("Informe o preço antigo:"))

if preco <= 50:
    preco += 0.05 * preco
    print(f"O preço atualizado é: R$ {preco}")
elif 50 < preco <= 100:
    preco += 0.1 * preco
    print(f"O preço atualizado é: R$ {preco}")
else:
    preco += 0.15 * preco
    print(f"O preço atualizado é: R$ {preco}")

if preco <= 80:
    print("Barato")
elif 80 < preco <= 120:
    print("Normal")
elif 120 < preco <= 200:
    print("Caro")
else:
    print("Muito caro")
