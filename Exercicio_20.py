print("Informe os três lados do triângulo a ser verificado.")
lado_A = float(input("Lado A:"))
lado_B = float(input("Lado B:"))
lado_C = float(input("Lado C:"))

if (lado_A + lado_B > lado_C) and (lado_C + lado_B > lado_A) and (lado_A + lado_C > lado_B):

    if lado_A == lado_B == lado_C:
        print("É um triângulo equilátero")
    elif lado_A != lado_B != lado_C:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")

else:
    print("Os valores não podem ser atribuidos a lados de um triângulo.")
