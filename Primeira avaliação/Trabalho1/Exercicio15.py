# Calcular a interseção de duas linhas

# Calcular o determinante
a1 = float(input("Digite o coeficiente 'a' para a linha 1: "))
b1 = float(input("Digite o coeficiente 'b' para a linha 1: "))
c1 = float(input("Digite o coeficiente 'c' para a linha 1: "))

a2 = float(input("Digite o coeficiente 'a' para a linha 2: "))
b2 = float(input("Digite o coeficiente 'b' para a linha 2: "))
c2 = float(input("Digite o coeficiente 'c' para a linha 2: "))

determinante = a1 * b2 - a2 * b1

# Verificar se as linhas são paralelas
if determinante == 0:
    print("As linhas são paralelas e não se intersectam.")
else:
    # Calcular o ponto de interseção
    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    # Imprimir o resultado
    print("O ponto de interseção é: (", x, ",", y, ")")
