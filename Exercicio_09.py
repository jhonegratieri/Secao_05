salario = float(input("Informe o salário do funcionário em reais:"))
valor_parcela = float(input("Informe o valor da prestação do empréstimo em reais:"))

limite = 0.2 * salario

if valor_parcela <= limite:
    print("Empréstimo concedido.")
else:
    print("Empréstimo não concedido")
