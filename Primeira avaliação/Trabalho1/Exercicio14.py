import math

def encontrar_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        return "Não há raízes reais"

# Solicitar os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Chamar a função para encontrar as raízes
raizes = encontrar_raizes(a, b, c)

# Imprimir as raízes encontradas
print("As raízes da equação são:", raizes)